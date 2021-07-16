"""
Basic Config handler
"""
from sys import platform

from ..info import name as app_name
from .data import ABCData

BASE = None

if platform == 'linux':
    from xdg import XDG_CONFIG_HOME
    BASE = XDG_CONFIG_HOME.joinpath(app_name)
    if BASE.exists() and not BASE.is_dir():
        BASE.unlink()

if not BASE.exists():
    BASE.mkdir()


class Config(ABCData):
    """
    Config Handler
    """

    def __create__(self):
        self._file = BASE.joinpath(f"{self.name}.toml")
