from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

class FirstScreen(Screen):
    def __init__(self,title):
        super().__init__(name = title)
        self.title = title
        layout = BoxLayout()
        label = Label(text="Привіт це тест руфє сподіваюсь тобі сподобається")
        button1 = Button(text="наступний екран", size=(200,200))
        button1.on_press = self.change_screen
        layout.add_widget(label)
        layout.add_widget(button1)
        self.add_widget(layout)

    def change_screen(self):
        self.manager.transition.direction = "left"
        self.manager.current = "Second"


    


class SecondScreen(Screen):
    def __init__(self,title):
        super().__init__(name = title)
        self.title = title
        layout = BoxLayout()
        label1 = Label(text="Як вас звати?")
        button1 = Button(text="Наступний екран")
        self.textinput = TextInput(text='')
        button1.on_press = self.change_screen
        layout.add_widget(label1)
        layout.add_widget(self.textinput)
        layout.add_widget(button1)
        self.add_widget(layout)




    def change_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Third"
        name = self.textinput.text
        print(name)

class ThirdScreen(Screen):
    def __init__(self,title):
        super().__init__(name = title)
        self.title = title
        layout = BoxLayout()
        label = Label(text="Скільки вам років?")
        button1 = Button(text="Наступний екран")
        self.textinput = TextInput(text='0')
        button1.on_press = self.change_screen
        layout.add_widget(label)
        layout.add_widget(self.textinput)
        layout.add_widget(button1)
        self.add_widget(layout)




    def change_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Fourth"
        age = self.textinput.text
        print(age)
        
        
class FourthScreen(Screen):
    def __init__(self,title):
        super().__init__(name = title)
        self.title = title
        layout = BoxLayout()
        label = Label(text="Введіть перший результат пульсу")
        button1 = Button(text="Наступний екран")
        button1.on_press = self.change_screen
        layout.add_widget(label)
        layout.add_widget(button1)
        self.add_widget(layout)




    def change_screen(self):
        self.manager.transition.direction = "left"
        self.manager.current = "Fourth"

class FifthScreen(Screen):
    def __init__(self,title):
        super().__init__(name = title)
        self.title = title
        layout = BoxLayout()
        label = Label(text="Ви на чертвертому екрані")
        button1 = Button(text="Головний екран")
        button1.on_press = self.change_screen
        layout.add_widget(label)
        layout.add_widget(button1)
        self.add_widget(layout)




    def change_screen(self):
        self.manager.transition.direction = "left"
        self.manager.current = "Fifth"



class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(FirstScreen("First"))
        screen_manager.add_widget(SecondScreen("Second"))
        screen_manager.add_widget(ThirdScreen("Third"))
        screen_manager.add_widget(FourthScreen("Fourth"))
        screen_manager.add_widget(FifthScreen("Fifth"))
        return screen_manager



app = MyApp()
app.run()