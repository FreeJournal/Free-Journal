import hashlib
import os


class BitMessageFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name, self.file_extension = os.path.splitext(self.file_path)

    def get_file_path(self):
        return self.file_path

    def get_file_name(self):
        return self.file_name

    def get_file_extension(self):
        return self.file_extension

    def get_file_bytes(self):
        data = None
        with open(self.file_path, 'rb') as f:
            data = f.read()

        return data

    def get_hash(self):
        file_hash = hashlib.md5()

        data = self.get_file_bytes()
        if not data:
            raise Exception("File could not be read!")

        file_hash.update(data)
        return file_hash.hexdigest()

