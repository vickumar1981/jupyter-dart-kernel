# coding: utf-8

# a swift kernel for Jupyter
# copyright Tim Nugent, made available under the MIT License
# see the repository https://github.com/McJones/jupyter-swift-kernel/ for full details

import subprocess, os, shutil, tempfile, re, json
from ipykernel.kernelbase import Kernel

class SwiftKernel(Kernel):
    # Jupiter stuff
    implementation = 'Swift'
    implementation_version = '1.1.1'
    language = 'swift'
    language_version = '3.0.2'
    language_info = {'mimetype': 'text/plain', 'file_extension': 'swift', 'name': 'swift'}
    banner = "Swift kernel"
    # my stuff
    output = ""
    swiftDirectory = tempfile.mkdtemp()
    
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
        # delete the temporary swift file(s) and directory
        shutil.rmtree(self.swiftDirectory)

    # appends the new text to the swift file
    # runs the swift file
    # capture all output
    # returns the result
    def runCode(self, command):
        swiftFileLocation = os.path.join(self.swiftDirectory, 'scratch.swift')
        canonicalFile = os.path.join(self.swiftDirectory, 'canonical.swift')
        
        # now copy everything from canonical into the scratch
        if os.path.isfile(canonicalFile):
            shutil.copyfile(canonicalFile, swiftFileLocation)
        
        with open(swiftFileLocation, 'ab') as swiftFile:
            unicodeCommand = (command + "\n").encode("UTF-8")
            swiftFile.write(unicodeCommand)
            
        errorOutput = []
        
        # because who needs warnings, right?!
        # queue up mental picture of Holtzman while reading the above comment please
        cmd = 'swift -suppress-warnings {0}'.format(swiftFileLocation)
        swift = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # handle all valid output
        newOutput = swift.stdout.read()
        
        # handle any errors
        for line in swift.stderr.readlines():
            # to clean up the default error message swift returns
            line = re.sub('^.*error: ', '', line.decode('utf-8'))
            errorOutput.append(line.rstrip("\n\r"))
        
        retval = swift.wait()
        
        # ran without error
        if retval == 0:
            # putting the valid code back into the canonical file
            shutil.copyfile(swiftFileLocation, canonicalFile)
            # returning the result
            diff = newOutput[len(self.output):]
            self.output = newOutput
            return 0, diff
        else:
            # dumping the dodgy file
            os.remove(swiftFileLocation)
            # returning the error(s)
            return 1, errorOutput

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=SwiftKernel)
