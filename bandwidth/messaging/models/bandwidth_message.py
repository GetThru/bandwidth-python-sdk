# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BandwidthMessage(object):

    """Implementation of the 'BandwidthMessage' model.

    TODO: type model description here.

    Attributes:
        id (string): The id of the message
        owner (string): The Bandwidth phone number associated with the
            message
        application_id (string): The application ID associated with the
            message
        time (string): The datetime stamp of the message in ISO 8601
        segment_count (int): The number of segments the original message from
            the user is broken into before sending over to carrier networks
        direction (string): The direction of the message relative to
            Bandwidth. Can be in or out
        to (list of string): The phone number recipients of the message
        mfrom (string): The phone number the message was sent from
        media (list of string): The list of media URLs sent in the message.
            Including a `filename` field in the `Content-Disposition` header
            of the media linked with a URL will set the displayed file name.
            This is a best practice to ensure that your media has a readable
            file name.
        text (string): The contents of the message
        tag (string): The custom string set by the user
        priority (string): The priority specified by the user

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "owner": 'owner',
        "application_id": 'applicationId',
        "time": 'time',
        "segment_count": 'segmentCount',
        "direction": 'direction',
        "to": 'to',
        "mfrom": 'from',
        "media": 'media',
        "text": 'text',
        "tag": 'tag',
        "priority": 'priority'
    }

    def __init__(self,
                 id=None,
                 owner=None,
                 application_id=None,
                 time=None,
                 segment_count=None,
                 direction=None,
                 to=None,
                 mfrom=None,
                 media=None,
                 text=None,
                 tag=None,
                 priority=None):
        """Constructor for the BandwidthMessage class"""

        # Initialize members of the class
        self.id = id
        self.owner = owner
        self.application_id = application_id
        self.time = time
        self.segment_count = segment_count
        self.direction = direction
        self.to = to
        self.mfrom = mfrom
        self.media = media
        self.text = text
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
        id = dictionary.get('id')
        owner = dictionary.get('owner')
        application_id = dictionary.get('applicationId')
        time = dictionary.get('time')
        segment_count = dictionary.get('segmentCount')
        direction = dictionary.get('direction')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        media = dictionary.get('media')
        text = dictionary.get('text')
        tag = dictionary.get('tag')
        priority = dictionary.get('priority')

        # Return an object of this model
        return cls(id,
                   owner,
                   application_id,
                   time,
                   segment_count,
                   direction,
                   to,
                   mfrom,
                   media,
                   text,
                   tag,
                   priority)
