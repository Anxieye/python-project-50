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
