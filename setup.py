from distutils.core import setup

setup(
    name='Kelvin',
    version='BetaI',
    packages=[
        'kelvin',
        'kelvin.siblings',
        'kelvin.siblings.business',
        'kelvin.siblings.data',
        'kelvin.siblings.environment',
        'kelvin.siblings.operations'
    ],
    author='Francisco Javier Banos Lemoine',
    author_email='franl@illyum.com',
    description='USD-MXP exchange rate: from Banxico WS to Oracle DB',
    license='Illyum',
    keywords='Kelvin Banxico indicadores USD MXP tipo de cambio'
)
