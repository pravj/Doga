#!/usr/bin/env python
import npyscreen


class WindowForm(npyscreen.ActionForm):
    def create(self, *args, **keywords):
        super(WindowForm, self).create(*args, **keywords)
    
    def while_waiting(self):
        pass
        
        
class DogaGUI(npyscreen.NPSApp):

    def __init__(self):
        self.window = None

        self.alert_status = None
        self.doga_status = None
        self.doga_logs = None
        self.alert_history = None

    def while_waiting(self):
        self.doga_status.value = "This is another sample status"
        self.doga_status.display()
        
    def main(self):
        self.keypress_timeout_default = 10

        self.window = WindowForm(parentApp=self, name="Doga : HTTP Log Monitor",)
        
        self.alert_status = self.window.add(npyscreen.TitleText, name="Alert Status", max_height=3)
        self.alert_status.value = "High Traffic Alert : Hits 324, triggered at 23:03:23"
        self.alert_status.editable = False

        self.doga_status = self.window.add(npyscreen.TitleText, name="Doga Status", max_height=3, rely=4)
        self.doga_status.value = "This is sample Doga usage status"
        self.doga_status.editable = False

        self.doga_logs = self.window.add(npyscreen.BoxTitle, name="Doga Logs", max_width=50, relx=2, rely=7)
        self.doga_logs.entry_widget.scroll_exit = True
        self.doga_logs.values = ["GET httpbin.org/ip"]

        self.alert_history = self.window.add(npyscreen.BoxTitle, name="Alert History", max_width=50, relx=52, rely=7)
        self.alert_history.entry_widget.scroll_exit = True
        self.alert_history.values = ["Alert 1"]

        self.window.edit()


if __name__ == "__main__":
    app = DogaGUI()
    app.run()
