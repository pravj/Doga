# -*- coding: utf-8 -*-

"""
Doga.configer

This module gives other modules access to use configuration values
"""

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')


def value(key):
    """ return config value for key

    param: key(str) : config data key
    """

    return parser.get('Doga', key)
