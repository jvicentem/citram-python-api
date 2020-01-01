from citram_api.constants.hosts import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_offices_by_type(offices_type):
    if offices_type is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?type={offices_type}'
                         .format(offices_type=str(offices_type)))
    else:
        raise NotEnoughParametersException('You must specify an office type.')

    return common_request(url_formatted)


def get_offices_by_type_and_postcode(offices_type, post_code):
    if offices_type is not None and post_code is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?type={offices_type}&postcode={postcode}'
                         .format(offices_type=str(offices_type), postcode=str(post_code)))
    else:
        raise NotEnoughParametersException('You must specify an office type and a zip code.')

    return common_request(url_formatted)


def get_offices_by_type_and_postcode(offices_type, post_code):
    if offices_type is not None and post_code is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?type={offices_type}&postcode={postcode}'
                         .format(offices_type=str(offices_type), postcode=str(post_code)))
    else:
        raise NotEnoughParametersException('You must specify an office type and a zip code.')

    return common_request(url_formatted)


def get_offices_by_type_and_municipality(offices_type, cod_municipality):
    if offices_type is not None and cod_municipality is not None:
        url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value +
                         '/GetOffices.php?type={offices_type}&codmunicipality={codmunicipality}'
                         .format(offices_type=str(offices_type), codmunicipality=str(cod_municipality)))
    else:
        raise NotEnoughParametersException('You must specify an office type and a municipality code.')

    return common_request(url_formatted)