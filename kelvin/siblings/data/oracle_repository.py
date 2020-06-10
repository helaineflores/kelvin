from .indicators_repository import IndicatorsRepository
from siblings.environment import configuration as c
from datetime import datetime

import cx_Oracle as oracle


class OracleRepository(IndicatorsRepository):
    def __init__(self, logger):
        self._logger = logger
        try:
            configuration = c.Configuration()
            connection_string = configuration.connection_string
            self._connection = oracle.connect(connection_string)
        except Exception as ex:
            self._connection = None
            self._logger.error(ex)

    def __enter__(self):
        return self

    def save_usd_exchange_rate(self, usd):
        assert self._connection, 'Database connection is not established'

        time_period = usd['time_period']
        value = usd['value']

        try:
            cursor = self._connection.cursor()
            sql = 'INSERT INTO ACSELX.TASA_CAMBIO(CODMONEDA, FECHORACAMBIO, TASACAMBIO, CODUSR) ' + \
                  'VALUES(:1, :2, :3, :4)'
            cursor.execute(sql, ('DL', time_period, value, 'KELVIN'))
            self._connection.commit()
        except oracle.IntegrityError:
            message = f'USD exchange rate {value} for {time_period} is already in the database'
            self._logger.info(message)

    def close(self):
        if(self._connection):
            self._connection.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
