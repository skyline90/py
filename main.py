import arcade

import random
import time
# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 1400

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Моё окошко"


def merge_two_lists( a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]

    if j < len(b):
        c += b[j:]
    print(c)
    return c


def merge_sort( s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    print(left)
    right = merge_sort(s[middle:])
    print(right)
    return merge_two_lists(left, right)


class Rectangle(arcade.Sprite):
    def update(self):
        game.on_draw()


class Text:
    pass

class OurGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.rectangles = arcade.SpriteList()
        self.text = Text()


    # начальные значения
    def setup(self):

        self.rand_numbers = []
        self.text.center_x = []
        self.text.center_y = []
        self.text.change_x = 0
        self.sound = arcade.load_sound("sound.wav")
        self.play_sound = True

        for j in range(20):
            self.rand_numbers.append(random.randint(1, 30))

        self.sort_arr = merge_sort(self.rand_numbers)
    # отрисовка объектов
    def on_draw(self):
        for i in range(20):
            self.margin = 30
            self.position = 400
            rectange = Rectangle("square.png", 0.1)
            rectange.center_x = self.margin * i + self.position
            self.text.center_x.append(rectange.center_x-6)
            rectange.center_y = 540
            self.text.center_y.append(rectange.center_y-4)
            self.rectangles.append(rectange)

        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.rectangles.draw()
        for i in range(20):
            arcade.draw_text(f"{self.rand_numbers[i]}",self.text.center_x[i], self.text.center_y[i], arcade.color.BLACK, 10 )


        for i in range(20):
            arcade.draw_text(f"{self.sort_arr[i]}",self.text.center_x[i], self.text.center_y[i]-60, arcade.color.BLACK, 10 )

        if self.play_sound == True:
            arcade.play_sound(self.sound)
            self.play_sound = False

    # логика
    def update(self, delta_time):
        pass


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
