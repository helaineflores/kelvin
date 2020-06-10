from yaml import load


class Configuration(object):
    class __Configuration:
        def __init__(self, filepath):
            with open(filepath, 'r') as file:
                self._configuration = load(file)

        @property
        def environment(self):
            return self._configuration['environment']

        @property
        def connection_string(self):
            section = self._configuration['database']
            return section['connection_string']
        
        @property
        def http_logging_url(self):
            section = self._configuration['http_logging']
            return section['url']

    instance = None

    def __new__(cls, filepath = 'kelvin/siblings/environment/config.yaml'):
        if(not Configuration.instance):
            Configuration.instance = Configuration.__Configuration(filepath)
        return Configuration.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, val):
        return super().__setattr__(name, val)
