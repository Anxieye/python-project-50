import json


def js(diff):
    """
    This functions converts "diff" which is dictionary
    to json format
    """
    json_format = json.dumps(diff, indent=4)
    return json_format
