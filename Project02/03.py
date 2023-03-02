import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import speech_recognition as sr

class VoiceRecognitionApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Start real-time voice recognition by clicking the button.")
        button = Button(text='Start Voice Recognition', size_hint=(1, 0.2))
        button.bind(on_press=self.start_recognition)
        layout.add_widget(button)
        layout.add_widget(self.label)
        return layout

    def start_recognition(self, button):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            self.label.text = "Speak now!"
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            self.label.text = f"You said: {text}"
        except sr.UnknownValueError:
            self.label.text = "Sorry, I could not understand what you said."
        except sr.RequestError as e:
            self.label.text = f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == '__main__':
    VoiceRecognitionApp().run()
