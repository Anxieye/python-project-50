from gendiff import generate_diff, gen_js_bool
import pytest


path = 'tests/fixtures/result_json.txt'
first_file = 'tests/fixtures/file1.json'
second_file = 'tests/fixtures/file2.json'


@pytest.mark.parametrize('file1, file2, excepted', [(first_file, second_file, path)])
def test_generate_diff(file1, file2, excepted):
    with open(excepted, 'r') as excepted_result:
        result = excepted_result.read()
        assert generate_diff(file1, file2) == result


def test_gen_js_bool():
    assert gen_js_bool(True) == 'true'
    assert gen_js_bool('') == ''
    assert gen_js_bool(10) == 10
    assert gen_js_bool('false') == 'false'
