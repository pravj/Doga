# -*- coding: utf-8 -*-

"""
Doga.gui

This module manages Doga GUI and keep it updated in realtime.
"""

import npyscreen


class WindowForm(npyscreen.ActionForm):
    def create(self, *args, **keywords):
        super(WindowForm, self).create(*args, **keywords)
    
    def while_waiting(self):
        pass
        
        
class DogaGUI(npyscreen.NPSApp):

    def __init__(self, statistics):
        self.window = None

        self.alert_status = None
        self.doga_status = None
        self.doga_logs = None
        self.alert_history = None

        self.template = statistics.template

    def while_waiting(self):
        self.alert_status.value = "%s" % self.template('alert')
        self.doga_status.value = "%s" % self.template('stats')
        self.alert_status.display()
        self.doga_status.display()
        
    def main(self):
        self.keypress_timeout_default = 10

        self.window = WindowForm(parentApp=self, name="Doga : HTTP Log Monitor",)
        
        self.alert_status = self.window.add(npyscreen.TitleText, name="Alert Status", max_height=3)
        self.alert_status.value = ""
        self.alert_status.editable = False

        self.doga_status = self.window.add(npyscreen.TitleText, name="Doga Status", max_height=3, rely=4)
        self.doga_status.value = ""
        self.doga_status.editable = False

        self.doga_logs = self.window.add(npyscreen.BoxTitle, name="Doga Logs", max_width=50, relx=2, rely=7)
        self.doga_logs.entry_widget.scroll_exit = True
        self.doga_logs.values = []

        self.alert_history = self.window.add(npyscreen.BoxTitle, name="Alert History", max_width=50, relx=52, rely=7)
        self.alert_history.entry_widget.scroll_exit = True
        self.alert_history.values = []

        self.window.edit()
