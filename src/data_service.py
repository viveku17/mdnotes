import os
import tempfile

DATA = {
    "ActiveDirectory": "",
    "FileStructure": {}
}


def get_data(key):
    return DATA[key]

def set_data(key, value):
    if not key in DATA:
        raise KeyError
    DATA[key] = value
