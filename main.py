from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory

Builder.load_string("""
#:include kv/login.kv
#:import utils kivy.utils
""")

class Loaf(MDApp):
    def __init__(self, **kwargs):
        self.title = "Baye Ganar - Application de Gestion"
        self.theme_cls_theme_style = "Dark"
        self.theme_cls_primary_palette = "Blue"
        self.sm = ScreenManager()
        super().__init__( **kwargs)


    def build(self):
        self.sm.add_widget(Factory.LoginScreen())
        return self.sm

if __name__ == "__main__":
    Loaf().run()