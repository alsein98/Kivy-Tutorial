from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        # Create a label with text, text size, and alignment
        label = Label(text='Hello, World!', text_size=(300, 100), halign='right')
        return label

if __name__ == '__main__':
    MyLabelApp().run()
