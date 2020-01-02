from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_lines_by_mode(mode_cod):
    """
    Get transport lines of a transport mode given a transport mode id.

    You can use constants.TransportModes to get the available transport modes ids.

    Example: get_lines_by_mode(TransportModes.CERCANIAS.value)

    :param int mode_cod: Id of a public transport. Use constants.TransportModes to easily select transport modes ids.
    :return dict: Lines of the transport specified. The returned dictionary look likes the following example:
    {
        'lines': {
            'Line': [{
                'codLine': '5__C1___',
                'shortDescription': 'C1',
                'description': 'P.Pío-Atocha-Recoletos-Chamartín-Aeropuerto T4',
                'codMode': '5',
                'updateDate': '2019-11-19T14:30:28+01:00',
                'updateKmlDate': '2019-11-19T14:25:06+01:00',
                'nightService': 0,
                'active': True,
                'shortItinerary': {
                    'Itinerary': [{
                        'codItinerary': '5__C1____1__IT_1',
                        'name': 'P.Pío-Atocha-Recoletos-Chamartín-Aeropuerto T4',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20191119_1425/cercaniaskmz/M5_LC-1_S1_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '5__C1____2__IT_1',
                        'name': 'Aeropuerto T4-Chamartín-Recoletos-Atocha-P.Pío',
                        'direction': 2,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20191119_1425/cercaniaskmz/M5_LC-1_S2_TRAMO.kmz',
                        'stops': {}
                    }]
                },
                'URLLine': 'http://www.crtm.es/tu-transporte-publico/cercanias-renfe/lineas/5__1___.aspx',
                'colorLine': '#4FB0E5',
                'text_colorLine': '#FFFFFF',
                'companyCode': '301'
            },
            ...
            ]
        }
    }
    """
    if mode_cod is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetLines.php?mode={mode}'
                         .format(mode=str(mode_cod)))
    else:
        raise NotEnoughParametersException('You must specify a transport mode.')

    return common_request(url_formatted)


def get_lines_by_municipality(cod_municipality, cod_mode=None):
    """
    Get transport lines of a transport mode given a municipality id.

    You can use constants.Municipalities to get the available municipalities ids.

    Example: get_lines_by_municipality(Municipalities.FUENLABRADA.value)

    :param int cod_municipality: Id of a municipality. Use constants.Municipalities to easily select transport modes ids.
    :param int cod_mode: If specified, the results will be filtered, returning only lines of that transport mode.
                         Optional, default: None (No transport mode filtering).
    :return dict: Lines of the municipality specified. The returned dictionary look likes the following example:
    {
        'lines': {
            'Line': [{
                'codLine': '4__12___',
                'shortDescription': '12',
                'description': 'MetroSur',
                'codMode': '4',
                'updateDate': '2019-03-22T17:21:37+01:00',
                'updateKmlDate': '2016-06-01T17:04:00+02:00',
                'nightService': 0,
                'active': True,
                'shortItinerary': {
                    'Itinerary': [{
                        'codItinerary': '4__12____1__IT_1',
                        'name': 'METROSUR (ANDEN-1)',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L12-1_S1_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '4__12____2__IT_1',
                        'name': 'METROSUR (ANDEN-2)',
                        'direction': 2,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L12-2_S1_TRAMO.kmz',
                        'stops': {}
                    }]
                },
                'URLLine': 'http://www.crtm.es/tu-transporte-publico/metro/lineas/4__12___.aspx',
                'colorLine': '#A49800',
                'text_colorLine': '#FFFFFF',
                'companyCode': '200'
            }, {
                'codLine': '5__C5___',
                'shortDescription': 'C5',
                'description': 'Móstoles-El Soto-Atocha-Fuenlabrada-Humanes',
                'codMode': '5',
                'updateDate': '2019-11-19T14:30:28+01:00',
                'updateKmlDate': '2019-11-19T14:25:06+01:00',
                'nightService': 0,
                'active': True,
                'shortItinerary': {
                    'Itinerary': [{
                        'codItinerary': '5__C5____1__IT_1',
                        'name': 'Móstoles El Soto-Atocha-Fuenlabrada-Humanes',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20191119_1425/cercaniaskmz/M5_LC-5_S1_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '5__C5____2__IT_1',
                        'name': 'Humanes-Fuenlabrada-Atocha-Móstoles El Soto',
                        'direction': 2,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20191119_1425/cercaniaskmz/M5_LC-5_S2_TRAMO.kmz',
                        'stops': {}
                    }]
                },
                'URLLine': 'http://www.crtm.es/tu-transporte-publico/cercanias-renfe/lineas/5__5___.aspx',
                'colorLine': '#F9BA13',
                'text_colorLine': '#FFFFFF',
                'companyCode': '301'
            }, {
                'codLine': '8__455___',
                'shortDescription': '455',
                'description': '455-PINTO - GETAFE',
                'codMode': '8',
                'updateDate': '2018-05-10T15:25:50+02:00',
                'updateKmlDate': '2016-06-01T17:04:00+02:00',
                'nightService': 0,
                'active': True,
                'shortItinerary': {
                    'Itinerary': [{
                        'codItinerary': '8__455____1_-_IT_1',
                        'name': '455 GETAFE',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/interurbanoskmz/M8_L455_S1_obs[-]_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '8__455____1_a._IT_2',
                        'name': '455 GETAFE',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/interurbanoskmz/M8_L455_S1_obs[a.]_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '8__455____1_am_IT_2',
                        'name': 'Hasta ambulatorio de Getafe',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/interurbanoskmz/M8_L455_S1_obs[am]_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '8__455____1_h._IT_2',
                        'name': 'Hasta/desde hospital de Getafe',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/interurbanoskmz/M8_L455_S1_obs[h.]_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '8__455____2_h._IT_2',
                        'name': 'Hasta/desde hospital de Getafe',
                        'direction': 2,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/interurbanoskmz/M8_L455_S2_obs[h.]_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '8__455____2_jc_IT_2',
                        'name': 'Desde Avda. Juan de la Cierva, 28',
                        'direction': 2,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/interurbanoskmz/M8_L455_S2_obs[jc]_TRAMO.kmz',
                        'stops': {}
                    }]
                },
                'URLLine': 'http://www.crtm.es/tu-transporte-publico/autobuses-interurbanos/lineas/8__455___.aspx',
                'colorLine': '#8EBF42',
                'text_colorLine': '#FFFFFF',
                'companyCode': '078'
            },
            ...
            ]
        }
    }
    """
    if cod_municipality is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetLines.php?codMunicipality={codMunicipality}'
                         .format(codMunicipality=str(cod_municipality)))

        if cod_mode is not None:
            url_formatted = url_formatted + '&mode={mode}'.format(mode=cod_mode)
    else:
        raise NotEnoughParametersException('You must specify a municipality code.')

    return common_request(url_formatted)


def get_lines_by_line_code(cod_line):
    """
    Returns the line specified. This method results in a brief description of the line.

    Example: get_lines_by_line_code(create_line_cod(TransportModes.METRO.value, 10))

    :param str cod_line: Line id. Use utils.create_line_cod to create this id easily.
    :return: The line of the line id specified. The returned dictionary look likes the following example:

    {
        'lines': {
            'Line': {
                'codLine': '4__10___',
                'shortDescription': '10',
                'description': 'Hospital del Norte-Puerta del Sur',
                'codMode': '4',
                'updateDate': '2019-03-22T17:21:37+01:00',
                'updateKmlDate': '2016-06-01T17:04:00+02:00',
                'nightService': 0,
                'active': True,
                'shortItinerary': {
                    'Itinerary': [{
                        'codItinerary': '4__10____1__IT_1',
                        'name': 'Hospital del Norte - Puerta del Sur',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L10a_S1_TRAMO.kmz#http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L10b_S1_TRAMO.kmz',
                        'stops': {}
                    }, {
                        'codItinerary': '4__10____2__IT_1',
                        'name': 'Puerta del Sur - Hospital del Norte',
                        'direction': 2,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L10a_S2_TRAMO.kmz#http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L10b_S2_TRAMO.kmz',
                        'stops': {}
                    }]
                },
                'URLLine': 'http://www.crtm.es/tu-transporte-publico/metro/lineas/4__10___.aspx',
                'colorLine': '#005AA9',
                'text_colorLine': '#FFFFFF',
                'companyCode': '200'
            }
        }
    }

    """
    if cod_line is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetLines.php?codLine={codLine}'
                         .format(codLine=str(cod_line)))
    else:
        raise NotEnoughParametersException('You must specify a line code.')

    return common_request(url_formatted)


def get_line_info(cod_line):
    """
    Returns line information from the line id specified.

    Example: get_line_info(create_line_cod(TransportModes.METRO.value, 10))

    :param str cod_line: Line id. Use utils.create_line_cod to create this id easily.
    :return: Info of the line id specified. The returned dictionary look likes the following example:
    {
        'lines': {
            'LineInformation': {
                'codLine': '4__10___',
                'shortDescription': '10',
                'description': 'Hospital del Norte-Puerta del Sur',
                'codMode': '4',
                'codMunicipalities': {
                    'string': ['4278', '4279', '4350', '4401']
                },
                'itinerary': {
                    'Itinerary': [{
                        'codItinerary': '4__10____1__IT_1',
                        'name': 'Hospital del Norte - Puerta del Sur',
                        'direction': 1,
                        'kml': 'http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L10a_S1_TRAMO.kmz#http://www.citram.es:8080/kml/itinerarios/20160601_1704/metrokmz/M4_L10b_S1_TRAMO.kmz',
                        'stops': {
                            'StopInformation': [{
                                'codStop': '4_284',
                                'shortCodStop': '',
                                'codMode': '4',
                                'name': 'HOSPITAL INFANTA SOFÍA',
                                'address': 'Paseo  Europa SN ',
                                'postCode': '',
                                'codMunicipality': '4401',
                                'coordinates': {
                                    'longitude': -3.61145,
                                    'latitude': 40.55977
                                },
                                'lines': {
                                    'Line': {
                                        'codLine': '4__10___',
                                        'shortDescription': '10',
                                        'description': 'Hospital del Norte-Puerta del Sur',
                                        'codMode': '4',
                                        'updateDate': '2019-03-22T17:21:37+01:00',
                                        'updateKmlDate': '2016-06-01T17:04:00+02:00',
                                        'nightService': 0,
                                        'active': True,
                                        'shortItinerary': {},
                                        'companyCode': ''
                                    }
                                },
                                'access': 0,
                                'park': 0,
                                'nightLinesService': 0
                            },
                            ...
                },
                'updateDate': '2019-03-22T17:21:37+01:00',
                'updateKmlDate': '2016-06-01T17:04:00+02:00',
                'nightService': 0,
                'lineTimePlanning': {
                    'codLine': '4__10___',
                    'codItinerary': '',
                    'type': '',
                    'startService': '',
                    'endService': '',
                    'updateDate': '0001-01-01T00:00:00'
                }
            }
        }
    }
    """
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetLinesInformation.php?activeItinerary=1&codLine={codLine}'
                     .format(codLine=cod_line))

    return common_request(url_formatted)


def get_lines_timeplanning(cod_line):
    """
    Timeplanning of the specified line id.

    Example: get_lines_timeplanning(create_line_cod(TransportModes.METRO.value, 10))

    :param str cod_line: Line id. Use utils.create_line_cod to create this id easily.
    :return: Timeplanning of the line id specified.
    """
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetLinesTimePlanning.php?activeItinerary=1&codLine={codLine}'
                     .format(codLine=cod_line))

    return common_request(url_formatted)


def get_line_location(mode_cod, cod_itinerary, cod_line, cod_stop, direction):
    """
    It returns the location of that line at the moment the request is performed. (i.e. Location of a bus of that line
    right now).

    Example:
    >>> line = get_line_info(create_line_cod(TransportModes.METRO.value, 10))['lines']['LineInformation']
    >>> get_line_location(int(line['codMode']),
    >>>                   line['itinerary']['Itinerary'][0]['codItinerary'],
    >>>                   line['codLine'],
    >>>                   line['itinerary']['Itinerary'][0]['stops']['StopInformation'][0]['codStop'],
    >>>                   line['itinerary']['Itinerary'][0]['direction'])

    :param int mode_cod: Id of a public transport. Use constants.TransportModes to easily select transport modes ids.
    :param int cod_itinerary: Itinerary of that line.
    :param str cod_line: Line id. Use utils.create_line_cod to create this id easily.
    :param str cod_stop: Stop id. In this case this is needed as a formality. Any stop of that line gives the same
                                  result.
    :param int direction: Direction of a itinerary.
    :return:
    """

    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetLineLocation.php?mode={mode}&codItinerary={codItinerary}&codLine={codLine}&codStop={codStop}&direction={direction}'
                     .format(mode=str(mode_cod), codItinerary=cod_itinerary, codLine=cod_line, codStop=cod_stop,
                             direction=str(direction)))

    return common_request(url_formatted)


def get_incidents_affectations(mode_cod, cod_line):
    """
    Returns incidents happening at the specified line.

    Example: get_incidents_affectations(TransportModes.METRO.value, create_line_cod(TransportModes.METRO.value, 10))

    :param int mode_cod: Id of a public transport. Use constants.TransportModes to easily select transport modes ids.
    :param str cod_line: Line id. Use utils.create_line_cod to create this id easily.
    :return dict: The current incidents going on in that line.
    """
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetIncidentsAffectations.php?mode={mode}&codLine={codLine}'
                     .format(mode=str(mode_cod), codLine=cod_line))

    return common_request(url_formatted)
