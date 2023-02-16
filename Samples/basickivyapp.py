import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class SimpleApp(App):
    def build(self):
        layout = GridLayout(cols=1)

        self.label = Label(text="Click the button to display a message!")
        layout.add_widget(self.label)

        button = Button(text="Click me!")
        button.bind(on_press=self.display_message)
        layout.add_widget(button)

        return layout

    def display_message(self, event):
        self.label.text = "Hello, World!"

if __name__ == '__main__':
    SimpleApp().run()
