#!/usr/bin/env python

import argparse

from Doga.interfaces.gui import DogaGUI
from Doga.interfaces.sockets import SocketInterface
from Doga.parsers.packet import PacketParser
from Doga.parsers.payload import PayloadParser
from Doga.logs.generator import LogGenerator
from Doga.statistics import Statistics
from Doga.thread_timer import ThreadJob


class Doga:

    def __init__(self):
        self.desc = 'HTTP log monitoring console for Humans'
        self.parser = argparse.ArgumentParser(description=(self.desc))

        self.parser.add_argument(
            '-f', dest='file', type=str, default=None, help='custom log file')

        args = vars(self.parser.parse_args())

if __name__ == '__main__':
    statistics = Statistics()

    app = DogaGUI(statistics)
    ThreadJob(app).start()

    log_generator = LogGenerator(statistics)
    payload_parser = PayloadParser(log_generator)
    packet_parser = PacketParser(payload_parser)
    socket_interface = SocketInterface(packet_parser)
