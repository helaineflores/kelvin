from xml.etree import ElementTree
from datetime import datetime


XMLNS = {'bm': 'http://www.banxico.org.mx/structure/key_families/dgie/sie/series/compact'}
SERIES_XPATH = 'bm:DataSet/bm:Series'
OBS_XPATH = 'bm:Obs'


class BanxicoParser(object):
    def parse(self, xml):
        assert xml, 'No XML document has been supplied'

        root = ElementTree.fromstring(xml)
        series = root.findall(SERIES_XPATH, XMLNS)
        for serie in series:
            obs = serie.find(OBS_XPATH, XMLNS)
            if obs.attrib['OBS_VALUE'] != 'N/E':
                title = serie.attrib['TITULO']
                id_serie = serie.attrib['IDSERIE']
                time_period = datetime.strptime(
                    obs.attrib['TIME_PERIOD'], '%Y-%m-%d')
                value = float(obs.attrib['OBS_VALUE'])
                yield (title, id_serie, time_period.date(), value)
