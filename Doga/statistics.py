# -*- coding: utf-8 -*-

"""
Doga.statistics

This module manage information about log statistics
update and keep track of usage summary periodically
"""

import time
import threading
from collections import Counter

from .config.configer import value
from thread_timer import ThreadTimer


class Statistics:

    def __init__(self):
        # list object having all requests of a timespan
        self.queue = []
        # total number of requests so far
        self.total = 0

        # all requests of a timespan, to be used for alert status
        self.alert_queue = []

        self.stop_event = threading.Event()

        # callback update_queue method using thread
        self.stats_timer = ThreadTimer(10, self.stop_event, self.update_queue)
        self.stats_timer.start()

        # callback update_alert_queue method using thread
        self.alert_timer = ThreadTimer(
            10, self.stop_event, self.update_alert_queue)
        self.alert_timer.start()

        # callback check_stats method using thread
        self.stats_scanner = ThreadTimer(1, self.stop_event, self.check_stats)
        self.stats_scanner.start()

        # log data and alert history values
        self.doga_logs = []
        self.alert_history = []

        # alert and usage status templates
        self.stats_template = "Maximum: [No recent requests], Recent: 0, Total: 0"
        self.alert_template = "Traffic status: Normal, Alert state: No"

        # alert state
        self.is_alert = False

        # timestamps representing alert start and end time
        self.alert_start = ""
        self.alert_end = ""

    def template(self, type):
        """ return a template value

        param: type(str): type of the template (alert or stats)
        """

        if (type == 'alert'):
            return self.alert_template
        elif (type == 'stats'):
            return self.stats_template

    def value(self, type):
        """ return value of private data

        param: type(str): type of data to return
        """

        if (type == 'logs'):
            return self.doga_logs
        elif (type == 'history'):
            return self.alert_history

    def queue_event(self, method, host, section):
        """ queue each request to be used in statistics

        param: method(str) : request method type
        param: host(str) : requested resource host
        param: section(str) : requested resource section
        """

        self.queue.append(host + section)
        self.alert_queue.append(host + section)

        self.doga_logs.append("%s %s%s" % (method, host, section))

    def update_statistics(self):
        """ update usage stats template having maximum hits and count of total hits
        """

        self.total += len(self.queue)

        status = "[No recent requests]"
        if (len(self.queue) > 0):
            counts = Counter(self.queue)
            frequency = counts.most_common()

            status = "[%s : %d]" % (frequency[0][0], frequency[0][1])

        self.stats_template = "Maximum : %s, Recent : %d, Total : %d" % (
            status, len(self.queue), self.total)

    def update_queue(self):
        """ update the doga statistics and queue periodically
        """

        self.update_statistics()
        self.queue = []

    def update_alert_queue(self):
        """ update the alert queue periodically
        """

        self.alert_queue = []

    def check_stats(self):
        """ check for requests and update the alert status according to that 
        """

        maximum = int(value('maximum'))

        # we are in alert state
        if (self.is_alert):
            if (len(self.alert_queue) < maximum):
                self.is_alert = False
                self.alert_end = time.strftime("%H:%M:%S")
                status_string = "Max Hits: %d, Recovered at: %s" % (
                    len(self.alert_queue), self.alert_start)
                self.alert_template = "Traffic: Normal, Alert state: No, %s" % (
                    status_string)
                self.alert_history.append(self.alert_template)
        # we are alert free now
        else:
            if (len(self.alert_queue) > maximum):
                self.is_alert = True
                self.alert_start = time.strftime("%H:%M:%S")
                status_string = "Max Hits: %d, Triggered at: %s" % (
                    len(self.alert_queue), self.alert_start)
                self.alert_template = "Traffic: High, Alert state: Yes, %s" % (
                    status_string)
                self.alert_history.append(self.alert_template)
