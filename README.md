![alt](jupyter-dart-kernel/logo-svg.svg)

# Dart kernel for Project Jupyter

A simple kernel that adds the  [Dart programming language](https://Dart.org) into [Project Jupyter](https://jupyter.org).

## Try out the kernel online: [https://gotocode.io](https://gotocode.io)

[![Gotocode](https://gotocode.io/static/assets/img/logo.jpg)](https://gotocode.io)

### Requirements

- Dart
- Python 3
- Jupyter

### Dev Install

1. [Install Dart](https://dart.dev/get-dart) for your platform
2. [Install Jupyter](http://jupyter.org/install.html)
3. Download the kernel and save it somewhere memorable.
4. Open shell in project folder
5. `pip install -e ./`
6. `jupyter kernelspec install --user jupyter-dart-kernel`
  - To use the kernel in the Jupyter console: `jupyter console --kernel jupyter-dart-kernel`
  - to use the kernel in a notebook: `jupyter notebook` and create a new notebook through the browser
  
## Uninstall

- `jupyter kernelspec uninstall jupyter-dart-kernel`
- `pip uninstall jupyter-dart-kernel`
