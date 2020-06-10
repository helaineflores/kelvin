from kelvin.siblings.business import indicators_processor as ip
from unittest import TestCase
from unittest.mock import MagicMock
from datetime import datetime

class TestIndicatorsProcessor(TestCase):
    def test_execute(self):
        # arrange
        exchange_rates = \
            [
                ('Euro', 'SF46410', datetime(2019, 4, 1).date(), 21.5835),
                ('Dólar USA (FIX)', 'SF43718', datetime(2019, 4, 1).date(), 19.2169),
                ('Libra', 'SF46407', datetime(2019, 4, 1).date(), 25.1837),
                ('Yen', 'SF46406', datetime(2019, 4, 1).date(), 0.1732),
                ('Dólar USA', 'SF60653', datetime(2019, 4, 1).date(), 19.3793)
            ]
        usd = {'time_period': datetime(2019, 4, 1).date(), 'value': 19.2169}
        mockService = MagicMock()
        mockRepository = MagicMock()
        mockLogger = MagicMock()

        mockService.get_exchange_rates.return_value = exchange_rates

        # act
        sut = ip.IndicatorsProcessor(mockService, mockRepository, mockLogger)
        sut.execute()

        # assert
        mockService.get_exchange_rates.assert_called()
        mockRepository.save_usd_exchange_rate.assert_called_with(usd)
        mockLogger.error.assert_not_called()

    def test_execute_with_usd_none(self):
        # arrange
        exchange_rates = \
            [
                ('Euro', 'SF46410', datetime(2019, 4, 1).date(), 21.5835),
                ('Dólar USA', 'SF43718', datetime(2019, 4, 1).date(), 19.2169),
                ('Libra', 'SF46407', datetime(2019, 4, 1).date(), 25.1837),
                ('Yen', 'SF46406', datetime(2019, 4, 1).date(), 0.1732),
                ('Dólar USA', 'SF60653', datetime(2019, 4, 1).date(), 19.3793)
            ]
        mockService = MagicMock()
        mockRepository = MagicMock()
        mockLogger = MagicMock()

        mockService.get_exchange_rates.return_value = exchange_rates

        # act
        sut = ip.IndicatorsProcessor(mockService, mockRepository, mockLogger)
        sut.execute()

        # assert
        mockService.get_exchange_rates.assert_called()
        mockRepository.save_usd_exchange_rate.assert_not_called()
        mockLogger.error.assert_not_called()

    def test_usd_from(self):
        # arrange
        exchange_rates = \
            [
                ('Euro', 'SF46410', datetime(2019, 4, 1).date(), 21.5835),
                ('Dólar USA (FIX)', 'SF43718', datetime(2019, 4, 1).date(), 19.2169),
                ('Libra', 'SF46407', datetime(2019, 4, 1).date(), 25.1837),
                ('Yen', 'SF46406', datetime(2019, 4, 1).date(), 0.1732),
                ('Dólar USA', 'SF60653', datetime(2019, 4, 1).date(), 19.3793)
            ]
        mockService = MagicMock()
        mockRepository = MagicMock()
        mockLogger = MagicMock()

        # act
        sut = ip.IndicatorsProcessor(mockService, mockRepository, mockLogger)
        actual = sut.usd_from(exchange_rates)

        # assert
        expected = {'time_period': datetime(2019, 4, 1).date(), 'value': 19.2169}
        self.assertEqual(expected, actual)

    def test_usd_from_none(self):
        # arrange
        exchange_rates = \
            [
                ('Euro', 'SF46410', datetime(2019, 4, 1).date(), 21.5835),
                ('Dólar USA', 'SF43718', datetime(2019, 4, 1).date(), 19.2169),
                ('Libra', 'SF46407', datetime(2019, 4, 1).date(), 25.1837),
                ('Yen', 'SF46406', datetime(2019, 4, 1).date(), 0.1732),
                ('Dólar USA', 'SF60653', datetime(2019, 4, 1).date(), 19.3793)
            ]
        mockService = MagicMock()
        mockRepository = MagicMock()
        mockLogger = MagicMock()

        # act
        sut = ip.IndicatorsProcessor(mockService, mockRepository, mockLogger)
        actual = sut.usd_from(exchange_rates)

        # assert
        self.assertIsNone(actual)

    def test_execute_logs_when_service_fails(self):
        # arrange
        mockService = MagicMock()
        mockRepository = MagicMock()
        mockLogger = MagicMock()

        mockService.get_exchange_rates.side_effect = Exception('Error')

        # act
        sut = ip.IndicatorsProcessor(mockService, mockRepository, mockLogger)
        sut.execute()

        # assert
        mockService.get_exchange_rates.assert_called()
        mockRepository.save_usd_exchange_rate.assert_not_called()
        mockLogger.error.assert_called()

    def test_execute_logs_when_repository_fails(self):
        # arrange
        exchange_rates = \
            [
                ('Euro', 'SF46410', datetime(2019, 4, 1).date(), 21.5835),
                ('Dólar USA (FIX)', 'SF43718', datetime(2019, 4, 1).date(), 19.2169),
                ('Libra', 'SF46407', datetime(2019, 4, 1).date(), 25.1837),
                ('Yen', 'SF46406', datetime(2019, 4, 1).date(), 0.1732),
                ('Dólar USA', 'SF60653', datetime(2019, 4, 1).date(), 19.3793)
            ]
        usd = {'time_period': datetime(2019, 4, 1).date(), 'value': 19.2169}
        mockService = MagicMock()
        mockRepository = MagicMock()
        mockLogger = MagicMock()

        mockService.get_exchange_rates.return_value = exchange_rates
        mockRepository.save_usd_exchange_rate.side_effect = Exception('Error')

        # act
        sut = ip.IndicatorsProcessor(mockService, mockRepository, mockLogger)
        sut.execute()

        # assert
        mockService.get_exchange_rates.assert_called()
        mockRepository.save_usd_exchange_rate.assert_called_with(usd)
        mockLogger.error.assert_called()
