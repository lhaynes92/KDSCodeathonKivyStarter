# KDS Codeathon Kivy Starter

##Intro:
This respository will help you get started on your own mobile app using [Kivy](https://kivy.org/docs/), a Python mobile app framework. Coments will be provided throughout the starter code. Comments in Python (and Kivy files) are any text after a #:

```python
#This is a comment.
#Here we define our main app class, StarterApp.
class StarterApp(App):
  pass
```
## Getting Started:

#### Getting pip

Unfortunately, this repository is not the only thing you need to get started. In order to install Kivy and any other programs you might need we are going to use **pip**. You will need to install pip by downloading this file: [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Please right click that link and say "Save File As..." Put it in your downloads

You will then run that file by using Terminal (OSX) or Command Prompt (Windows) :

MAC: To open Terminal, search "Terminal" in Spotlight and select the application
Windows: To open Command Prompt, hit the windows key and type "Command Prompt".

In the Terminal/Command Prompt, type or paste the following commands:

```
cd Downloads
python get-pip.py
```

This means that you can now use the command `pip`, hurrah!

#### Getting a copy of this project

You are now ready to grab your very own copy of this project. If you know how to use git, feel free to clone this repo. If that last sentence didn't make any sense, don't worry. You can just download the .zip of this entire project from that big green button in the upper right like this:

![zip download](https://github.com/lhaynes92/KDSCodeathonKivyStarter/blob/master/Resources/Clone.png "How to download a zip archive" | height=250)

If you downloaded the zip file, unzip it and move it out of your downloads folder. You will be working from that folder for the rest of this project, so keep it accessible.

#### Installing requirements **for MacOS**

1. Install Homebrew by pasting the following command into your terminal.
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Now we can use brew to install requirements:
```
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
```
3. Finally we use pip to install Kivy and Cython (needed for kivy).
```
sudo -H pip install -I Cython==0.23
sudo -H USE_OSX_FRAMEWORKS=0 pip install kivy
```

That should be it! Check if you have kivy by typing or copying the following in the command line:
``` 
python -m kivy 
```

#### Installing requirements **for Windows**

You now need to install the requirements for this project. It is simple now that you have `pip`. 
0. command prompt) run the following commands (you can copy paste).

1. Ensure you have the latest pip and wheel:
```
python -m pip install --upgrade pip wheel setuptools
```
Install the dependencies (skip gstreamer (~90MB) if not needed, see Kivy’s dependencies):

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
``` 
python -m kivy 
```
This should print your kivy version (something like `[info   ][kivy   ] v1.9.1`) followed by info about your python version and some other messages.

#### Getting Started in Kivy

Kivy is based around Widgets, a class that handles events and formatting for UI components. Although it is possible to code your entire Kivy app in a Python code file (extension .py), it is cleaner to move the construction of the widgets into a separate Kivy language file (extension .kv). Kivy language is built to facilitate easy nesting and organization of Widgets, the behavior of which can then be defined in the accompanying Python language file.

In the example code folder you downloaded should see two files: 
```
MyFirstApp.py
Starter.kv
```
Kivy will automatically import your Kivy file into your Python program if your .kv file has the same name as the **App class** you define in your Python file without the word App (case doesn't matter).

#####Inside the starter Python file
```python

class StarterApp(App):
  def build(self):
    pass
```
So our associated Kivy file is named `Starter.kv`.

You can run the starter code by navigating to the starter code folder in Terminal or Command line, then typing:
```
python MyFirstApp.py
```
## Get hacking

Start changing the code. Break it, improve it, make it your own. Don't forget to ask for help if you need it or consult [Kivy's Documentation](https://kivy.org/docs/api-kivy.html).

#### A few last hints:

- There are a few useful tutorials starting [here](https://kivy.org/docs/tutorials/pong.html#) if you want more jumping off places.
- There are fairly extensive comments in the starter code that describe what is happening as well.
 - In both python and kivy files comments start with the `#` symbol
