from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

import os
os.environ['KIVY_GL_BACKEND'] = 'gl'

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CustomLayout(BoxLayout):
    pass

class MainActivityApp(App):
    def build(self):
        return CustomLayout()

MainActivityApp().run()
