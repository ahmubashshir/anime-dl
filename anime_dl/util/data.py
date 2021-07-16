"""
Basic Data handler
"""

from sys import platform
from pathlib import Path
from abc import ABCMeta, abstractmethod as method

import toml
from ..info import name as app_name


class ABCData(dict):
    """
        Base class for config/data
    """

    __metaclass__ = ABCMeta
    _file: Path = None
    name: str = None

    def __init__(self, name: str = app_name, default: dict = {}, **kwargs):
        """ Initializer override """
        super().__init__(default, **kwargs)
        self.name = name
        self.__create__()
        self.load()

    @method
    def __create__(self):
        """
        Abstract method for creating file
        """

    def load(self):
        """ Load data from file """
        if self._file.exists():
            with open(self._file, 'r') as _f:
                self.update(toml.load(_f))

    def save(self):
        """ Save data to file """
        with open(self._file, 'w') as _f:
            toml.dump(self, _f)


if platform == 'linux':
    from xdg import XDG_DATA_HOME
    BASE = XDG_DATA_HOME.joinpath(app_name)

if BASE.exists() and not BASE.is_dir():
    BASE.unlink()

if not BASE.exists():
    BASE.mkdir()


class Data(ABCData):
    """
    Data Handler
    """

    def __create__(self):
        self._file = BASE.joinpath(f"{self.name}.toml")
