from .indicators_service import IndicatorsService
from .banxico_parser import BanxicoParser
from zeep import Client, Transport

import requests


WSDL = 'http://www.banxico.org.mx/DgieWSWeb/DgieWS?wsdl'


class BanxicoService(IndicatorsService):
    def __init__(self, logger):
        self._logger = logger
        self._parser = BanxicoParser()
        try:
            self._session = requests.Session()
            self._client = Client(WSDL, transport=Transport(session=self._session))
        except Exception as ex:
            self._session = None
            self._client = None
            self._logger.error(ex)

    def __enter__(self):
        return self

    def get_exchange_rates(self):
        assert self._session and self._client, 'Banxico communication failed'

        response = self._client.service.tiposDeCambioBanxico()
        return self._parser.parse(response)

    def close(self):
        if(self._session):
            self._session.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
