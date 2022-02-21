import sys
from pathlib import Path

import ssg.parsers

class Site:
    def __init__(self, source, dest, parsers=None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []  # when parsers=None instance variable _parsers is assigned to empty list

    def create_dir(self,path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser
                
    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:   # comparision with None
            parser.parse(path, self.source, self.dest)
        else:
            self.error("No parser for the {} extension, file skipped!".format(path.suffix))
            
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob('*'):   # recursive glob
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
    
    @staticmethod
    def error(message):
        sys.stderr.write("\x1b[1;31m{}\n".format(message))
    