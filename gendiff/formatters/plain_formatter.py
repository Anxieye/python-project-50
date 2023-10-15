from gendiff.formatters.to_style import gen_json_value, to_plain_style


text = {'added': "Property '{}' was added with value: {}",
        'deleted': "Property '{}' was removed",
        'changed': "Property '{}' was updated. From {} to {}"}


def plain(diff: dict) -> str:
    """
    This function completes the formatting of a string
    by removing the last line break from it and
    returns a final result
    """
    plain_lst = []
    get_plain_string(diff, '', 1, plain_lst)
    final = '\n'.join(filter(lambda _: _ not in ['', None], plain_lst))
    return final


def get_plain_string(diff, path, depth, plain_lst):
    """
    This function is formatter for dict type from python.
    Generates a string that looks like a plain text with
    a description of what happened
    """

    for key in diff:
        value = gen_json_value(diff.get(key).get('value'))
        STATE = diff.get(key).get('state')
        if depth < 2:
            path = key

        if STATE == 'dictionary':
            plain_lst.append(get_plain_string(value,
                                              build_path(depth, path, key),
                                              depth + 1,
                                              plain_lst
                                              )
                             )
        if STATE == 'changed':
            old = gen_json_value(diff.get(key).get('old_value'))
            new = gen_json_value(diff.get(key).get('new_value'))
            plain_lst.append(text['changed'].format(build_path(depth,
                                                               path,
                                                               key),
                                                    to_plain_style(old),
                                                    to_plain_style(new)))
        if STATE == 'added':
            plain_lst.append(text['added'].format(build_path(depth,
                                                             path,
                                                             key),
                                                  to_plain_style(value)))
        if STATE == 'deleted':
            plain_lst.append(text['deleted'].format(build_path(depth,
                                                               path,
                                                               key)))


def build_path(depth, path, key):
    """
    This function builds a path for plain format
    """
    if depth >= 2:
        path += f'.{key}'
    else:
        return path
    return path
