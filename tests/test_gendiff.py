from gendiff import generate_diff, gen_js_bool, get_converted_file
import pytest


flat = 'tests/fixtures/result_json.txt'
tree = 'tests/fixtures/result_tree.txt'
fst_json = 'tests/fixtures/file1.json'
scnd_json = 'tests/fixtures/file2.json'
fst_yaml = 'tests/fixtures/file1.yml'
scnd_yaml = 'tests/fixtures/file2.yaml'
js_tree1 = 'tests/fixtures/tree1.json'
js_tree2 = 'tests/fixtures/tree2.json'
yml_tree1 = 'tests/fixtures/tree1.yaml'
yml_tree2 = 'tests/fixtures/tree2.yml'


@pytest.mark.parametrize('file1, file2, excepted', [(fst_json, scnd_json, flat),
                                                    (fst_yaml, scnd_yaml, flat),
                                                    (js_tree1, js_tree2, tree),
                                                    (yml_tree1, yml_tree2, tree)
                                                    ]
                         )
def test_generate_diff(file1, file2, excepted):
    with open(excepted, 'r') as excepted_result:
        result = excepted_result.read()
        assert generate_diff(file1, file2) == result


def test_gen_js_bool():
    assert gen_js_bool(True) == 'true'
    assert gen_js_bool('') == ''
    assert gen_js_bool(10) == 10
    assert gen_js_bool('false') == 'false'
    assert gen_js_bool(None) == 'null'


@pytest.mark.parametrize('file', [fst_json, scnd_json,
                                  fst_yaml, scnd_yaml,
                                  js_tree1, js_tree2,
                                  yml_tree1, yml_tree2
                                  ]
                         )
def test_get_converted_file(file):
    assert isinstance(get_converted_file(file), dict)
