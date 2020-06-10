from siblings.data import banxico_service as bs
from siblings.data import banxico_parser as bp
from siblings.data import oracle_repository as ar
from siblings.operations import logger
from siblings.operations import http_logger as hl
from siblings.operations import print_logger as pl
from siblings.environment import configuration as c
from siblings.business import indicators_processor as ip
from dependency_injector import containers, providers


class Loggers(containers.DeclarativeContainer):
    environment = c.Configuration().environment
    if(environment == 'development'):
        logger = providers.Factory(pl.PrintLogger)
    else:
        logger = providers.Factory(hl.HttpLogger)

class Services(containers.DeclarativeContainer):
    indicators = providers.Factory(
        bs.BanxicoService,
        logger=Loggers.logger
    )

class Repositories(containers.DeclarativeContainer):
    indicators = providers.Factory(
        ar.OracleRepository,
        logger=Loggers.logger
    )

class Processors(containers.DeclarativeContainer):
    indicators = providers.Factory(
        ip.IndicatorsProcessor,
        service=Services.indicators,
        repository=Repositories.indicators,
        logger=Loggers.logger
    )


def main():
    with Processors.indicators() as processor:
        processor.execute()


if __name__ == '__main__':
    main()
