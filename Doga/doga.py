# -*- coding: utf-8 -*-

import argparse
import sys

from statistics import Statistics
from interfaces.gui import DogaGUI
from thread_jobs import Job
from logs.generator import LogGenerator
from parsers.payload import PayloadParser
from parsers.packet import PacketParser
from interfaces.sockets import SocketInterface


def main():
    desc = 'HTTP log monitoring console for Humans'
    parser = argparse.ArgumentParser(description=desc)

    # argument for optional custom log file
    parser.add_argument(
        '-f', dest='file', type=str, default=None, help='custom log file')

    # dictionary object with all supplied arguments
    args = vars(parser.parse_args())

    # Statistics class instance
    statistics = Statistics()

    # run npyscreen.NPSApp using separate thread
    app = DogaGUI(statistics)
    Job(app).start()

    # LogGenerator class instance
    # optional logfile is given
    if (args['file']):
        generator = LogGenerator(statistics, args['file'])
    # log to default logfile
    else:
        generator = LogGenerator(statistics)

    # PayloadParser class instance
    payload_parser = PayloadParser(generator)

    # PacketParser class instance
    packet_parser = PacketParser(payload_parser)

    # SocketInterface class interface
    socket_interface = SocketInterface(packet_parser)
