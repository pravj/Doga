# -*- coding: utf-8 -*-

"""
Doga.config.configer

This module gives other modules access to use configuration values
"""

import os
from ConfigParser import ConfigParser

# configuration file path
config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config_file = os.path.abspath(config_file_path)

# read config data using ConfigParser module
parser = ConfigParser()
parser.read(config_file)


def value(key):
    """ return config value for key

    param: key(str) : config data key
    return: config value for the requested key(str)
    """

    return parser.get('Doga', key)


def update(key, value):
    """ update option(key) with (value) in config section

    param: key(str) : config data key
    param: value(str) : config data value for option 'key'
    """

    parser.set('Doga', key, value)

    config = open(config_file, 'w')
    parser.write(config)
    config.close()
