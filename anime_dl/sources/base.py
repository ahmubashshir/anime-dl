"""
    base module for episode sources
"""
from abc import ABCMeta, abstractmethod


class Source:
    """
        Abstract Base class for episode source
    """
    __metaclass__ = ABCMeta
    data = {
        'url': None,
        'type': None
    }

    @abstractmethod
    def retrive(self):
        """ retrive data from source """
        return

    @property
    def url(self):
        """get final url"""
        if not self.data['url']:
            self.retrive()

        return self.data['url']

    @property
    def type(self):
        """ get source type """
        if not self.data['type']:
            self.retrive()

        return self.data['type']

    def __init__(self, sid=None):
        self._id = sid


class InvalidSource(Source):
    name = 'NotImplemented'

    def __init__(self, sid, name='NotImplemented'):
        Source.__init__(self, sid)
        self.name = name

    def retrive(self):
        self.data['url'] = '%s: Not Implemented' % self.name
        self.data['type'] = 'Unknown'
