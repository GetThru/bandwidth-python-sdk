# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ModeEnum(object):

    """Implementation of the 'Mode' enum.

    The machine detection mode. If set to 'async', the detection result will
    be sent in a 'machineDetectionComplete' callback. If set to 'sync', the
    'answer' callback will wait for the machine detection to complete and will
    include its result. Default is 'async'.

    Attributes:
        SYNC: TODO: type description here.
        ASYNC: TODO: type description here.

    """

    SYNC = 'sync'

    ASYNC = 'async'
