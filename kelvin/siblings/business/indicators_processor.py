class IndicatorsProcessor(object):
    def __init__(self, service, repository, logger):
        self._service = service
        self._repository = repository
        self._logger = logger

    def __enter__(self):
        return self

    def execute(self):
        try:
            self._logger.info('Kelvin processor started...')
            exchange_rates = self._service.get_exchange_rates()
            usd = self.usd_from(exchange_rates)
            if(usd):
                self._repository.save_usd_exchange_rate(usd)
        except Exception as ex:
            self._logger.error(ex)
        finally:
            self._logger.info('Kelvin processor finished...')

    def usd_from(self, exchange_rates):
        for title, _, time_period, value in exchange_rates:
            if('(FIX)' in title):
                return {'time_period': time_period, 'value': value}

    def close(self):
        if(self._service):
            self._service.close()

        if(self._repository):
            self._repository.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
