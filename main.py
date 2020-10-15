from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
import kivy
from kivy.uix.spinner import Spinner

""""""""
kivy.require('1.8.0')

sm = ScreenManager()

food_list = []


class Food_choice(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=2)
        spinner = Spinner(
            # default value shown
            text='Home',
            # available values
            values=('Home', 'Work', 'Other', 'Custom'),
            size_hint=(None, None),
            size=(400, 200))
        spinner2 = Spinner(
            # default value shown
            text='Мясо',
            # available values
            values=('мясо1', 'мясо2', 'мясо3', 'мясо4'),
            size_hint=(None, None),
            size=(400, 200))

        but = Button(text="Потвердить", on_press=self.to_main_window)
        spinner.bind(text=self.show_selected_value)
        spinner2.bind(text=self.show_selected_value)

        layout.add_widget(spinner)
        layout.add_widget(spinner2)
        layout.add_widget(but)
        self.add_widget(layout)
        sm.add_widget(self)

    def show_selected_value(self, spinner, text):
        print(food_list.append(text))

    def to_main_window(self, *args):
        sm.switch_to(MainWindow(name='main'))


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=3)

        but = Button(text="Выбрать продукты", on_press=self.printer)

        self.add_widget(but)
        sm.add_widget(self)

    def printer(self, *args):
        sm.switch_to(Food_choice(name="food"))


class LoginScreen(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scr1 = Screen(name="None")

        self.layout = GridLayout(cols=3)
        self.layout.add_widget(Label(text=''))
        self.layout.add_widget(Label(text='Мужской'))
        self.layout.add_widget(Label(text='Женский'))
        self.layout.add_widget(Label(text='Пол'))

        self.check_box_male = CheckBox(active=False)
        self.check_box_male.bind(active=self.check)
        self.layout.add_widget(self.check_box_male)

        self.check_box_female = CheckBox(active=False)
        self.check_box_female.bind(active=self.check)
        self.layout.add_widget(self.check_box_female)

        self.layout.add_widget(Label(text='Имя'))
        self.username = TextInput(multiline=False)
        self.layout.add_widget(self.username)
        self.layout.add_widget(Label(text=''))

        self.but = Button(text="sumbit", on_press=self.redirect)
        self.layout.add_widget(self.but)

        self.scr1.add_widget(self.layout)
        sm.add_widget(self.scr1)

    def redirect(self, *args):
        sm.switch_to(MainWindow(name='main'))

    def check(self, checkboxInstance, isActive):
        if isActive:
            print("Checkbox Checked")
        else:
            print("Checkbox unchecked")


class MyApp(App):

    def build(self):
        login = LoginScreen()
        main = MainWindow()
        print(sm.screen_names)

        return sm


if __name__ == '__main__':
    MyApp().run()
print(food_list)
