from kelvin.siblings.data import banxico_service as bs
from unittest import TestCase
from unittest.mock import MagicMock


class TestBanxicoService(TestCase):
    def test_get_exchange_rates(self):
        # arrange
        mockLogger = MagicMock()

        # act
        with bs.BanxicoService(mockLogger) as sut:
            actual = [item for item in sut.get_exchange_rates()]

        # assert
        self.assertTrue(len(actual) > 0)
