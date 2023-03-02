from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
  #  pass
   # """
      
  def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation= "vertical"
        #-----------------Button----------
        b1=Button(text=  "Button 1")
        b1.size= 400, 200
        b1.pos=0,400
        b2=Button(text=  "Button 2")
        #-----------------Label----------
        l1=Label(text=  "Hello World!")
        l1.size= 400, 200
        l1.pos=0,400
        l1.color= 0,1,0 ,100
        #-----------------Add To Layout----------
        self.add_widget(b1)
        self.add_widget(l1)
        self.add_widget(b2)
        

   # """
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass 

TheLabApp().run()