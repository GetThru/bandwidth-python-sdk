# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bandwidth.api_helper import APIHelper
from bandwidth.voice.models.machine_detection_configuration import MachineDetectionConfiguration


class CreateCallResponse(object):

    """Implementation of the 'CreateCallResponse' model.

    TODO: type model description here.

    Attributes:
        account_id (string): TODO: type description here.
        call_id (string): TODO: type description here.
        application_id (string): TODO: type description here.
        to (string): TODO: type description here.
        mfrom (string): TODO: type description here.
        start_time (datetime): TODO: type description here.
        enqueued_time (datetime): TODO
        call_url (string): TODO: type description here.
        call_timeout (float): TODO: type description here.
        callback_timeout (float): TODO: type description here.
        answer_url (string): TODO: type description here.
        answer_method (AnswerMethodEnum): TODO: type description here.
        answer_fallback_url (string): TODO: type description here.
        answer_fallback_method (AnswerFallbackMethodEnum): TODO: type
            description here.
        disconnect_url (string): TODO: type description here.
        disconnect_method (DisconnectMethodEnum): TODO: type description
            here.
        username (string): TODO: type description here.
        password (string): TODO: type description here.
        fallback_username (string): TODO: type description here.
        fallback_password (string): TODO: type description here.
        tag (string): TODO: type description here.
        priority (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "call_id": 'callId',
        "application_id": 'applicationId',
        "to": 'to',
        "mfrom": 'from',
        "call_url": 'callUrl',
        "answer_url": 'answerUrl',
        "answer_method": 'answerMethod',
        "disconnect_method": 'disconnectMethod',
        "start_time": 'startTime',
        "enqueued_time": 'enqueuedTime',
        "call_timeout": 'callTimeout',
        "callback_timeout": 'callbackTimeout',
        "answer_fallback_url": 'answerFallbackUrl',
        "answer_fallback_method": 'answerFallbackMethod',
        "disconnect_url": 'disconnectUrl',
        "username": 'username',
        "password": 'password',
        "fallback_username": 'fallbackUsername',
        "fallback_password": 'fallbackPassword',
        "tag": 'tag',
        "machine_detection": 'machineDetection',
        "priority": 'priority'
    }

    def __init__(self,
                 account_id=None,
                 call_id=None,
                 application_id=None,
                 to=None,
                 mfrom=None,
                 call_url=None,
                 answer_url=None,
                 answer_method=None,
                 disconnect_method=None,
                 start_time=None,
                 enqueued_time=None,
                 call_timeout=None,
                 callback_timeout=None,
                 answer_fallback_url=None,
                 answer_fallback_method=None,
                 disconnect_url=None,
                 username=None,
                 password=None,
                 fallback_username=None,
                 fallback_password=None,
                 tag=None,
                 priority=None):
        """Constructor for the CreateCallResponse class"""

        # Initialize members of the class
        self.account_id = account_id
        self.call_id = call_id
        self.application_id = application_id
        self.to = to
        self.mfrom = mfrom
        self.start_time = APIHelper.RFC3339DateTime(start_time) if start_time else None
        self.enqueued_time = APIHelper.RFC3339DateTime(enqueued_time) if enqueued_time else None,
        self.enqueued_time = enqueued_time
        self.call_url = call_url
        self.call_timeout = call_timeout
        self.callback_timeout = callback_timeout
        self.answer_url = answer_url
        self.answer_method = answer_method
        self.answer_fallback_url = answer_fallback_url
        self.answer_fallback_method = answer_fallback_method
        self.disconnect_url = disconnect_url
        self.disconnect_method = disconnect_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.priority = priority

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        account_id = dictionary.get('accountId')
        call_id = dictionary.get('callId')
        application_id = dictionary.get('applicationId')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        call_url = dictionary.get('callUrl')
        answer_url = dictionary.get('answerUrl')
        answer_method = dictionary.get('answerMethod')
        disconnect_method = dictionary.get('disconnectMethod')
        start_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("startTime")).datetime if dictionary.get("startTime") else None
        enqueued_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("enqueuedTime")).datetime if dictionary.get("enqueuedTime") else None
        call_timeout = dictionary.get('callTimeout')
        callback_timeout = dictionary.get('callbackTimeout')
        answer_fallback_url = dictionary.get('answerFallbackUrl')
        answer_fallback_method = dictionary.get('answerFallbackMethod')
        disconnect_url = dictionary.get('disconnectUrl')
        username = dictionary.get('username')
        password = dictionary.get('password')
        fallback_username = dictionary.get('fallbackUsername')
        fallback_password = dictionary.get('fallbackPassword')
        tag = dictionary.get('tag')
        priority = dictionary.get('priority')

        # Return an object of this model
        return cls(account_id,
                   call_id,
                   application_id,
                   to,
                   mfrom,
                   call_url,
                   answer_url,
                   answer_method,
                   disconnect_method,
                   start_time,
                   enqueued_time,
                   call_timeout,
                   callback_timeout,
                   answer_fallback_url,
                   answer_fallback_method,
                   disconnect_url,
                   username,
                   password,
                   fallback_username,
                   fallback_password,
                   tag,
                   priority)
