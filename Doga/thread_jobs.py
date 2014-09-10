# -*- coding: utf-8 -*-

"""
Doga.thread_jobs

This module works as 'TimeInterval' function and invoke callback functions
also run npyscreen.NPSApp as a separate thread using 'Job' class
"""

import threading


class Job(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)

        self.app = app

    def run(self):
        self.app.run()


class Timer(threading.Thread):

    def __init__(self, interval, event, callback):
        threading.Thread.__init__(self)
        self.stopped = event

        self.interval = interval
        self.callback = callback

    def run(self):
        while not self.stopped.wait(self.interval):
            self.callback()
