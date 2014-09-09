# -*- coding: utf-8 -*-

"""
Doga.log_generator

This module manage Doga log generation and writing log to log file.
"""

import os
import time

from configer import value


class LogGenerator:

    def __init__(self, statistics):
        self.statistics = statistics

        self.log_file_path = None
        self.log_file = None

        self.connect_log_file()

    def connect_log_file(self):
        """ manage instance variable for Doga log file path
        """

        home_dir = os.path.expanduser('~')

        self.log_file_path = os.path.join(home_dir, value('logfile'))
        self.log_file = os.path.abspath(self.log_file_path)

    def timestamp(self):
        """ return current timestamp(str) in special format to be used in logs
        """

        return time.strftime("%d/%b/%Y:%H:%M:%S %z")

    def write_log(self, log_string):
        """ write log strings to log file

        param: log_string(str): formatted log string
        """

        with open(self.log_file, 'a+') as f:
            f.write(log_string)
            f.close()

    def generate(self, method, path, http_type, host, useragent, section):
        """ generate formatted log string for each request

        param: method(str) : request method type
        param: path(str) : resource path
        param: http_type(str) : HTTP type (1.1/1.0)
        param: host(str) : host requested
        param: useragent(str) : user-agent for requesting source
        param: section(str) : section for request's resource path
        """

        timestr = self.timestamp()
        log_str = "%s [%s] \"%s %s %s\" \"%s\"\n" % (
            host, timestr, method, path, http_type, useragent)

        self.statistics.queue_event(method, host, section)
        self.write_log(log_str)
