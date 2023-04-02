#!/usr/bin/env python
import os, shutil
from jupyter_client.kernelspec import KernelSpecManager

json = """{"argv":["python","-m","jupyterdartkernel", "-f", "{connection_file}"],
	"display_name":"Dart"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
   version="1.1"
   id="Layer_1"
   viewBox="0 0 300 300.00001"
   enable-background="new 0 0 439 137.29"
   xml:space="preserve"
   width="300"
   height="300"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"><defs
   id="defs80" />
<g
   id="g75"
   transform="matrix(2.1875172,0,0,2.1875172,-3.0277657,-0.17305578)">
	<g
   opacity="0.54"
   id="g48">
		
		
		
	</g>
	<g
   id="g73">
		<path
   fill="#01579b"
   d="M 29.64,108.94 6.36,85.66 C 3.6,82.82 1.88,78.82 1.88,74.91 1.88,73.1 2.9,70.27 3.67,68.64 L 25.16,23.87 Z"
   id="path50" />
		<path
   fill="#40c4ff"
   d="M 109.34,28.35 86.06,5.07 C 84.03,3.03 79.79,0.59 76.21,0.59 c -3.08,0 -6.1,0.62 -8.06,1.79 L 25.17,23.87 Z"
   id="path52" />
		<polygon
   fill="#40c4ff"
   points="33.23,112.52 57.4,136.7 113.82,136.7 113.82,112.52 71.73,99.09 "
   id="polygon54" />
		<path
   fill="#29b6f6"
   d="m 25.17,96.41 c 0,7.18 0.9,8.95 4.48,12.54 l 3.58,3.58 h 80.59 L 74.42,67.76 25.17,23.88 Z"
   id="path56" />
		<path
   fill="#01579b"
   d="M 96.8,23.87 H 25.16 l 88.65,88.65 h 24.18 V 57 L 109.34,28.35 c -4.02,-4.04 -7.6,-4.48 -12.54,-4.48 z"
   id="path58" />
		<path
   opacity="0.2"
   fill="#ffffff"
   enable-background="new    "
   d="m 30.54,109.84 c -3.58,-3.6 -4.48,-7.14 -4.48,-13.43 V 24.77 l -0.9,-0.9 V 96.4 c 0.01,6.3 0.01,8.04 5.38,13.44 l 2.69,2.69 v 0 z"
   id="path60" />
		<polygon
   opacity="0.2"
   fill="#263238"
   enable-background="new    "
   points="113.82,112.52 138,112.52 138,57.01 137.1,56.11 137.1,111.63 112.92,111.63 "
   id="polygon62" />
		<path
   opacity="0.2"
   fill="#ffffff"
   enable-background="new    "
   d="M 109.34,28.35 C 104.9,23.91 101.26,23.87 95.91,23.87 H 25.17 l 0.9,0.9 h 69.85 c 2.66,0 9.41,-0.45 13.42,3.58 z"
   id="path64" />

			<radialGradient
   id="SVGID_1_"
   cx="69.955002"
   cy="60.886398"
   r="68.065002"
   gradientTransform="matrix(1,0,0,-1,0,129.5328)"
   gradientUnits="userSpaceOnUse">
			<stop
   offset="0"
   style="stop-color:#FFFFFF;stop-opacity:0.1"
   id="stop66" />
			<stop
   offset="1"
   style="stop-color:#FFFFFF;stop-opacity:0"
   id="stop68" />
		</radialGradient>
		<path
   opacity="0.2"
   fill="url(#SVGID_1_)"
   enable-background="new    "
   d="M 137.1,56.11 109.34,28.35 86.06,5.07 C 84.03,3.03 79.79,0.59 76.21,0.59 c -3.08,0 -6.1,0.62 -8.06,1.79 L 25.17,23.87 3.68,68.64 c -0.77,1.63 -1.79,4.46 -1.79,6.27 0,3.91 1.72,7.91 4.48,10.75 l 21.46,21.3 c 0.51,0.63 1.11,1.27 1.83,1.98 l 0.9,0.9 2.69,2.69 23.28,23.28 0.9,0.9 h 55.52 0.9 v -24.18 h 24.18 v -0.06 -55.46 z"
   id="path71"
   style="fill:url(#SVGID_1_)" />
	</g>
</g>
</svg>"""

def install_kernelspec():
    kerneldir = "/tmp/jupyterdartkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'jupyterdartkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall jupyterdartkernel')
    