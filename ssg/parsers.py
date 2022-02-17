from pathlib import Path
from typing import List


class Parser:
    def __init__(self):
        extensions: List[str] = []
        
    def valid_extensions(self,extension):
        return extension in self.extensions
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(self, path):
        with open(path, 'r') as file:
            return file.read()