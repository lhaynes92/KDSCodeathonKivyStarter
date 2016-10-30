#Starter App
#Importing different Widgets and event handlers
#

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from random import *


class parent(FloatLayout):
	pass


class StarterApp(App):
	def build(self):
		return parent()

if __name__ == '__main__':
	StarterApp().run()