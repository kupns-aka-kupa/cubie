import codecs
import json


class FileManager:

    @staticmethod
    def recursive_load(stored_data, _list):
        for element in _list:
            if isinstance(element, str):
                key = (element.split("/")[-1]).split(".")[0].upper()
                stored_data[key] = FileManager.open_file(element)
            elif isinstance(element, dict):
                stored_data[key] = element
            else:
                FileManager.recursive_load(stored_data, element)


    @staticmethod
    def load(_list):
        data = {}
        FileManager.recursive_load(data, _list)
        return data

    def save(self):
        pass

    @staticmethod
    def open_file(file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def write_file(data, file_name):
        with codecs.open(file_name, 'w', encoding='utf8') as file:
            json.dump(data, file)
