import socket
import struct

from payload_parser import PayloadParser

ETH_LENGTH = 14


class PacketParser:

    def __init__(self, ip):
        self.ip = ip
        self.payload_parser = PayloadParser()

    def parse_ip_header(self, packet_string):
        """ Parse required info from packret according IP Header structure
        Reference : Wikipedia (http://en.wikipedia.org/wiki/IPv4#Header)
        """

        iph = packet_string[ETH_LENGTH:20+ETH_LENGTH]
        unpacked_iph = struct.unpack('!BBHHHBBH4s4s', iph)

        iph_first_byte = unpacked_iph[0]
        version = iph_first_byte >> 4
        ihl = iph_first_byte & 0xF
        iph_length = ihl * 4

        packet_protocol = unpacked_iph[6]

        source_addr = socket.inet_ntoa(unpacked_iph[8])
        dest_addr = socket.inet_ntoa(unpacked_iph[9])

        return (iph_length, packet_protocol, [source_addr, dest_addr])

    def parse_tcp_header(self, packet_string, iph_length):
        """ Parse required info from packet according TCP Header structure
        Reference : Wikipedia (http://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)
        """

        shift = iph_length + ETH_LENGTH

        tcph = packet_string[shift:shift+20]
        unpacked_tcph = struct.unpack('!HHLLBBHHH', tcph)

        source_port = unpacked_tcph[0]
        dest_port = unpacked_tcph[1]

        data_offset = unpacked_tcph[4]
        tcph_length = (data_offset >> 4) * 4

        header_size = ETH_LENGTH + iph_length + tcph_length

        data_size = len(packet_string) - header_size
        data = packet_string[header_size:]

        return (data, [source_port, dest_port])

    def verify_packet_data(self, addr, ports):
        """ Verify the packet to filter HTTP packets

        param: addr (list object) : source and destination connection addresses
        param: ports (list object) : source and destination connection ports
        """

        return True if 80 in ports and self.ip == addr[0] else False

    def parse(self, packet_string):
        """ Parse required info from packet according Ethernet Header structure
        Reference : Wikipedia (http://en.wikipedia.org/wiki/Ethernet_frame#Structure)

        param: packet_string (str object) : packet string from packet tuple object
        """

        eth_h = packet_string[:ETH_LENGTH]
        unpacked_eth_h = struct.unpack('!6s6sH', eth_h)

        eth_protocol = socket.ntohs(unpacked_eth_h[2])

        if (eth_protocol == 8):
            iph_len, packet_protocol, addr = self.parse_ip_header(packet_string)

            if (packet_protocol == 6):
                data, ports = self.parse_tcp_header(packet_string, iph_len)

                if (len(data) != 0):

                    if self.verify_packet_data(addr, ports):
                        self.payload_parser.parse(data, addr, ports)
