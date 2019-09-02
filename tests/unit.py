from app import fruitpal


class TestFruitpal:
    def test_load_data(self):
        fp = fruitpal.Fruitpal()
        fp.load_data('tests/test_data.json')
        assert fp.prices
