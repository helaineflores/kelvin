from Kelvin.business.strange_processor import StrangeProcessor
from Kelvin.business.oo import OnlyOne


import unittest
import unittest.mock


class TestStrangeProcessor(unittest.TestCase):
    @unittest.mock.patch.object(OnlyOne, 'get_value', autospec=True)
    def test_exec(self, mock_get_value):
        mock_get_value.return_value = 'Charmander'
        sut = StrangeProcessor()
        sut.exec()
        assert(sut.onlyone.get_value() == "Charmander")
        mock_get_value.assert_called()

