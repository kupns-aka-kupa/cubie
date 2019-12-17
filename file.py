import codecs
import json


def load(file_name):
    with codecs.open(file_name, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data


def save(data, file_name):
    with codecs.open(file_name, 'w', encoding='utf8') as file:
        json.dump(data, file)
