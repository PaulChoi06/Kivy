import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class InputApp(App):
    def build(self):
        return InputGrid()

class InputGrid(Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    food = ObjectProperty(None)

    def pressed(self):
        name = self.name.text
        age = self.age.text
        food = self.food.text

        print(f'Hi {name}, I see you are {age} years old and like to eat{food}.')

        self.name.text = ''
        self.age.text = ''
        self.food.text = ''

if __name__ == '__main__':
    InputApp().run()
