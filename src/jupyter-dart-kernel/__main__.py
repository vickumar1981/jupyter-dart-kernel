#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import DartKernel
IPKernelApp.launch_instance(kernel_class=DartKernel)

