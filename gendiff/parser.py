import yaml
import json


def get_converted_file(extention, data):
    """
    This function creates a dict type of python
    from json or yaml files
    """
    if extention == 'json':
        return json.load(data)
    if extention == 'yaml':
        return yaml.safe_load(data)
