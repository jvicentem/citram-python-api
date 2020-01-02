import xmltodict
from zeep import Client

from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_municipalities():
    """
    Returns the municipalities that are in CRTM system with their ids.

    :return dict: A dictionary with the municipalities and ids. It looks like this:
    {
        'municipalities': {
            'Municipality': [{
                'codMunicipality': '4273',
                'name': 'ACEBEDA, LA'
            }, {
                'codMunicipality': '4274',
                'name': 'AJALVIR'
            }, {
                'codMunicipality': '4275',
                'name': 'ALAMEDA DEL VALLE'
            }, {
                'codMunicipality': '4276',
                'name': 'ÁLAMO, EL'
            }, {
                'codMunicipality': '4277',
                'name': 'ALCALÁ DE HENARES'
            }, {
                'codMunicipality': '4278',
                'name': 'ALCOBENDAS'
            },
            ...
            ]
        }
    }
    """
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value + '/GetMunicipalities.php')

    return common_request(url_formatted)


def get_ttp_card_info(ttp_number):
    """
    Get information from the specified transport card number.

    The number is the concatenation of the last 3 numbers of the first row and all the numbers of the second row.
    See this image: https://tarjetatransportepublico.crtm.es/CRTM-ABONOS/archivos/img/TTP.jpg

    :param str ttp_number: The number that identifies a transport card. It must be a string of the last 3 numbers
    of the first row and all the numbers of the second row.
    :return dict: A dictionary with information of the transport card. It has information regarding the titles
    in that card, expiring dates, purchase dates, title types (young, normal, old, ...), among others.
    """
    if ttp_number is not None:
        client = Client(Urls.CITRAM_CARD_SERVICE.value)
        result = client.service.ConsultaSaldo1(sNumeroTTP=ttp_number)
    else:
        raise NotEnoughParametersException('You must specify a transport card number.')

    final_result = {'status': result['iCallLogField'],
                    'card_info': xmltodict(result['sResulXMLField'])}

    return final_result


def get_transport_modes():
    """
    Returns the transport modes available and their id.

    :return dict: Transport modes and their ids. The result looks like this:
    {
        'modes': {
            'Mode': [{
                'codMode': '4',
                'name': 'METRO'
            }, {
                'codMode': '6',
                'name': 'AUTOBUSES EMT'
            }, {
                'codMode': '5',
                'name': 'CERCANIAS'
            }, {
                'codMode': '10',
                'name': 'METRO LIGERO/TRANVÍA'
            }, {
                'codMode': '8',
                'name': 'AUTOBUSES INTERURBANOS'
            }, {
                'codMode': '9',
                'name': 'AUTOBUSES URBANOS OTROS MUNICIPIOS'
            }, {
                'codMode': '90',
                'name': 'INTERCAMBIADORES'
            }, {
                'codMode': '0',
                'name': 'LARGO RECORRIDO'
            }, {
                'codMode': '1',
                'name': 'APARCAMIENTOS'
            }]
        }
    }
    """
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value + '/GetModes.php')

    return common_request(url_formatted)
