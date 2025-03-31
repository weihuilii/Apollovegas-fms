import os
import hashlib
from .logger import logger

log = logger('utils.file')
class File(object):

    def __get_hash(self, algorithm='sha256'):
        hash_func = hashlib.new(algorithm)
        with open(self.file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def update(self, file_path):
        try:
            self.file_path = file_path
            self.path = os.path.dirname(self.file_path)
            self.filename = os.path.basename(self.file_path)
            self.size = os.path.getsize(self.file_path)
            self.hash = self.__get_hash()
            self.creation_time = os.path.getctime(self.file_path)
            self.modification_time = os.path.getmtime(self.file_path)
            self.access_time = os.path.getatime(self.file_path)
        except Exception as e:
            log.error(repr(e))

    def __init__(self, file_path):
        self.update(file_path)
    
    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()
        
    def write(self, content):
        with open(self.file_path, 'w') as f:
            f.write(content)
