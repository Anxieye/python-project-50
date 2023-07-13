import json
import yaml


def generate_diff(first_path, second_path):
    file1 = get_converted_file(first_path)
    file2 = get_converted_file(second_path)
    sorted_set = sorted(set(file1) | set(file2))
    diff = ''

    for key in sorted_set:
        value1 = gen_js_bool(file1.get(key))
        value2 = gen_js_bool(file2.get(key))
        if key in file1 and key in file2:
            if value1 == value2:
                diff += f'    {key}: {value1}\n'
            else:
                diff += f'  - {key}: {value1}\n  + {key}: {value2}\n'
        elif key not in file2:
            diff += f'  - {key}: {value1}\n'
        else:
            diff += f'  + {key}: {value2}\n'

    return '{\n' + diff + '}'


def gen_js_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    else:
        return value


def get_converted_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
