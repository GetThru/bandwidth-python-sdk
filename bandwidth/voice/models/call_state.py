# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bandwidth.api_helper import APIHelper


class CallState(object):

    """Implementation of the 'CallState' model.

    TODO: type model description here.

    Attributes:
        call_id (string): TODO: type description here.
        parent_call_id (string): TODO: type description here.
        application_id (string): TODO: type description here.
        account_id (string): TODO: type description here.
        to (string): TODO: type description here.
        mfrom (string): TODO: type description here.
        direction (string): TODO: type description here.
        state (string): The current state of the call. Current possible values
            are 'initiated', 'answered' and 'disconnected'. Additional states
            may be added in the future, so your application must be tolerant
            of unknown values.
        identity (string): TODO: type description here.
        stir_shaken (dict): TODO: type description here.
        start_time (datetime): TODO: type description here.
        answer_time (datetime): TODO: type description here.
        end_time (datetime): TODO: type description here.
        disconnect_cause (string): The reason the call was disconnected, or
            null if the call is still active. Current values are 'cancel',
            'timeout', 'busy', 'rejected', 'hangup', 'invalid-bxml',
            'callback-error', 'application-error', 'error', 'account-limit',
            'node-capacity-exceeded' and 'unknown'. Additional causes may be
            added in the future, so your application must be tolerant of
            unknown values.
        error_message (string): TODO: type description here.
        error_id (string): TODO: type description here.
        last_update (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "call_id": 'callId',
        "parent_call_id": 'parentCallId',
        "application_id": 'applicationId',
        "account_id": 'accountId',
        "to": 'to',
        "mfrom": 'from',
        "direction": 'direction',
        "state": 'state',
        "identity": 'identity',
        "stir_shaken": 'stirShaken',
        "start_time": 'startTime',
        "enqueued_time": 'enqueuedTime',
        "answer_time": 'answerTime',
        "end_time": 'endTime',
        "disconnect_cause": 'disconnectCause',
        "error_message": 'errorMessage',
        "error_id": 'errorId',
        "last_update": 'lastUpdate'
    }

    def __init__(self,
                 call_id=None,
                 parent_call_id=None,
                 application_id=None,
                 account_id=None,
                 to=None,
                 mfrom=None,
                 direction=None,
                 state=None,
                 identity=None,
                 stir_shaken=None,
                 start_time=None,
                 enqueued_time=None,
                 answer_time=None,
                 end_time=None,
                 disconnect_cause=None,
                 error_message=None,
                 error_id=None,
                 last_update=None):
        """Constructor for the CallState class"""

        # Initialize members of the class
        self.call_id = call_id
        self.parent_call_id = parent_call_id
        self.application_id = application_id
        self.account_id = account_id
        self.to = to
        self.mfrom = mfrom
        self.direction = direction
        self.state = state
        self.identity = identity
        self.stir_shaken = stir_shaken
        self.start_time = APIHelper.RFC3339DateTime(start_time) if start_time else None
        self.enqueued_time = APIHelper.RFC3339DateTime(enqueued_time) if enqueued_time else None
        self.answer_time = APIHelper.RFC3339DateTime(answer_time) if answer_time else None
        self.end_time = APIHelper.RFC3339DateTime(end_time) if end_time else None
        self.disconnect_cause = disconnect_cause
        self.error_message = error_message
        self.error_id = error_id
        self.last_update = APIHelper.RFC3339DateTime(last_update) if last_update else None

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
        call_id = dictionary.get('callId')
        parent_call_id = dictionary.get('parentCallId')
        application_id = dictionary.get('applicationId')
        account_id = dictionary.get('accountId')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        direction = dictionary.get('direction')
        state = dictionary.get('state')
        identity = dictionary.get('identity')
        stir_shaken = dictionary.get('stirShaken')
        start_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("startTime")).datetime if dictionary.get("startTime") else None
        enqueued_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("enqueuedTime")).datetime if dictionary.get("enqueuedTime") else None
        answer_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("answerTime")).datetime if dictionary.get("answerTime") else None
        end_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("endTime")).datetime if dictionary.get("endTime") else None
        disconnect_cause = dictionary.get('disconnectCause')
        error_message = dictionary.get('errorMessage')
        error_id = dictionary.get('errorId')
        last_update = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastUpdate")).datetime if dictionary.get("lastUpdate") else None

        # Return an object of this model
        return cls(call_id,
                   parent_call_id,
                   application_id,
                   account_id,
                   to,
                   mfrom,
                   direction,
                   state,
                   identity,
                   stir_shaken,
                   start_time,
                   enqueued_time,
                   answer_time,
                   end_time,
                   disconnect_cause,
                   error_message,
                   error_id,
                   last_update)
