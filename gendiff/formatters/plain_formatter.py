from gendiff.formatters.to_js import gen_json_value


def plain(diff: dict) -> str:
    """
    This function completes the formatting of a string
    by removing the last line break from it and
    returns a final result
    """
    result = get_plain_string(diff, '', 1)
    result = result[:-1]
    return result


def get_plain_string(diff, path, depth):
    """
    This function is formatter for dict type from python.
    Generates a string that looks like a plain text with
    a description of what happened
    """
    string = ''
    JS_TYPE = ['null', 'true', 'false']
    for key in diff:
        value = gen_json_value(diff.get(key).get('value'))
        state = diff.get(key).get('state')
        if depth < 2:
            path = key

        if state == 'dictionary':
            string += (get_plain_string(value,
                                        build_path(depth, path, key),
                                        depth + 1
                                        )
                       )
        if state == 'changed':
            old = gen_json_value(diff.get(key).get('old_value'))
            new = gen_json_value(diff.get(key).get('new_value'))
            string += (get_changed_property(build_path(depth, path, key),
                                            new, old,
                                            JS_TYPE
                                            )
                       )
        if state == 'added':
            string += (get_added_property(value,
                                          build_path(depth, path, key),
                                          JS_TYPE
                                          )
                       )
        if state == 'deleted':
            string += (get_deleted_property(value,
                                            build_path(depth, path, key)
                                            )
                       )
    return string


def build_path(depth, path, key):
    """
    This function builds a path for plain format
    """
    if depth >= 2:
        path += f'.{key}'
    else:
        return path
    return path


def get_added_property(value, path, type):
    """
    This function creates a string which contains an added property
    """
    string = ''
    if isinstance(value, dict):
        string += f"Property '{path}' was added with value: [complex value]\n"
    elif is_not_str(value, type):
        string += f"Property '{path}' was added with value: {value}\n"
    else:
        string += f"Property '{path}' was added with value: '{value}'\n"
    return string


def get_deleted_property(value, path):
    """
    This function creates a string which contains a deleted property
    """
    return f"Property '{path}' was removed\n"


def get_changed_property(path, new, old, type):
    """
    This function creates a string which contains a changed property
    """
    string = ''
    if isinstance(old, dict):
        if is_not_str(new, type):
            string += f"Property '{path}' was updated. "
            string += f"From [complex value] to {new}\n"
        else:
            string += f"Property '{path}' was updated. "
            string += f"From [complex value] to '{new}'\n"
    elif isinstance(new, dict):
        if is_not_str(old, type):
            string += f"Property '{path}' was updated. "
            string += f"From {old} to [complex value]\n"
        else:
            string += f"Property '{path}' was updated. "
            string += f"From '{old}' to [complex value]\n"
    else:
        if is_not_str(old, type) and is_not_str(new, type):
            string += f"Property '{path}' was updated. "
            string += f"From {old} to {new}\n"
        elif new in type or isinstance(new, int):
            string += f"Property '{path}' was updated. "
            string += f"From '{old}' to {new}\n"
        elif old in type or isinstance(old, int):
            string += f"Property '{path}' was updated. "
            string += f"From {old} to '{new}'\n"
        else:
            string += f"Property '{path}' was updated. "
            string += f"From '{old}' to '{new}'\n"
    return string


def is_not_str(value, type):
    """
    This is a function-predicate that
    checks if a value is a boolean type, NoneType
    or not str and returns True or False
    """
    if not isinstance(value, str) or value in type:
        return True
    else:
        return False
