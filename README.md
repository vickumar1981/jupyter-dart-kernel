# Swift kernel for Project Jupyter

A simple kernel that adds Apple's [Swift programming language](https://swift.org) into [Project Jupyter](https://jupyter.org).

Thanks to [O'Reilly Media](http://www.oreilly.com) for sponsoring this development, I would never have gotten around to this without them.

This is implemented as a Python wrapper kernel and supports the basic functionality of Jupyter in both the console and in notebooks.
It works by creating a temporary file, dumping the user text into the file and running that through swift.
The output is captured, massaged a little bit, and then sent back to Jupyter.

## Installation

### Requirements

- Swift 3
- Python (I used 2.7 but 3 should also be fine)
- Jupyter

### Steps

1. [Install Swift](https://swift.org/download/) for your platform
2. [Install Jupyter](http://jupyter.org/install.html)
3. Download the kernel and save it somewhere memorable. The important files are `kernel.json` and `swiftkernel.py`
4. Install the kernel into Jupyter: `jupyter kernelspec install /path/to/swiftkernel --user`
  - You can verify the kernel installed correctly: `jupyter kernelspec list`
  - It will appear in the list of kernels installed under the name of the project folder
5. Run Jupyter and start using Swift
  - To use the kernel in the Jupyter console: `jupyter console --kernel kernelname`
  - to use the kernel in a notebook: `jupyter notebook` and create a new notebook through the browser

## Caveats

- If you crash the kernel or Jupyter without exiting it will leave temporary files called `canonical.swift` and `scratch.swift` on your machine.
- Unlike many other Jupiter kernels if you type something like `1 + 1` it will display no result because of how I implemented the kernel. So wrap any code like that inside a `print()` call to see it. The code will still run so you can do things like `let thing = 5` and then later `print(thing)` and this will work fine.
- errors just appear underneath the code as valid output.

## Future features

- Add prints to non-printing statements
- Proper error handling
- Implement Jupyter's nice to have features
- Work out a better way of interfacing with Swift that doesn't need temporary files
- Support warnings instead of just ignoring them
- Add in proper tests

## FAQ

**Tim, did anyone actually ask you any of these?**

No, but I've always wanted to answer an FAQ so I made one up.

**Tim, why do you write in this manner?**

I'm gonna blame being Australian, sure, yeah, let's go with that.

**Does this work on Linux?**

I did all my development on MacOS but I did test it briefly on Ubuntu and it seemed ok, so yeah..?

**Why a wrapper kernel?**

It is the fastest and easiest way to get a Jupyter kernel up and running. The initial idea was to wrap the Swift REPL using replwrap but that fell apart quickly when I realised that the Swift REPL does a few weird things that make it tricky to wrap. At that point I'd already created a file called `swiftkernel.py` and thought I might as well keep going with Python anyway.

**Why Python 2.7 and not 3.x?**

It is what was installed on my Macbook. Nothing I've done is 2.7 specific and everything will work fine in Python 3.x. As I already had 2.7 installed on my machine I didn't see the benefit in installing another version. Had I realised how weird the default macOS install of Python was I probably would have.

**I typed a statement in, ran it and nothing appeared, what gives?**

Because of how it is currently implemented statements that are non-printing, such as `1 + 1` or `let thing = 4`, do not display any result back to Jupyter. I plan on updating the code to fix this but for now just add a print statement in yourself on anything you want to see. Your code will still run fine, it just won't display anything until you make it.

**I keep getting an error saying something like "No module named SwiftKernel" when running the kernel what's up?**

I had this appear almost randomly during development as I have a very broken installation of Python on my Macbook from years of doing horrible things to it. I fixed it by manually setting PYTHONPATH in Bash to where the kernel was installed by Jupyter and this fixed it. According to the Jupyter docs this shouldn't be necessary but hey, maybe you've also done terrible things to Python.

**Tim, this Python code looks like it was written by someone who doesn't know how to Python**

That'd be me, I am a Swift, mobile, and game developer. I normally only use Python when I need to make something quick and dirty for scripting, this is my first Python program longer than about 30 lines of code.
Please fix it up and send in a pull request.

**Tim, you've used Library X incorrectly**

See above answer.

**Can I help with this?**

Please do! Improve my documentation, submit a pull request, open an issue, [tweet at me](https://twitter.com/the_mcjones) saying you like the kernel, buy me a drink or socks, etc etc. I would love for some other people to help make this better than what it currently is.
