def gen_json_value(value):
    """
    This function generates a string like in json files
    from python bool data type and NoneType.
    Example: True = 'true', None = 'null'
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def to_plain_style(value):
    JS_TYPE = ['null', 'true', 'false']
    if value in JS_TYPE or isinstance(value, int):
        return value
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"
