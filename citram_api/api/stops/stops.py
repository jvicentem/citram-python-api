import requests

from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_stops_by_cod_stop(cod_stop):
    if cod_stop is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?codStop={codStop}'
                         .format(codStop=cod_stop))
    else:
        raise NotEnoughParametersException('You must specify a stop code.')

    return common_request(url_formatted)


def get_stops_by_custom_search(custom_search):
    if custom_search is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?customSearch={customSearch}'
                         .format(customSearch=custom_search))
    else:
        raise NotEnoughParametersException('Introduce a valid string as a search.')

    return common_request(url_formatted)


def get_stops_by_zip_code(postcode):
    if postcode is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?postcode={postcode}'
                         .format(postcode=postcode))
    else:
        raise NotEnoughParametersException('You must specify a zip code.')

    res = requests.get(url_formatted)

    return res.json()


def get_stops_by_municipality(cod_municipality):
    if cod_municipality is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?codMunicipality={codMunicipality}'
                         .format(codMunicipality=cod_municipality))
    else:
        raise NotEnoughParametersException('You must specify a municipality code.')

    res = requests.get(url_formatted)

    return res.json()


def get_stop_info(cod_stop):
    if cod_stop is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetStops.php?codStop={codStop}'
                         .format(codStop=cod_stop))
    else:
        raise NotEnoughParametersException('You must specify a stop code.')

    res = requests.get(url_formatted)

    return res.json()


def get_stop_times(cod_stop, stop_type, order_by, stop_times_by_iti):
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
    if latitude is not None and longitude is not None and method is not None and distance is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetNearestStopsByLocation.php?latitude={latitude}&longitude={longitude}&mode=&method={method}&precision={precision}'
                         .format(latitude=latitude, longitude=longitude,
                                 method=method, precision=distance))
    else:
        raise NotEnoughParametersException('You must specify all the needed parameters.')

    return common_request(url_formatted)
