from kelvin.siblings.data import banxico_parser as bp
from unittest import TestCase
from datetime import datetime

TEST_FILES_PATH='tests/files'

class TestBanxicoParser(TestCase):
    def test_exchange_rates_parsing(self):
        # arrange
        with open(f'{TEST_FILES_PATH}/banxico_tipos_de_cambio.xml', encoding='utf-8') as file:
            xml = file.read()

        # act
        sut = bp.BanxicoParser()
        actual = [item for item in sut.parse(xml)]

        # assert
        expected = \
            [
                ('Euro', 'SF46410', datetime(2019, 4, 1).date(), 21.5835),
                ('Dólar USA', 'SF43718', datetime(2019, 4, 1).date(), 19.2169),
                ('Libra', 'SF46407', datetime(2019, 4, 1).date(), 25.1837),
                ('Yen', 'SF46406', datetime(2019, 4, 1).date(), 0.1732),
                ('Dólar USA', 'SF60653', datetime(2019, 4, 1).date(), 19.3793)
            ]
        self.assertEqual(expected, actual)
