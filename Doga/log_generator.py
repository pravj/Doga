# -*- coding: utf-8 -*-

import os
import time

from statistics import Statistics
from configer import value


class LogGenerator:

    def __init__(self):
        self.statistics = Statistics()

        self.log_file_path = None
        self.log_file = None

        self.connect_log_file()

    def connect_log_file(self):
        """ set instance variable for Doga log file
        """

        home_dir = os.path.expanduser('~')

        self.log_file_path = os.path.join(home_dir, value('logfile'))
        self.log_file = os.path.abspath(self.log_file_path)

    def timestamp(self):
        """ return current timestamp in particular format to be used in logs
        """
        return time.strftime("%d/%b/%Y:%H:%M:%S %z")

    def write_log(self, log_string):
        """ Write log string to log file

        param: log_string(str): formatted log string
        """

        with open(self.log_file, 'a+') as f:
            f.write(log_string)
            f.close()

    def generate(self, method, path, http_type, host, useragent, section):
        """ write log string for each request

        param: method(str) : request method type
        param: path(str) : resource path
        param: http_type(str) : HTTP type (1.1/1.0)
        param: host(str) : host requested
        param: useragent(str) : user-agent for requesting source
        param: section(str) : section for request's resource path
        """

        timestr = self.timestamp()
        log_str = "%s [%s] \"%s %s %s\" \"%s\"\n" % (host, timestr, method, path, http_type, useragent)

        self.write_log(log_str)

        self.statistics.queue_event(method, host, section)
