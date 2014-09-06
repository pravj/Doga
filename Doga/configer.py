# -*- coding: utf-8 -*-

"""
Doga.configer

This module give other modules access to use configuration values
"""

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

def value(key):
    return parser.get('Doga', key)
