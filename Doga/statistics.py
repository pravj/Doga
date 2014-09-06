# -*- coding: utf-8 -*-

"""
Doga.statistics

This module manage information about log statistics
Shows data summary periodically in each 10 seconds
"""

import threading
from collections import Counter

from thread_timer import ThreadTimer


class Statistics():

    def __init__(self):
        self.queue = []
        self.total = 0

        self.stop_event = threading.Event()

        self.stats_timer = ThreadTimer(10, self.stop_event, self.update_queue)
        self.stats_timer.start()

    def queue_event(self, method, host, section):
        """ Queue each request to be used in statistics

        param: method(str) : request method type
        param: host(str) : requested resource host
        param: section(str) : requested resource section
        """

        self.queue.append(host + section)

    def max_queue(self):
        """ return resource section info having maximum hits and count of total hits
        """

        if (len(self.queue) > 0):
            frequency = Counter(self.queue)
            print frequency.most_common()[0][0], frequency.most_common()[0][1]
        else:
            print "No requests"
        print len(self.queue)
        self.total += len(self.queue)
        print self.total

    def update_queue(self):
        """ update the queue periodically and call for 'max_queue' method
        """

        self.max_queue()
        self.queue = []
