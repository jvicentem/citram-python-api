from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_lines_by_mode(mode_cod):
    if mode_cod is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetLines.php?mode={mode}'
                         .format(mode=str(mode_cod)))
    else:
        raise NotEnoughParametersException('You must specify a transport mode.')

    return common_request(url_formatted)


def get_lines_by_municipality(cod_municipality):
    if cod_municipality is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetLines.php?codMunicipality={codMunicipality}'
                         .format(codMunicipality=str(cod_municipality)))
    else:
        raise NotEnoughParametersException('You must specify a municipality code.')

    return common_request(url_formatted)


def get_lines_by_line_code(cod_line):
    if cod_line is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetLines.php?codLine={codLine}'
                         .format(codLine=str(cod_line)))
    else:
        raise NotEnoughParametersException('You must specify a line code.')

    return common_request(url_formatted)


def get_line_info(cod_line):
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetLinesInformation.php?activeItinerary=1&codLine={codLine}'
                     .format(codLine=cod_line))

    return common_request(url_formatted)


def get_lines_timeplanning(cod_line):
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetLinesTimePlanning.php?activeItinerary=1&codLine={codLine}'
                     .format(codLine=cod_line))

    return common_request(url_formatted)


def get_line_location(mode, cod_itinerary, cod_line, cod_stop, direction):
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetLineLocation.php?mode={mode}&codItinerary={codItinerary}&codLine={codLine}&codStop={codStop}&direction={direction}'
                     .format(mode=str(mode), codItinerary=cod_itinerary, codLine=cod_line, codStop=cod_stop,
                             direction=str(direction)))

    return common_request(url_formatted)


def get_incidents_affectations(mode, cod_line):
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                     '/GetIncidentsAffectations.php?mode={mode}&codLine={codLine}'
                     .format(mode=str(mode), codLine=cod_line))

    return common_request(url_formatted)
