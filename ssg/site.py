from pathlib import Path
import ssg.parsers

class Site:
    def __init__(self, source, dest,parsers=None):
        self._source = Path(source)
        self._dest = Path(dest)

    def create_dir(self,path):
        directory = self._dest / path.relative_to(self._source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self._dest.mkdir(parents=True, exist_ok=True)
        for path in self._source.rglob('*'):   # recursive glob
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                Parser.run_parser()
                
    def load_parsers(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser
                
    def run_parser(self, path):
        self.load_parsers(path.suffix)
        if parser != None:
            ResourceParser.parse()