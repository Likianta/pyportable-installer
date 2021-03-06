from os import popen

from .base import BaseCompiler
from ..global_dirs import global_dirs


class PycCompiler(BaseCompiler):
    
    def __init__(self, python_interpreter=''):
        super().__init__(python_interpreter)
        self._code_template = 'from py_compile import compile; ' \
                              'compile(\'{src_file}\', \'{dst_file}\')'
    
    def compile_all(self, pyfiles: list[str]):
        for src_file in pyfiles:
            dst_file = global_dirs.to_dist(src_file) + 'c'
            self.compile_one(src_file, dst_file)
    
    def compile_one(self, src_file, dst_file):
        """ Compile py file to pyc.
        
        References:
            https://stackoverflow.com/questions/5607283/how-can-i-manually
                -generate-a-pyc-file-from-a-py-file
            https://docs.python.org/3/library/py_compile.html
        """
        code = self._code_template.format(
            src_file=src_file, dst_file=dst_file
        )
        popen(f'{self._interpreter} -c "{code}"')
