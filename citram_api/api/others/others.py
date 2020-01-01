from citram_api.constants.constants import Urls
from citram_api.utils.utils import common_request


def get_municipalities():
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value + '/GetMunicipalities.php')

    return common_request(url_formatted)

