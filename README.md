# Dart kernel for Project Jupyter

A simple kernel that adds the  [Dart programming language](https://Dart.org) into [Project Jupyter](https://jupyter.org).

## Try out the kernel online: [https://gotocode.io](https://gotocode.io)

[![Gotocode](https://gotocode.io/static/assets/img/logo.jpg)](https://gotocode.io)

### Requirements

- Dart
- Python 3
- Jupyter

### Steps

1. [Install Dart](https://dart.dev/get-dart) for your platform
2. [Install Jupyter](http://jupyter.org/install.html)
3. Download the kernel and save it somewhere memorable. The important files are `kernel.json` and `dartkernel.py`
4. Install the kernel into Jupyter: `jupyter kernelspec install /path/to/dartkernel --user`
  - You can verify the kernel installed correctly: `jupyter kernelspec list`
  - It will appear in the list of kernels installed under the name of the project folder
5. Run Jupyter and start using Dart
  - To use the kernel in the Jupyter console: `jupyter console --kernel kernelname`
  - to use the kernel in a notebook: `jupyter notebook` and create a new notebook through the browser
  
  
### Getting an Error:  `No module named dartkernel`


1. Make sure dart is installed and accessible via the path. You can check this by opening a terminal / command prompt and typing: dart --version.

2. Make sure the location of where the jupyter-dart-kernel is installed is in your PYTHONPATH. This is where the python interpreter looks for modules, including the dartkernel.py file.



