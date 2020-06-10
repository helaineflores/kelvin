from kelvin.siblings.environment import configuration as c

import unittest
import unittest.mock


CONFIGURATION_FILE_FOR_TESTING = 'tests/files/config.yaml'


class TestConfiguration(unittest.TestCase):
    def test_is_singleton(self):
        # arrange
        filepath = CONFIGURATION_FILE_FOR_TESTING

        # act
        sut1 = c.Configuration(filepath)
        sut2 = c.Configuration(filepath)

        # assert
        self.assertEqual(id(sut1), id(sut2))

    def test_environment(self):
        # arrange
        filepath = CONFIGURATION_FILE_FOR_TESTING

        # act
        sut = c.Configuration(filepath)
        actual = sut.environment

        # assert
        expected = 'ENVIRONMENT_FOR_TESTING'
        self.assertEqual(expected, actual)

    def test_connection_string(self):
        # arrange
        filepath = CONFIGURATION_FILE_FOR_TESTING

        # act
        sut = c.Configuration(filepath)
        actual = sut.connection_string

        # assert
        expected = 'CONNECTION_STRING_FOR_TESTING'
        self.assertEqual(expected, actual)

    def test_http_logging_url(self):
        # arrange
        filepath = CONFIGURATION_FILE_FOR_TESTING

        # act
        sut = c.Configuration(filepath)
        actual = sut.http_logging_url

        # assert
        expected = 'URL_FOR_TESTING'
        self.assertEqual(expected, actual)
