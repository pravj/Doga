import re


class PayloadParser:

    def __init__(self):
        self.pattern = re.compile(r"(GET|HEAD|POST|PUT|DELETE|TRACE|OPTIONS|CONNECT|PATCH)\s(\/.*)\s(HTTP\/.*)\nHost:\s(.*)")

    def parse(self, data, addr, ports):
        #print data
        result = (self.pattern).match(data)
        print result.group(1), result.group(2), result.group(3), result.group(4)
