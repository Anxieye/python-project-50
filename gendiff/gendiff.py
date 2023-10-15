from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import js
from gendiff.parser import get_converted_file


def diff(tree1, tree2):
    """
    The 'diff' function returns a dictionary
    which contains a difference between two files
    and values of keys in this files.
    The state 'added' means that key was not in first file but in second file.
    The state 'deleted' means that key was in first file but not in second file.
    The state 'dictionary' means that value of key has a type dict.
    The state 'not_changed' means that key was in first
    and second file and it has no changes.
    The state 'changed' means that key was in first
    and second file and it was changed.
    """
    result = {}
    children = sorted(set(tree1) | set(tree2))
    for child in children:
        value1 = tree1.get(child)
        value2 = tree2.get(child)
        if child in tree1 and child in tree2:
            if isinstance(value1, dict) and isinstance(value2, dict):
                result[child] = {'state': 'dictionary',
                                 'value': diff(value1, value2)
                                 }
            else:
                if value1 == value2:
                    result[child] = {'state': 'not_changed',
                                     'value': value1
                                     }
                else:
                    result[child] = {'state': 'changed',
                                     'old_value': value1,
                                     'new_value': value2
                                     }
        elif child not in tree2:
            result[child] = {'state': 'deleted',
                             'value': value1
                             }
        else:
            result[child] = {'state': 'added',
                             'value': value2
                             }
    return result


def read_file(path):
    return open(path)


def get_extention(path):
    if path.endswith('.json'):
        return 'json'
    if path.endswith('.yaml') or path.endswith('.yml'):
        return 'yaml'


def generate_diff(first_path, second_path, format='stylish'):
    """
    This function contains the "diff" function
    which generates a diff dictionary between two files
    and the "stylish"
    which creates a string vision of difference
    """
    formatters = {'stylish': stylish,
                  'plain': plain,
                  'json': js
                  }
    data1 = read_file(first_path)
    data2 = read_file(second_path)
    ext1 = get_extention(first_path)
    ext2 = get_extention(second_path)
    file1 = get_converted_file(ext1, data1)
    file2 = get_converted_file(ext2, data2)
    difference = diff(file1, file2)
    return formatters[format](difference)
