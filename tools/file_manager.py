import os, codecs, json

class FileManager():

    def open_file(self, file_name):
        with codecs.open(file_name, 'r', encoding = 'utf8') as file:
            data = json.load(file)
        return data

    def write_file(self, file_name, data):
        with codecs.open(file_name, 'w', encoding = 'utf8') as file:
            json.dump(data, file)
