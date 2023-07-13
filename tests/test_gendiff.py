from gendiff import generate_diff, gen_js_bool, get_converted_file
import pytest


path = 'tests/fixtures/result_json.txt'
fst_json = 'tests/fixtures/file1.json'
scnd_json = 'tests/fixtures/file2.json'
fst_yaml = 'tests/fixtures/file1.yml'
scnd_yaml = 'tests/fixtures/file2.yaml'


@pytest.mark.parametrize('file1, file2, excepted', [(fst_json, scnd_json, path),
                                                    (fst_yaml, scnd_yaml, path)
                                                    ])
def test_generate_diff(file1, file2, excepted):
    with open(excepted, 'r') as excepted_result:
        result = excepted_result.read()
        assert generate_diff(file1, file2) == result


def test_gen_js_bool():
    assert gen_js_bool(True) == 'true'
    assert gen_js_bool('') == ''
    assert gen_js_bool(10) == 10
    assert gen_js_bool('false') == 'false'


@pytest.mark.parametrize('file', [fst_json, scnd_json,
                                  fst_yaml, scnd_yaml
                                  ])
def test_get_converted_file(file):
    assert isinstance(get_converted_file(file), dict)
