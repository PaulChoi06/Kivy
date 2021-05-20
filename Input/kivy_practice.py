from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
'''Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '750')'''


class MenuWindow(Screen):
    pass

class GameWindow(Screen):

    state = OptionProperty('normal', options=('normal', 'down'))

    def __init__(self, **kwargs):
        super(GameWindow, self).__init__(**kwargs)

        self.left_btn = Button(text='LEFT',size=(350, 750),size_hint=(None,None))
        self.left_btn.bind(on_press=self.left, on_release=self.reset)
        self.add_widget(self.left_btn)

        self.right_btn = Button(text='RIGHT',size=(350, 750),size_hint=(None,None),pos=(350,0))
        self.right_btn.bind(on_press=self.right, on_release=self.reset)
        self.add_widget(self.right_btn)

        with self.canvas:
            self.bg = Rectangle(source='bg1.png', pos=(-400,-500), size=(1524, 1415))
            self.car = Rectangle(source='car.png', pos=(325, -50), size=(90,200))


    moving_right = 'false'
    moving_left = 'false'

    def start(self):
        bg_x = self.bg.pos[0]
        bg_y = self.bg.pos[1]

        bg_y += 5

        self.bg.pos = (bg_x,bg_y)

    def reset(self, instance):
        global moving_right, moving_left

        moving_left = 'false'
        moving_right = 'false'

        if moving_left == 'false' and moving_right == 'false':
            #print('left: ', moving_left, '\nright: ', moving_right, '\n')
            self.car.source = 'car.png'
            self.car.size = (90,200)
            self.car.pos = (325, -50)

    def left(self, instance):
        global moving_left

        moving_left = 'true'

        bg_x = self.bg.pos[0]
        bg_y = self.bg.pos[1]

        print('left: ', moving_left, '\n\n', '(', bg_x, ',', bg_y, ')')

        self.car.source = 'car_L2.png'
        self.car.size = (175,230)
        self.car.pos = (250, -75)
        bg_x += 5
        bg_y -= 5

        if bg_x >= -300:
            bg_x = -300
            self.car.source = 'car.png'
            self.car.size = (90,200)
            self.car.pos = (325, -50)

        self.bg.pos = (bg_x,bg_y)

    def move(self):
        bg_x = self.bg.pos[0]
        bg_y = self.bg.pos[1]

        self.car.source = 'car.png'
        self.car.size = (90,200)
        self.car.pos = (325, -50)
        bg_y -= 5

        self.bg.pos = (bg_x,bg_y)

    def right(self, instance):
        global moving_right

        moving_right = 'true'

        bg_x = self.bg.pos[0]
        bg_y = self.bg.pos[1]

        print('right: ', moving_right, '\n\n', '(', bg_x, ',', bg_y, ')')
        self.car.source = 'car_R2.png'
        self.car.size = (175,230)
        self.car.pos = (350, -75)
        bg_x -= 5
        bg_y -= 5

        if bg_x <= -500:
            bg_x = -500
            self.car.source = 'car.png'
            self.car.size = (90,200)
            self.car.pos = (325, -50)

        self.bg.pos = (bg_x,bg_y)

        

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('car.kv')

class CarApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    CarApp().run()