import re

from app import fruitpal


class TestFruitpal:
    def setup_method(self):
        self.fp = fruitpal.Fruitpal()
        self.fp.load_data('tests/test_data.json')
        assert self.fp.prices
        assert not self.fp.bad_entries

    def test_bad_data(self):
        fp = fruitpal.Fruitpal()
        fp.load_data('tests/bad_data.json')
        assert not fp.prices
        assert fp.bad_entries

    def test_calculate(self):
        result = self.fp.calculate_and_list_prices('mango', 53, 405)
        assert next(filter(lambda x: x[0] == 'MX', result))[1] == 21999.2

    def test_format(self):
        result = fruitpal.Fruitpal.format_data(
            [('Foo', 1234, '(1*2)+3')]
        )
        assert re.match(r'\w+ [0-9\.]+ | ([0-9\.]+\*[0-9\.]+)\+[0-9\.]+', result)
