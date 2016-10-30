# KDS Codeathon Kivy Starter

##Intro:
This respository will help you get started on your own mobile app using [Kivy](https://kivy.org/docs/), a Python mobile app framework. Coments will be provided throughout the starter code. Comments in Python (and Kivy files) are any text after a #:

```python
#This is a comment.
#Here we define our main app class, StarterApp.
class StarterApp(App):
  pass
```
## Getting Started

#### Getting pip

Unfortunately, this repository is not the only thing you need to get started. In order to install Kivy and any other programs you might need we are going to use **pip**. You will need to install pip by downloading this file: [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Please right click that link and say "Save File As..." Put it in your downloads

You will then run that file by using Terminal (OSX) or Command Prompt (Windows) to run these commands:

```
cd Downloads
python get-pip.py
```

This means that you can now use the command `pip`, hurrah!

#### Getting a copy of this project

You are now ready to grab your very own copy of this project. If you know how to use git, feel free to clone this repo. If that last sentence didn't make any sense, don't worry. You can just download the .zip of this entire project from that big green button in the upper right like this:

![zip download](https://github.com/MrClement/KDS-Hack2016-DjangoStarter/raw/master/resources/clone.png "How to download a zip archive")

If you downloaded the zip file, unzip it and move it out of your downloads folder. You will be working from that folder for the rest of this project, so keep it accessible.

#### Installing requirements

You now need to install the requirements for this project. It is simple now that you have `pip`. In terminal (or command prompt) run the following commands (you can copy paste).

1. Ensure you have the latest pip and wheel:
```
python -m pip install --upgrade pip wheel setuptools
Install the dependencies (skip gstreamer (~90MB) if not needed, see Kivy’s dependencies):
```
2. Ensure you have the latest pip and wheel:
```
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/
```
3. Install kivy:
```
python -m pip install kivy 
```
That should be it! Check if you have kivy by typing or copying the following in the command line:
``` python -m kivy 
```
This should print your kivy version (something like [info   ][kivy   ] v1.9.1) followed by info about your python version and some other messages.
