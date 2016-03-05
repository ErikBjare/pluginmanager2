from typing import Any
import functools


class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
        functools.update_wrapper(self, cls)

    def __call__(self, *args, **kwds) -> Any:
        if self.instance is None:
            self.instance = self.cls(*args, **kwds)
        return self.instance

    def reset_singleton(self):
        """
        Detaches the instance from the singleton, causing the creation of
        a new object when __call__'d.
        Useful in testing.
        """
        self.instance = None
