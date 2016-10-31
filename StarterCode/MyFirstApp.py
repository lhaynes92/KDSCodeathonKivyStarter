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
from kivy.storage.jsonstore import JsonStore

class parent(FloatLayout):
	
	def logIn(self):
		'''Checks the JSON file for an existing username and associated password,
		if the username doesn't exist stores the username and password as 
		a key and value pair in a Dictionary.'''
		name = self.ids.name_input.text
		password = self.ids.password_input.text
		if (self.store.exists(name)):
			realPass = self.store.get(name)['password']
			if (realPass == password):
				self.ids.login_message.text = "Success! Welcome "+ name + "!"
			else:
				self.ids.login_message.text = "sorry, that username and password do not match"
		else:
			self.store.put(name, password = password)


class StarterApp(App):
	def __init__(self,**kwargs):
		super(StarterApp, self).__init__(**kwargs)

		#JSONstore dictionaries are a way to save data so that it persists
		#between usages of your app. Each key is associated with one or more named
		#parameters. Our keys are the usernames, and each username has one associated
		#parameter, a password. All the data is stored in the associated .json file.
		#More documentation at https://kivy.org/docs/api-kivy.storage.html#module-kivy.storage
		self.store = JsonStore('starter.json')
	

	def build(self):
		#build just returns our parent widget, which contains 
		#all our sub-widgets and behavior
		return parent()

if __name__ == '__main__':
	StarterApp().run()