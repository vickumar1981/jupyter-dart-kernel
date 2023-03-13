#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import dartkernel
IPKernelApp.launch_instance(kernel_class=dartkernel)

