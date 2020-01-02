from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_offices_by_type(offices_type):
    """
    Returns all the offices of the specified type.

    Example: get_offices_by_type(OfficeTypes.OFICINA.value)

    :param str offices_type: Office type. Use constants.OfficeTypes to choose the available types easily.
    :return dict: A dictionary with a list of offices of the specified type.
    {
        'offices': {
            'Office': [{
                'codOffice': '01_000015',
                'name': 'Oficina de Gestión del Consorcio Regional de Transportes de Madrid',
                'address': 'Plaza Descubridor Diego de Ordás, 3. 28003 Madrid',
                'openTime': 'Horario de atención al público: Lunes a Viernes de 8 a 20 h',
                'coordinates': {
                    'longitude': -3.700064,
                    'latitude': 40.44086
                },
                'type': 'gestion'
            }, {
                'codOffice': '01_000020',
                'name': 'Oficina de Gestión de Moncloa',
                'address': 'Plaza de la Moncloa, 1. 28008 Madrid',
                'openTime': 'Horario de atención al público: Lunes a viernes de 7 a 22 h: Sábados y domingos de 10 a 22 h',
                'coordinates': {
                    'longitude': -3.719445,
                    'latitude': 40.43502
                },
                'type': 'gestion'
            }, {
                'codOffice': '01_000025',
                'name': 'Oficina de Gestión de Sol',
                'address': 'Plaza de la Puerta del Sol, 6. 28013 Madrid',
                'openTime': 'Horario de atención al público: Lunes a viernes de 7 a 22 h; Sábados y domingos de 10 a 22 h',
                'coordinates': {
                    'longitude': -3.703257,
                    'latitude': 40.416877
                },
                'type': 'gestion'
            }, {
                'codOffice': '01_000030',
                'name': 'Oficina de Gestión de Príncipe Pío',
                'address': 'Paseo de la Florida, 2. 28008 Madrid',
                'openTime': 'Horario de atención al público: Lunes a viernes de 7 a 22 h; Sábados de 10 a 22 h',
                'coordinates': {
                    'longitude': -3.720322,
                    'latitude': 40.421069
                },
                'type': 'gestion'
            },
            ...
            }]
        }
    }
    """
    if offices_type is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?type={offices_type}'
                         .format(offices_type=str(offices_type)))
    else:
        raise NotEnoughParametersException('You must specify an office type.')

    return common_request(url_formatted)


def get_offices_by_postcode(post_code, offices_type=None):
    """

    Returns all the offices from the specified zip code. If offices_type is specified, the results will be filtered,
    returning only offices of that type.

    Example: get_offices_by_postcode(28004)

    :param int post_code: Zip code of the area to look for offices.
    :param str offices_type: Office type. If set, filters the results by the office type specified.
                             Use constants.OfficeTypes to choose the available types easily.
                             Optional, default: None (no filtering).
    :return dict: A dictionary with a list of offices from the zip code specified.
    """
    if post_code is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?postcode={postcode}'
                         .format(postcode=str(post_code)))
        if offices_type is not None:
            url_formatted = url_formatted + '&type={offices_type}'.format(offices_type=str(offices_type))
    else:
        raise NotEnoughParametersException('You must specify a zip code.')

    return common_request(url_formatted)


def get_offices_by_municipality(cod_municipality, offices_type=None):
    """
    Returns all the offices from the specified municipality. If offices_type is specified, the results will be filtered,
    returning only offices of that type.

    Example: get_offices_by_municipality(Municipalities.FUENLABRADA.value, OfficeTypes.OFICINA.value)

    :param int cod_municipality: Id of a municipality. Use constants.Municipalities to easily select transport modes ids.
    :param str offices_type: Office type. If set, filters the results by the office type specified.
                             Use constants.OfficeTypes to choose the available types easily.
                             Optional, default: None (no filtering).
    :return dict: A dictionary with a list of offices in that municipality.
    """
    if cod_municipality is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?codmunicipality={codmunicipality}'
                         .format(codmunicipality=str(cod_municipality)))
        if offices_type is not None:
            url_formatted = url_formatted + '&type={offices_type}'.format(offices_type=str(offices_type))
    else:
        raise NotEnoughParametersException('You must specify a municipality code.')

    return common_request(url_formatted)
