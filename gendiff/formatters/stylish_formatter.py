from gendiff.formatters.to_style import gen_json_value


def gen_json_string(dict_value, depth, special):
    """
    This function generates a string from a key's value that is a dictionary.
    It is used to traverse key values that the function 'diff' did not traverse
    due to the fact that the key was in one of the two files
    or when the key was changed, the value was a dictionary.
    """
    string = ''
    SPACES = 4
    step = SPACES * depth - 2
    space = ' ' * step

    for key, value in dict_value.items():
        value = gen_json_value(value)
        if isinstance(value, dict):
            string += f'{space}{special}{key}: '
            string += f'{gen_json_string(value, depth + 1, special)}\n'
        else:
            string += f'{space}{special}{key}: {value}\n'

    return '{\n' + string + (' ' * SPACES * (depth - 1)) + '}'


def stylish(diff: dict) -> str:
    """
    This function is formatter for dict type from python.
    Generates a string that looks like an object type from json files
    """
    def inner(diff, depth):
        string = ''
        SPACES = 4
        step = SPACES * depth - 2
        space = ' ' * step
        IMMUT = '  '
        for key in diff:
            value = gen_json_value(diff.get(key).get('value'))
            state = diff.get(key).get('state')
            if state == 'added':
                string += gen_added_property(value,
                                             space,
                                             key,
                                             depth,
                                             IMMUT
                                             )
            elif state == 'deleted':
                string += gen_deleted_property(value,
                                               space,
                                               key,
                                               depth,
                                               IMMUT
                                               )
            elif state == 'not_changed':
                string += gen_not_changed_propety(value,
                                                  space,
                                                  key,
                                                  depth,
                                                  IMMUT
                                                  )
            elif state == 'changed':
                old = gen_json_value(diff.get(key).get('old_value'))
                new = gen_json_value(diff.get(key).get('new_value'))
                string += gen_changed_property(new,
                                               old,
                                               space,
                                               key,
                                               depth,
                                               IMMUT
                                               )
            else:
                string += f'{space}{IMMUT}{key}: '
                string += f'{inner(value, depth + 1)}\n'
        return '{\n' + string + (' ' * SPACES * (depth - 1)) + '}'
    return inner(diff, 1)


def gen_added_property(value, space, key, depth, immut):
    """
    This function creates a string which contains an added property
    """
    string = ''
    ADDED = '+ '
    if isinstance(value, dict):
        string += f'{space}{ADDED}{key}: '
        string += f'{gen_json_string(value, depth + 1, immut)}\n'
    else:
        string += f'{space}{ADDED}{key}: {value}\n'
    return string


def gen_deleted_property(value, space, key, depth, immut):
    """
    This function creates a string which contains a deleted property
    """
    DELETED = '- '
    string = ''
    if isinstance(value, dict):
        string += f'{space}{DELETED}{key}: '
        string += f'{gen_json_string(value, depth + 1, immut)}\n'
    else:
        string += f'{space}{DELETED}{key}: {value}\n'
    return string


def gen_not_changed_propety(value, space, key, depth, immut):
    """
    This function creates a string which contains a not changed property
    """
    string = ''
    if isinstance(value, dict):
        string += f'{space}{immut}{key}: '
        string += f'{gen_json_string(value, depth + 1, immut)}\n'
    else:
        string += f'{space}{immut}{key}: {value}\n'
    return string


def gen_changed_property(new, old, space, key, depth, immut):
    """
    This function creates a string which contains a changed property
    """
    string = ''
    ADDED = '+ '
    DELETED = '- '
    if isinstance(old, dict) and not isinstance(new, dict):
        string += f'{space}{DELETED}{key}: '
        string += f'{gen_json_string(old, depth + 1, immut)}\n'
        string += f'{space}{ADDED}{key}: {new}\n'
    elif isinstance(new, dict) and not isinstance(old, dict):
        string += f'{space}{DELETED}{key}: {old}\n'
        string += f'{space}{ADDED}{key}: '
        string += f'{gen_json_string(new, depth + 1, immut)}\n'
    elif isinstance(old, dict) and isinstance(new, dict):
        string += f'{space}{DELETED}{key}: '
        string += f'{gen_json_string(old, depth + 1, immut)}\n'
        string += f'{space}{ADDED}{key}: '
        string += f'{gen_json_string(new, depth + 1, immut)}\n'
    else:
        string += f'{space}{DELETED}{key}: {old}\n'
        string += f'{space}{ADDED}{key}: {new}\n'
    return string
