from gendiff import generate_diff, get_converted_file
from gendiff.formatters import gen_js_bool
import pytest


flat = 'tests/fixtures/flat_result.txt'
tree = 'tests/fixtures/result_tree.txt'
plain = 'tests/fixtures/plain_result.txt'
json = 'tests/fixtures/json_result.json'
fst_json = 'tests/fixtures/file1.json'
scnd_json = 'tests/fixtures/file2.json'
fst_yaml = 'tests/fixtures/file1.yml'
scnd_yaml = 'tests/fixtures/file2.yaml'
js_1 = 'tests/fixtures/tree1.json'
js_2 = 'tests/fixtures/tree2.json'
yml_1 = 'tests/fixtures/tree1.yaml'
yml_2 = 'tests/fixtures/tree2.yml'


@pytest.mark.parametrize('file1, file2, excepted, format',
                         [(fst_json, scnd_json, flat, 'stylish'),
                          (fst_yaml, scnd_yaml, flat, 'stylish'),
                          (fst_json, scnd_yaml, flat, 'stylish'),
                          (js_1, js_2, tree, 'stylish'),
                          (js_1, yml_2, tree, 'stylish'),
                          (yml_1, yml_2, tree, 'stylish'),
                          (js_1, js_2, plain, 'plain'),
                          (js_1, yml_2, plain, 'plain'),
                          (yml_1, yml_2, plain, 'plain'),
                          (js_1, js_2, json, 'json'),
                          (js_1, yml_2, json, 'json'),
                          (yml_1, yml_2, json, 'json')])
def test_generate_diff(file1, file2, excepted, format):
    with open(excepted, 'r') as excepted_result:
        result = excepted_result.read()
        assert generate_diff(file1, file2, format) == result


def test_gen_js_bool():
    assert gen_js_bool(True) == 'true'
    assert gen_js_bool('') == ''
    assert gen_js_bool(10) == 10
    assert gen_js_bool('false') == 'false'
    assert gen_js_bool(None) == 'null'


@pytest.mark.parametrize('file', [fst_json, scnd_json,
                                  fst_yaml, scnd_yaml,
                                  js_1, js_2,
                                  yml_1, yml_2
                                  ]
                         )
def test_get_converted_file(file):
    assert isinstance(get_converted_file(file), dict)
