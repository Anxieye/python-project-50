def gen_js_bool(value):
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


def gen_json_string(dict_value, depth, special):
    """
    This function generates a string from a key's value that is a dictionary.
    It is used to traverse key values that the function 'diff' did not traverse
    due to the fact that the key was in one of the two files
    or when the key was changed, the value was a dictionary.
    """
    string = ''
    spaces = 4
    step = spaces * depth - 2
    space = ' ' * step

    for key, value in dict_value.items():
        value = gen_js_bool(value)
        if isinstance(value, dict):
            string += f'{space}{special}{key}: '
            string += f'{gen_json_string(value, depth + 1, special)}\n'
        else:
            string += f'{space}{special}{key}: {value}\n'

    return '{\n' + string + (' ' * spaces * (depth - 1)) + '}'


def stylish(diff: dict) -> str:
    """
    This function is formatter for dict type from python.
    Generates a string which looks like text from json files
    """
    def inner(diff, depth):
        string = ''
        spaces = 4
        step = spaces * depth - 2
        space = ' ' * step
        added = '+ '
        deleted = '- '
        immut = '  '
        for key in diff:
            value = gen_js_bool(diff.get(key).get('value'))
            state = diff.get(key).get('state')
            if state == 'added':
                if isinstance(value, dict):
                    string += f'{space}{added}{key}: '
                    string += f'{gen_json_string(value, depth + 1, immut)}\n'
                else:
                    string += f'{space}{added}{key}: {value}\n'
            elif state == 'deleted':
                if isinstance(value, dict):
                    string += f'{space}{deleted}{key}: '
                    string += f'{gen_json_string(value, depth + 1, immut)}\n'
                else:
                    string += f'{space}{deleted}{key}: {value}\n'
            elif state == 'not_changed':
                if isinstance(value, dict):
                    string += f'{space}{immut}{key}: '
                    string += f'{gen_json_string(value, depth + 1, immut)}\n'
                else:
                    string += f'{space}{immut}{key}: {value}\n'
            elif state == 'changed':
                old = gen_js_bool(diff.get(key).get('old_value'))
                new = gen_js_bool(diff.get(key).get('new_value'))
                if isinstance(old, dict) and not isinstance(new, dict):
                    string += f'{space}{deleted}{key}: '
                    string += f'{gen_json_string(old, depth + 1, immut)}\n'
                    string += f'{space}{added}{key}: {new}\n'
                elif isinstance(new, dict) and not isinstance(old, dict):
                    string += f'{space}{deleted}{key}: {old}\n'
                    string += f'{space}{added}{key}: '
                    string += f'{gen_json_string(new, depth + 1, immut)}\n'
                elif isinstance(old, dict) and isinstance(new, dict):
                    string += f'{space}{deleted}{key}: '
                    string += f'{gen_json_string(old, depth + 1, immut)}\n'
                    string += f'{space}{added}{key}: '
                    string += f'{gen_json_string(new, depth + 1, immut)}\n'
                else:
                    string += f'{space}{deleted}{key}: {old}\n'
                    string += f'{space}{added}{key}: {new}\n'
            else:
                string += f'{space}{immut}{key}: '
                string += f'{inner(value, depth + 1)}\n'
        return '{\n' + string + (' ' * spaces * (depth - 1)) + '}'
    return inner(diff, 1)
