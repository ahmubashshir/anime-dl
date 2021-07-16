"""
	base module for sites
"""

from abc import ABCMeta, abstractmethod as method
from enum import Enum


class EpTypes(Enum):
    TV = 'TV'
    SPECIAL = 'Special'
    OVA = 'OVA'
    ONA = 'ONA'
    MOVIE = 'Movie'


class Site:
    """
            Abstract Base class for sites
    """
    __metaclass__ = ABCMeta

    @method
    def search(self, what, *args, **kwargs):
        """
                Search in site
        """
        return

    def episode(self, _id):
        """
                Get Episode by ID
        """
        return Episode(_id)

    def anime(self, _id):
        """
                Get Anime by ID
        """
        return Anime(_id)


class Anime:
    """
            Base Class for anime
    """

    __metaclass__ = ABCMeta
    ID = None
    props: dict = {}
    Type: EpTypes = EpTypes.TV

    def __init__(self, _id, *args, **kwargs):
        """
                Default Initializer
        """
        self.ID = _id

    @method
    def retrive(self):
        """
                Retrive anime data from site
        """
        return

    @property
    def episodes(self):
        if not self.props.get('episodes', None):
            self.retrive()
        return self.props['episodes']


class Episode:
    """
            Base class for episode
    """
    __metaclass__ = ABCMeta

    ID = None
    NUM: int = None
    Type: EpTypes = EpTypes.TV
    props: dict = {}

    def __init__(self, _id, *args, **kwargs):
        """
                Base init method
        """
        self.ID = _id

    @method
    def retrive(self):
        """
                Retrive episode data
        """

    @property
    def mirrors(self):
        if not self.props.get('mirrors', None):
            self.retrive()
        return self.props.get('mirrors', None)
