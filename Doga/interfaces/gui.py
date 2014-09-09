# -*- coding: utf-8 -*-

"""
Doga.interfaces.gui

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
        # npyscreen form widget, parent of all widgets in GUI
        self.window = None

        # different data values to show in GUI
        self.alert_status = None
        self.doga_status = None
        self.doga_logs = None
        self.alert_history = None

        # reference to Statistics module functions that return data values
        self.template = statistics.template
        self.value = statistics.value

    def while_waiting(self):
        """ defines the default actions to be performed while waiting for user
        here this function updates widget data values periodically
        """

        # updating data values for all section
        self.alert_status.value = "%s" % self.template('alert')
        self.doga_status.value = "%s" % self.template('stats')
        self.doga_logs.values = self.value('logs')
        self.alert_history.values = self.value('history')

        # reverse lists to show them like recently updated(latest first)
        self.doga_logs.values = self.doga_logs.values[::-1]
        self.alert_history.values = self.alert_history.values[::-1]

        # display updated values in widgets, call 'Widget.display()' method
        self.alert_status.display()
        self.doga_status.display()
        self.doga_logs.display()
        self.alert_history.display()
        
    def main(self):
        """ 'main' function of npyscreen.NPSApp application object
        this function help in initial widget setup and rendering
        """

        # time(ms) to wait for user interactions
        self.keypress_timeout_default = 10

        # Form widget instance
        self.window = WindowForm(parentApp=self, name="Doga : HTTP Log Monitor",)
        
        # setup a section for Alert status
        self.alert_status = self.window.add(npyscreen.TitleText, name="Alert Status", max_height=3)
        self.alert_status.value = ""
        self.alert_status.editable = False

        # setup a section for Doga status
        self.doga_status = self.window.add(npyscreen.TitleText, name="Doga Status", max_height=3, rely=4)
        self.doga_status.value = ""
        self.doga_status.editable = False

        # setup a section for Doga logs
        self.doga_logs = self.window.add(npyscreen.BoxTitle, name="Doga Logs", max_width=50, relx=2, rely=7)
        self.doga_logs.entry_widget.scroll_exit = True
        self.doga_logs.values = []

        # setup a section for Alert history
        self.alert_history = self.window.add(npyscreen.BoxTitle, name="Alert History", max_width=50, relx=52, rely=7)
        self.alert_history.entry_widget.scroll_exit = True
        self.alert_history.values = []

        # update parent widget by embedding sub-widgets
        self.window.edit()
