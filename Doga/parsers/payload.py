# -*- coding: utf-8 -*-

"""
Doga.parsers.payload

This module parse payload string and collect information from that.
info involves (method, host, resource path, section, http_type, useragent).
"""

import re
import sys


class PayloadParser:

    def __init__(self, log_generator):
        self.log_generator = log_generator

        self.method = '(GET|HEAD|POST|PUT|DELETE|TRACE|OPTIONS|CONNECT|PATCH)'
        self.path = '(\/.*)'
        self.http_type = '(HTTP\/1.[0-1])'

        self.req_regex = "%s\s%s\s%s" % (
            self.method, self.path, self.http_type)
        self.host_regex = "Host:\s(.*)\r"
        self.useragent_regex = "User-Agent:\s(.*)\r"

    def parse(self, data, ports):
        """ Parse request method, path, host, useragent, httptype etc.

        param: data(str) : packet payload string
        param: ports(list) : list object having source and destination ports
        """

        req_str = re.search(self.req_regex, data)
        host_str = re.search(self.host_regex, data)
        useragent_str = re.search(self.useragent_regex, data)

        try:
            method = req_str.group(1)
            path = req_str.group(2)
            http_type = req_str.group(3)
            host = host_str.group(1)
            useragent = useragent_str.group(1)
            section = path.split('?')[0]

            print data
            self.log_generator.generate(
                method, path, http_type, host, useragent, section)
        except:
            pass
