import os
import time

from config import DOGA_LOGS


class LogGenerator:

    def __init__(self):
        self.log_file_path = None
        self.log_file = None

        self.connect_log_file()

    def connect_log_file(self):
        """ set instance variable for Doga log file
        """

        home_dir = os.path.expanduser('~')

        self.log_file_path = os.path.join(home_dir, DOGA_LOGS)
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

    def generate(self, method, host, path, useragent):
        """ write log string for each request

        param: method(str) : request method type
        param: host(str) : host requested
        param: path(str) : resource path
        param: useragent(str) : user-agent for requesting source
        """

        timestr = self.timestamp()
        log_str = "%s %s %s %s %s\n" % (timestr, method, host, path, useragent)

        self.write_log(log_str)

#lg = LogGenerator()
#lg.write_log("alpha beta\n")
