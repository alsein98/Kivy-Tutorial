import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class HelloWorldApp(App):
    def build(self):
        # create 5 BoxLayouts
        layout1 = BoxLayout(orientation='horizontal')
        layout2 = BoxLayout(orientation='horizontal')
        layout3 = BoxLayout(orientation='horizontal')
        layout4 = BoxLayout(orientation='horizontal')
        layout5 = BoxLayout(orientation='horizontal')
        
        # create buttons with 'Hello World' text
        button1 = Button(text='Hello World')
        button2 = Button(text='Hello World')
        button3 = Button(text='Hello World')
        button4 = Button(text='Hello World')
        button5 = Button(text='Hello World')
        
        # add buttons to corresponding layouts
        layout1.add_widget(button1)
        layout2.add_widget(button2)
        layout3.add_widget(button3)
        layout4.add_widget(button4)
        layout5.add_widget(button5)
        
        # add layouts to root BoxLayout
        root_layout = BoxLayout(orientation='vertical')
        root_layout.add_widget(layout1)
        root_layout.add_widget(layout2)
        root_layout.add_widget(layout3)
        root_layout.add_widget(layout4)
        root_layout.add_widget(layout5)
        
        return root_layout


if __name__ == '__main__':
    HelloWorldApp().run()
