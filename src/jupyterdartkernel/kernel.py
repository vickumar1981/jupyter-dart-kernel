# coding: utf-8

import subprocess, os, shutil, tempfile, re
from ipykernel.kernelbase import Kernel

class dartkernel(Kernel):
    implementation = 'Dart'
    implementation_version = '1.0.0'
    language = 'dart'
    language_version = '2.18.5'
    language_info = {'mimetype': 'application/dart', 'file_extension': 'dart', 'name': 'dart'}
    banner = "Dart kernel"

    # pubspec.yaml template
    pubspec = ("name: dart_kernel_app\n"
               "description: A dart kernel depenency controller.\n"
               "publish_to: 'none'\n"
               "\n"
               "version: 1.0.0+1\n"
               "\n"
               "environment:\n"
               "  sdk: '>=3.1.5 <4.0.0'\n"
               ""
               "dependencies:\n"
               "  flutter:\n"
               "    sdk: flutter\n"
               "\n"
               "%s")

    output = ""
    dartDirectory = tempfile.mkdtemp()
    
    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        errorCode, dump = self.runCode(code)
        
        if errorCode == 0:
            
            if not silent:
                stream = {'name':'stdout', 'text':dump.decode('utf-8')}
                self.send_response(self.iopub_socket, 'stream', stream)
    
            return {
                        'status':'ok',
                        'execution_count':self.execution_count,
                        'payload':[],
                        'user_expressions':{}
                   }
        else:
            # every example does it like this but this just feels weird
            # why does the execution_count increment?!
            if not silent:
                stream = {
                            'status' : 'error',
                            'ename': 'ERROR',
                            'evalue': 'error',
                            'traceback': dump
                         }
                self.send_response(self.iopub_socket, 'error', stream)
        
            return {
                        'status':'error',
                        'execution_count':self.execution_count,
                        'ename': 'ERROR',
                        'evalue': 'error',
                        'traceback': dump
                   }

    def do_shutdown(self, restart):
        shutil.rmtree(self.dartDirectory)

    def runCode(self, command):
        dartFileLocation = os.path.join(self.dartDirectory, 'scratch.dart')
        canonicalFile = os.path.join(self.dartDirectory, 'canonical.dart')
        runFile = os.path.join(self.dartDirectory, 'main.dart')
        specFile = os.path.join(self.dartDirectory, 'pubspec.yaml')
    
        if os.path.isfile(canonicalFile):
            shutil.copyfile(canonicalFile, dartFileLocation)
        
        with open(dartFileLocation, 'ab') as dartFile:
            unicodeCommand = (command + "\n").encode("UTF-8")
            dartFile.write(unicodeCommand)

        rf = open(dartFileLocation, "r")
        lines_read = rf.readlines()
        rf.close()

        (code_lines, import_lines, class_lines) = (["void main() {\n"], list(), list())
        idx = 0
        while idx < len(lines_read):
            curr_line = lines_read[idx]
            if curr_line.startswith("import "):
                import_lines.append(curr_line)
            elif curr_line.startswith("class ") or curr_line.startswith("abstract "):
                class_lines.append(curr_line)
                open_brackets = 0
                open_brackets += curr_line.count("{")
                open_brackets -= curr_line.count("}")
                while open_brackets > 0 and idx < len(lines_read) - 1:
                    idx += 1
                    class_line = lines_read[idx]
                    open_brackets += class_line.count("{")
                    open_brackets -= class_line.count("}")
                    class_lines.append(class_line)
            else:
                code_lines.append(curr_line)
            idx += 1
        code_lines.append("}\n")
        wf = open(runFile, "w")
        wf.writelines(import_lines)
        wf.write("\n")
        wf.writelines(class_lines)
        wf.write("\n")
        wf.writelines(code_lines)
        wf.close()
        
        if import_lines:
            # write the pubspec.yaml file to the template direcotory
            with open(specFile, "w") as f:
                # extract package name and version from comment in the end of the import line
                # example of the comment:
                # `xml: ^6.3.0`
                # `intl: "^0.18.1"`
                imp = re.findall("^\s*import[^;]+;\s*\/\/\s*(\w+):(.*)", "\n".join(import_lines), re.MULTILINE)
                spec = "\n".join( "  %s: %s" % (x[0].strip(), x[1].strip()) for x in imp )
                f.write(self.pubspec % spec)
        
        error_output = []
        os.chdir(self.dartDirectory)

        # run resolve dependencies before run 
        cmd = 'dart pub get; dart {0}'.format(runFile)
        dart = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        new_output = dart.stdout.read()

        for line in dart.stderr.readlines():
            line = re.sub('^.*error: ', '', line.decode('utf-8'))
            error_output.append(line.rstrip("\n\r"))
        
        retval = dart.wait()
        
        # ran without error
        if retval == 0:
            # putting the valid code back into the canonical file
            shutil.copyfile(dartFileLocation, canonicalFile)
            # returning the result
            diff = new_output[len(self.output):]
            self.output = new_output
            return 0, diff
        else:
            os.remove(dartFileLocation)
            return 1, error_output
