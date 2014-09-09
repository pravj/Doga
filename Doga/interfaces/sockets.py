# -*- coding: utf-8 -*-

"""
Doga.socket_interface

This module does some Socket related tasks for Doga.
"""

import sys
import socket
import struct

from ..config.configer import value


class SocketInterface:

    def __init__(self, packet_parser):
        self.ip = self.ipv4()
        self.raw_socket = None

        self.packet_parser = packet_parser

        self.create_raw_socket()
        self.capture(self.raw_socket)

    def ipv4(self):
        """ return local IP Address(str) of system(IPV4 type)

        though this method depends on availability of 'httpbin.org'
        """

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((value('httpbin'), 80))

        try:
            ipv4 = sock.getsockname()[0]
        except ValueError:
            sys.exit()

        sock.close()

        return ipv4

    def create_raw_socket(self):
        """ Create row socket(SOCK_RAW type) to listen for traffic
        """

        try:
            self.raw_socket = socket.socket(
                socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        except socket.error, msg:
            print "unable to create socket"
            print "Error Code %d : Message %s" % (msg[0], msg[1])
            sys.exit()

    def capture(self, sock):
        """ Capture packets in traffic

        param: sock(socket._socketobject): raw socket that listen for traffic
        """

        while True:
            # socket.recvfrom() method returns tuple object
            packet_tuple = sock.recvfrom(65565)
            packet_str = packet_tuple[0]

            self.packet_parser.parse(self.ip, packet_str)
