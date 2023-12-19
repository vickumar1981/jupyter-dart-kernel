![alt](jupyterdartkernel/logo-svg.svg)

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
6. `jupyterdartkernel` or `jupyter kernelspec install --user jupyterdartkernel`
  - To use the kernel in the Jupyter console: `jupyter console --kernel jupyterdartkernel`
  - to use the kernel in a notebook: `jupyter notebook` and create a new notebook through the browser
  
## Uninstall

- `jupyter kernelspec uninstall jupyterdartkernel`
- `pip uninstall jupyterdartkernel`
