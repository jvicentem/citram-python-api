import requests

from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_stops_by_cod_stop(cod_stop):
    """
    It returns the stop specified by a stop id. This method results in a brief description of the stop.

    You can create a cod_stop easily by using utils.create_cod_stop.

    .. code-block:: python   
        
        get_stops_by_cod_stop(create_stop_cod(TransportModes.METRO.value, 276))

    :param str cod_stop: Stop id. You can create a cod_stop easily by using utils.create_cod_stop.
    :return dict: Short description of stop. It looks like this:

    .. code-block:: python   
        
        {
            'stops': {
                'Stop': {
                    'codStop': '4_276',
                    'shortCodStop': '276',
                    'codMode': '4',
                    'name': 'LAS TABLAS',
                    'address': 'Calle de Palas de Rey 48 ',
                    'postCode': '28050',
                    'codMunicipality': '4350',
                    'coordinates': {
                        'longitude': -3.66944,
                        'latitude': 40.50833
                    },
                    'codLines': {
                        'Line': ['4__10___', '10__ML1___']
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }
            }
        }
    """
    if cod_stop is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?codStop={codStop}'
                         .format(codStop=cod_stop))
    else:
        raise NotEnoughParametersException('You must specify a stop code.')

    return common_request(url_formatted)


def get_stops_by_custom_search(custom_search):
    """
    It returns stops based on the custom search string specified.

    Example: 

    .. code-block:: python   
            
        get_stops_by_custom_search('tres aguas')

    :param str custom_search: Custom search string.
    :return dict: A dictionary of the stops that match your search. The result looks like this:

    .. code-block:: python   
            
        {
            'stops': {
                'Stop': [{
                    'codStop': '8_08469',
                    'shortCodStop': '08469',
                    'codMode': '8',
                    'name': 'AV.S.MARTÍN VALDEIGLESIAS-C.C.TRES AGUAS',
                    'address': 'AV.S.MARTÍN VALDEIGLESIAS-C.C.TRES AGUAS',
                    'postCode': '28925',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.8321874141693,
                        'latitude': 40.357341766357
                    },
                    'codLines': {
                        'Line': ['8__510___', '8__510_A__', '8__518___', '8__551___', '8__581___', '8_N_504___', '9__3__007_']
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 1,
                    'stopType': 0
                }, {
                    'codStop': '8_09364',
                    'shortCodStop': '09364',
                    'codMode': '8',
                    'name': 'ARGENTINA-C.C.TRES AGUAS',
                    'address': 'ARGENTINA-C.C.TRES AGUAS',
                    'postCode': '28922',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.8295669555664,
                        'latitude': 40.355888366699
                    },
                    'codLines': {
                        'Line': ['8__510___', '8__510_A__', '8__518___', '8__551___', '8__581___', '8_N_504___', '9__3__007_']
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 1,
                    'stopType': 0
                }]
            }
        }
    """
    if custom_search is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?customSearch={customSearch}'
                         .format(customSearch=custom_search))
    else:
        raise NotEnoughParametersException('Introduce a valid string as a search.')

    return common_request(url_formatted)


def get_stops_by_zip_code(postcode):
    """
    It returns the stops that belong to a zip code.

    Example: 
    
    .. code-block:: python   
            
        get_stops_by_zip_code(28922)

    :param int postcode: Zip code from where the stops are going to be retrieved.
    :return dict: Stops that belong to the zip code specified. The result looks like this:

    .. code-block:: python   
            
        {
            'stops': {
                'Stop': [{
                    'codStop': '4_211',
                    'shortCodStop': '211',
                    'codMode': '4',
                    'name': 'ALCORCON CENTRAL',
                    'address': 'Avda de Móstoles 12 ',
                    'postCode': '28922',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.83178,
                        'latitude': 40.35008
                    },
                    'codLines': {
                        'Line': ['4__12___', '5__C5___']
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }, {
                    'codStop': '4_212',
                    'shortCodStop': '212',
                    'codMode': '4',
                    'name': 'PARQUE OESTE',
                    'address': 'Calle de Estambul 5 ',
                    'postCode': '28922',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.84934,
                        'latitude': 40.34589
                    },
                    'codLines': {
                        'Line': '4__12___'
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }, {
                    'codStop': '5_5',
                    'shortCodStop': '5',
                    'codMode': '5',
                    'name': 'ALCORCON',
                    'address': 'ALCORCON',
                    'postCode': '28922',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.8316340093152,
                        'latitude': 40.35008820867
                    },
                    'codLines': {
                        'Line': ['4__12___', '5__C5___']
                    },
                    'access': 1,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }, {
                    'codStop': '5_66',
                    'shortCodStop': '66',
                    'codMode': '5',
                    'name': 'RETAMAS, LAS',
                    'address': 'RETAMAS, LAS',
                    'postCode': '28922',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.8423299815775,
                        'latitude': 40.341902701431
                    },
                    'codLines': {
                        'Line': '5__C5___'
                    },
                    'access': 1,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }, {
                    'codStop': '8_08434',
                    'shortCodStop': '08434',
                    'codMode': '8',
                    'name': 'AV.MÓSTOLES-VIVERO',
                    'address': 'AV.MÓSTOLES-VIVERO',
                    'postCode': '28922',
                    'codMunicipality': '4279',
                    'coordinates': {
                        'longitude': -3.8468658924103,
                        'latitude': 40.337970733643
                    },
                    'codLines': {
                        'Line': ['8__520___', '8_N_501___']
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 1,
                    'stopType': 0
                },
                ...
                ]
            }
        }
    """
    if postcode is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?postcode={postcode}'
                         .format(postcode=postcode))
    else:
        raise NotEnoughParametersException('You must specify a zip code.')

    res = requests.get(url_formatted)

    return res.json()


def get_stops_by_municipality(cod_municipality):
    """
    It returns the stops that belong to the specified municipality.

    You can use constants.Municipalities to get the available municipalities ids.

    Example: 

    .. code-block:: python   
            
        get_stops_by_municipality(Municipalities.FUENLABRADA.value)

    :param int cod_municipality: Id of a municipality. Use constants.Municipalities to easily select transport modes ids.
    :return dict: Stops that belong to the municipality specified. The result looks like this:

    .. code-block:: python   
            
        {
            'stops': {
                'Stop': [{
                    'codStop': '4_218',
                    'shortCodStop': '218',
                    'codMode': '4',
                    'name': 'LORANCA',
                    'address': 'Calle de la Alegría SN ',
                    'postCode': '28942',
                    'codMunicipality': '4330',
                    'coordinates': {
                        'longitude': -3.83768,
                        'latitude': 40.29681
                    },
                    'codLines': {
                        'Line': '4__12___'
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }, {
                    'codStop': '4_219',
                    'shortCodStop': '219',
                    'codMode': '4',
                    'name': 'HOSPITAL DE FUENLABRADA',
                    'address': 'Cmno del Molino SN ',
                    'postCode': '28942',
                    'codMunicipality': '4330',
                    'coordinates': {
                        'longitude': -3.81642,
                        'latitude': 40.28576
                    },
                    'codLines': {
                        'Line': '4__12___'
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                },
                ...
                ]
            }
        }
    """
    if cod_municipality is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?codMunicipality={codMunicipality}'
                         .format(codMunicipality=cod_municipality))
    else:
        raise NotEnoughParametersException('You must specify a municipality code.')

    res = requests.get(url_formatted)

    return res.json()


def get_stop_info(cod_stop):
    """
    Returns detailed information about the specified stop.

    You can create a cod_stop easily by using utils.create_cod_stop.

    Example:

    .. code-block:: python   
            
        get_stop_info(create_stop_cod(TransportModes.METRO.value, 276))

    :param str cod_stop: Stop id. You can create a cod_stop easily by using utils.create_cod_stop.
    :return dict: Detailed information about the specified stop. The result looks like this:

    .. code-block:: python   
                
        {
            'stops': {
                'Stop': {
                    'codStop': '4_276',
                    'shortCodStop': '276',
                    'codMode': '4',
                    'name': 'LAS TABLAS',
                    'address': 'Calle de Palas de Rey 48 ',
                    'postCode': '28050',
                    'codMunicipality': '4350',
                    'coordinates': {
                        'longitude': -3.66944,
                        'latitude': 40.50833
                    },
                    'codLines': {
                        'Line': ['4__10___', '10__ML1___']
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0,
                    'stopType': 0
                }
            }
        }
    """
    if cod_stop is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?codStop={codStop}'
                         .format(codStop=cod_stop))
    else:
        raise NotEnoughParametersException('You must specify a stop code.')

    res = requests.get(url_formatted)

    return res.json()


def get_stop_times(cod_stop, stop_type, stop_times_by_iti, order_by=2):
    """
    Get the stop times for the stop and line itinerary specified.

    You can create a cod_stop easily by using utils.create_cod_stop.

    .. code-block:: python   
        
        stop = get_stop_info(create_stop_cod(TransportModes.METRO.value, 276))
        line = get_line_info(stop['stops']['Stop']['codLines']['Line'][0])['lines']['LineInformation']
        get_stop_times(stop['stops']['Stop']['codStop'],
                       stop['stops']['Stop']['stopType'],
                       stop['stops']['Stop']['codStop'],
                       line['itinerary']['Itinerary'][0]['codItinerary'])

    :param str cod_stop: Stop id. You can create a cod_stop easily by using utils.create_cod_stop.
    :param str stop_type: Stop type number. Unfortunately, we don't have information of what type of stop each number
    represents, so the easiest thing is to get it from the stop info.
    :param str stop_times_by_iti: Itinerary name.
    :param int order_by: Rule to sort results. Optional, 2 by default. Unfortunately, we don't know what numbers
    correspond to what order criteria, so the default value is provided by default.
    :return dict: A dictionary with the times of the itinerary for that stop.

    .. code-block:: python   
        
        {
            'stopTimes': {
                'actualDate': '2020-01-02T01:35:27+01:00',
                'stop': {
                    'codStop': '4_276',
                    'shortCodStop': '276',
                    'name': 'LAS TABLAS',
                    'park': 0,
                    'nightLinesService': 0
                },
                'times': {
                    'Time': [{
                        'line': {
                            'codLine': '4__10___',
                            'shortDescription': '10',
                            'description': '10-Hospital del Norte-Puerta del Sur',
                            'codMode': '4',
                            'updateDate': '2019-03-22T17:21:37+01:00',
                            'updateKmlDate': '2016-06-01T17:04:00+02:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        },
                        'direction': 1,
                        'destination': 'PUERTA DEL SUR',
                        'destinationStop': {
                            'codStop': '4_205',
                            'shortCodStop': '205',
                            'name': 'PUERTA DEL SUR',
                            'park': 0,
                            'nightLinesService': 0
                        },
                        'time': '2020-01-02T01:48:39+01:00',
                        'codVehicle': '',
                        'codIssue': ''
                    }, {
                        'line': {
                            'codLine': '4__10___',
                            'shortDescription': '10',
                            'description': '10-Hospital del Norte-Puerta del Sur',
                            'codMode': '4',
                            'updateDate': '2019-03-22T17:21:37+01:00',
                            'updateKmlDate': '2016-06-01T17:04:00+02:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        },
                        'direction': 1,
                        'destination': 'PUERTA DEL SUR',
                        'destinationStop': {
                            'codStop': '4_205',
                            'shortCodStop': '205',
                            'name': 'PUERTA DEL SUR',
                            'park': 0,
                            'nightLinesService': 0
                        },
                        'time': '2020-01-02T01:48:39+01:00',
                        'codVehicle': '',
                        'codIssue': ''
                    }, {
                        'line': {
                            'codLine': '4__10___',
                            'shortDescription': '10',
                            'description': '10-Hospital del Norte-Puerta del Sur',
                            'codMode': '4',
                            'updateDate': '2019-03-22T17:21:37+01:00',
                            'updateKmlDate': '2016-06-01T17:04:00+02:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        },
                        'direction': 1,
                        'destination': 'PUERTA DEL SUR',
                        'destinationStop': {
                            'codStop': '4_205',
                            'shortCodStop': '205',
                            'name': 'PUERTA DEL SUR',
                            'park': 0,
                            'nightLinesService': 0
                        },
                        'time': '2020-01-02T01:49:39+01:00',
                        'codVehicle': '',
                        'codIssue': ''
                    }]
                },
                'linesStatus': {
                    'LineStatus': {
                        'line': {
                            'codLine': '4__10___',
                            'shortDescription': '10'
                        },
                        'SAEStatus': True
                    }
                }
            }
        }
    """
    if cod_stop is not None and stop_type is not None and order_by is not None and stop_times_by_iti is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStopsTimes.php?codStop={codStop}&type={stop_type}&orderBy={orderBy}&stopTimesByIti={stopTimesByIti}'
                         .format(codStop=cod_stop, stop_type=stop_type,
                                 orderBy=order_by, stopTimesByIti=stop_times_by_iti))
    else:
        raise NotEnoughParametersException('You must specify all the needed parameters.')

    res = requests.get(url_formatted)

    return res.json()


def get_nearest_stops(latitude, longitude, distance, method=2):
    """
    Retrieves the stops within a distance given a set of coordinates.

    Example: 

    .. code-block:: python   
            
        get_nearest_stops(40.453053, -3.688344, 500.0)

    :param float latitude: Latitude.
    :param float longitude: Longitude.
    :param float distance: Distance from the point specified to find stops.
    :param int method: Method to find stops. Unfortunately we don't know what method each value represents, so
    by default the value of 2 is provided.
    :return dict: Dictionary with stops within the distance of the location provided. The result looks like this:

    .. code-block:: python   
            
        {
            'stops': {
                'Stop': [{
                    'codStop': '6_36',
                    'shortCodStop': '36',
                    'codMode': '6',
                    'name': 'Castellana-San Germán',
                    'address': 'Pº de la Castellana, 113',
                    'postCode': '',
                    'codMunicipality': '4350',
                    'coordinates': {
                        'longitude': -3.6904863648497,
                        'latitude': 40.456610013049
                    },
                    'lines': {
                        'Line': [{
                            'codLine': '6__5___',
                            'shortDescription': '5',
                            'description': '5-SOL/SEVILLA-CHAMARTIN',
                            'codMode': '6',
                            'updateDate': '2017-11-08T12:43:20+01:00',
                            'updateKmlDate': '2017-11-08T12:37:23+01:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }, {
                            'codLine': '6__27___',
                            'shortDescription': '27',
                            'description': '27-EMBAJADORES-PLAZA CASTILLA',
                            'codMode': '6',
                            'updateDate': '2017-11-08T12:43:20+01:00',
                            'updateKmlDate': '2017-11-08T12:37:23+01:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }, {
                            'codLine': '6__40___',
                            'shortDescription': '40',
                            'description': '40-TRIBUNAL-ALFONSO XIII',
                            'codMode': '6',
                            'updateDate': '2016-06-02T09:31:47+02:00',
                            'updateKmlDate': '2016-06-01T17:04:00+02:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }, {
                            'codLine': '6__147___',
                            'shortDescription': '147',
                            'description': '147-CALLAO-BARRIO DEL PILAR',
                            'codMode': '6',
                            'updateDate': '2016-06-02T09:31:47+02:00',
                            'updateKmlDate': '2016-06-01T17:04:00+02:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }, {
                            'codLine': '6_N_22___',
                            'shortDescription': 'N22',
                            'description': 'N22-CIBELES-BARRIO DEL PILAR',
                            'codMode': '6',
                            'updateDate': '2017-06-27T11:21:02+02:00',
                            'updateKmlDate': '2017-06-27T10:08:00+02:00',
                            'nightService': 1,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }, {
                            'codLine': '6_N_24___',
                            'shortDescription': 'N24',
                            'description': 'N24-CIBELES-LAS TABLAS',
                            'codMode': '6',
                            'updateDate': '2016-06-02T09:31:47+02:00',
                            'updateKmlDate': '2016-06-01T17:04:00+02:00',
                            'nightService': 1,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }]
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 1
                }, {
                    'codStop': '6_4828',
                    'shortCodStop': '4828',
                    'codMode': '6',
                    'name': 'Castellana-San Germán',
                    'address': 'Pº de la Castellana, 152',
                    'postCode': '',
                    'codMunicipality': '4350',
                    'coordinates': {
                        'longitude': -3.6899180284389,
                        'latitude': 40.456032321623
                    },
                    'lines': {
                        'Line': {
                            'codLine': '6__5___',
                            'shortDescription': '5',
                            'description': '5-SOL/SEVILLA-CHAMARTIN',
                            'codMode': '6',
                            'updateDate': '2017-11-08T12:43:20+01:00',
                            'updateKmlDate': '2017-11-08T12:37:23+01:00',
                            'nightService': 0,
                            'active': True,
                            'shortItinerary': {},
                            'companyCode': ''
                        }
                    },
                    'access': 2,
                    'park': 0,
                    'nightLinesService': 0
                }, {
                    'codStop': '4_192',
                    'shortCodStop': '192',
                    'codMode': '4',
                    'name': 'SANTIAGO BERNABEU',
                    'address': 'Paseo de la Castellana 97 ',
                    'postCode': '',
                    'codMunicipality': '4350',
                    'coordinates': {
                        'longitude': -3.69038,
                        'latitude': 40.45159
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
                ]
            }
        }
    """
    if latitude is not None and longitude is not None and method is not None and distance is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetNearestStopsByLocation.php?latitude={latitude}&longitude={longitude}&mode=&method={method}&precision={precision}'
                         .format(latitude=latitude, longitude=longitude,
                                 method=method, precision=distance))
    else:
        raise NotEnoughParametersException('You must specify all the needed parameters.')

    return common_request(url_formatted)
