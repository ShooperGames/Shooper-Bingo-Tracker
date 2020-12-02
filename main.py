import kivy

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

#Main
class BingoMain(FloatLayout):
    def __init__(self, **kwargs):
        super(BingoMain, self).__init__(**kwargs)
        #self.add_widget(BingoMenu())
        gameB = GameBoard()
        gameB.size_hint_y = 0.9
        gameB.pos_hint = {'x':0, 'y':.1}
        gameB.add_widget(Label(text="B"))
        gameB.add_widget(Label(text="I"))
        gameB.add_widget(Label(text="N"))
        gameB.add_widget(Label(text="G"))
        gameB.add_widget(Label(text="O"))
        cBut = ClearBut(text="Clear")
        cBut.size_hint_y = 0.1
        for i in range(1,16):
            for j in range(5):
                gameB.add_widget(NumBut(text=str(i+(j*15))))
        self.add_widget(gameB)
        self.add_widget(cBut)

#UIs
class GameBoard(GridLayout):
    pass

class ClearBut(Button):
    always_release = False
    min_state_time = 0.1
    def on_release(self):
        hRoot = self.parent
        hRoot.clear_widgets()
        gameB = GameBoard()
        gameB.size_hint_y = 0.9
        gameB.pos_hint = {'x':0, 'y':.1}
        gameB.add_widget(Label(text="B"))
        gameB.add_widget(Label(text="I"))
        gameB.add_widget(Label(text="N"))
        gameB.add_widget(Label(text="G"))
        gameB.add_widget(Label(text="O"))
        cBut = ClearBut(text="Clear")
        cBut.size_hint_y = 0.1
        for i in range(1,16):
            for j in range(5):
                gameB.add_widget(NumBut(text=str(i+(j*15))))
        hRoot.add_widget(gameB)
        hRoot.add_widget(cBut)

class NumBut(Button):
    always_release = False
    min_state_time = 0.1
    background_normal = ""

    def __init__(self, **kwargs):
        super(NumBut, self).__init__(**kwargs)
        self.background_color = [0,0,0,1]
        self.selected = False

    def on_release(self):
        self.selected = not self.selected
        if self.selected:
            self.background_color = [0,0,0.5,1]
        else:
            self.background_color = [0,0,0,1]

#App
class BingoApp(App):
    def build(self):
        return BingoMain()

#Main
if __name__ == '__main__':
    BingoApp().run()
