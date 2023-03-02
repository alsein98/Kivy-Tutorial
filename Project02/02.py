import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from plyer import bluetooth


class BluetoothScanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create switch widget to turn on/off Bluetooth scanning
        self.switch = Switch(active=False)
        self.switch.bind(active=self.on_switch)

        # Create label to display status of Bluetooth scanning
        self.status_label = Label(text="Bluetooth scanning is off")

        # Add switch and label widgets to layout
        self.add_widget(self.switch)
        self.add_widget(self.status_label)

        # Create box layout to hold Bluetooth device buttons
        self.devices_layout = BoxLayout(orientation="vertical")
        self.add_widget(self.devices_layout)

    def on_switch(self, instance, value):
        if value:
            # Turn Bluetooth on
            bluetooth.enable()

            # Scan for available Bluetooth devices
            devices = bluetooth.discover_devices()

            # Clear previous device buttons from layout
            self.devices_layout.clear_widgets()

            if devices:
                self.status_label.text = f"Found {len(devices)} Bluetooth device(s):"
                # Create a button for each available device and add it to layout
                for device in devices:
                    device_button = Button(text=device[1])
                    self.devices_layout.add_widget(device_button)
            else:
                self.status_label.text = "No Bluetooth devices found"
        else:
            # Turn Bluetooth off
            bluetooth.disable()
            # Clear previous device buttons from layout
            self.devices_layout.clear_widgets()
            self.status_label.text = "Bluetooth scanning is off"


class BluetoothScannerApp(App):
    def build(self):
        return BluetoothScanner()


if __name__ == "__main__":
    BluetoothScannerApp().run()
