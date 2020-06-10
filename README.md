# Introduction 
Lord Kelvin once said: 'If you can't measure it, you can't control it'. That's why the 'medidores económicos' project is named 'Kelvin'. Basically, it gets the Banxico USD exchange rate to MXP and save it in an Oracle database.

# Unit Testing
From directory kelvin, run:
```
python3 -m unittest tests/banxico_parser.py
python3 -m unittest tests/indicators_processor.py
```
Note that that `python` depends on which version is installed and configured.
This project was developed and tested with Python 3.7.3.

>Banxico introduced a breaking change and the SOAP web service doesn't work anymore so the unit test banxico_service.py and the application itself breaks.

# Configuration and Environment
No configuration files have been uploaded to source control. That's a best practice. So, once the project has been `git cloned`, four YAML files must be created under the kelvin/siblings/environment folder:

1. config.yaml
2. development.config.yaml
3. staging.config.yaml
4. production.config.yaml

All of them have the same content and structure as shown below:

```
environment: name
database:
    connection_string: value
http_logging:
    url: value
```

Kelvin uses only `config.yaml`. When needed, its content is replaced with the content of any of the environment configuration file: `development.config.yaml`, `staging.config.yaml`, and `production.config.yaml`. Following is the files content used by Illyum:

## development.config.yaml
```
environment: development
database:
    connection_string: ADSOL/ADMIG08@135.35.1.248:1521/migra3
http_logging:
    url: https://not-used-for-development
```
## staging.config.yaml
```
environment: staging
database:
    connection_string: ADSOL/ADMIG08@135.35.1.248:1521/migra3
http_logging:
    url: https://logs-01.loggly.com/inputs/ff2ad657-b511-41d0-98a8-62e1d9c4e1ef/tag/kelvin/
```
## production.config.yaml
```
environment: production
database:
    connection_string: TBD
http_logging:
    url: TBD
```
Either manually or automatically (recommended as part of the build process), the `config.yaml` must be created with the proper configuration according to the environment. The `development.config.yaml`, `staging.config.yaml`, and `production.config.yaml` are supplied as examples.

## Dependency packages
Kelvin depends on the following packages which must be installed in the target environment through `pip` before running Kelvin:
```
pip install dependency-injector
pip install cx-Oracle
pip install PyYAML
pip install zeep
```
Es importante hacer notar que el paquete `cx-Oracle` requiere descargar, instalar y configurar `Oracle Instant Client` como se encuentra documentado en https://www.oracle.com/technetwork/database/database-technologies/instant-client/downloads/index.html.

## Calendarización del proceso Kelvin en Linux
Para ejecutar Kelvin de las 12:00 a las 16:00, de lunes a viernes se deberá usar la siguiente expresión `crontab`:
```
0 12-16 * * 1-5 python <path_to_Kelvin_folder>
```

Ejemplo: si Kelvin se instala en la ruta `/opt/Kelvin`, la expresión `crontab` será:

```
0 12-16 * * 1-5 python /opt/Kelvin
```
Se debe considerar:
1. La distribución de Linux para definir si se tiene que usar `cron` o `crontab`.
2. La versión de Python y el comando para ejecutar que depende de la instalación y configuración que se haya hecho en el servidor de producción: `python`, `python3`, `python3.6`, etc.
3. Tanto por configuración, por dependencias y velocidad de deployment, Illyum recomienda ampliamente usar Docker.