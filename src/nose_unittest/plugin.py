import sys
import unittest
from nose.plugins.base import Plugin


class UnitTestPlugin(Plugin):
    """
    Enables unittest compatibility mode (dont test functions, only TestCase subclasses,
    and only methods that start with [Tt]est).
    """
    enabled = True
    score = sys.maxint
    name = 'unittest'

    def configure(self, options, conf):
        pass

    def wantClass(self, cls):
        if 'test' not in cls.__name__.lower():
            return False
        if not issubclass(cls, unittest.TestCase):
            return False

    def wantMethod(self, method):
        if not issubclass(method.im_class, unittest.TestCase):
            return False
        if not method.__name__.lower().startswith('test'):
            return False

    def wantFunction(self, function):
        return False
