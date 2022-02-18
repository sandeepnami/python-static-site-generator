from importlib.abc import Loader
import re
from time import clock_settime # regular expression
from yaml import loader, FullLoader
from collections.abc import Mapping


class Contents(Mapping):
    
    __delimitter = r"^(?:-|\+){3}\s*$"   # this is raw string
    __regex = re.compile(__delimitter, re.MULTILINE)
    
    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)  # dont want to capture first element so give _
        metadata = cls.load(fm, Loader=FullLoader)
        return cls(metadata, content)
    
    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content
    