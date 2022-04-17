import pytest

class TestStringConvert:
    @pytest.fixture
    def target(self):
        from fizz_buzz import string_convert        
        return string_convert

    check_value_data = [
        (1, '1'),
        (2, '2'),
        (3, 'Fizz')
    ]

    @pytest.mark.parametrize('num, expected_return_value', check_value_data)
    def test_return_value(self, target, num, expected_return_value):      
        assert target(num) == expected_return_value
