# -*- coding: utf-8 -*-

"""
Doga.statistics

This module manage information about log statistics
Shows data summary periodically in each 10 seconds
"""

import time
import threading

from thread_timer import ThreadTimer


#class ThreadTimer(threading.Thread):
#
#    def __init__(self, event, callback):
#        threading.Thread.__init__(self)
#        self.stopped = event
#
#        self.callback = callback
#
#    def run(self):
#        while not self.stopped.wait(10):
#            self.callback()


class Statistics():

    def __init__(self):
        self.queue = []
        self.total_count = 0

        stop_event = threading.Event()
        thread_timer = ThreadTimer(10, stop_event, self.update_queue)
        thread_timer.start()

    def queue_event(self, method, host, section):
        """ Queue each request to be used in statistics
        """

        self.queue.append(host + section)

    def update_queue(self):
        print len(self.queue)
        self.queue = []
