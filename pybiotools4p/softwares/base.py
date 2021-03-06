# AUTOGENERATED! DO NOT EDIT! File to edit: 00_base.ipynb (unless otherwise specified).

__all__ = ['Base', 'modify_cmd', 'modify_cmd']

# Cell


from abc import ABCMeta
from functools import wraps

# Cell

class Base(metaclass=ABCMeta):
    def __init__(self, software):
        self._software = software

    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;{software} --version'.format(
            repr=self.__repr__(),

            software=self._software
        )

    def __repr__(self):
        return "Base()"

    def __str__(self):
        return "Abstract class Base"

# Cell

def modify_cmd(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).rstrip().lstrip()

    return wrapper

# Cell

def modify_cmd(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).rstrip().lstrip()

    return wrapper