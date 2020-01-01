import xmltodict
from zeep import Client

from citram_api.constants.constants import Urls
from citram_api.utils.custom_exceptions import NotEnoughParametersException
from citram_api.utils.utils import common_request


def get_municipalities():
    url_formatted = (Urls.CITRAM_WIDGET_SERVICE.value + '/GetMunicipalities.php')

    return common_request(url_formatted)


def get_ttp_card_info(ttp_number):
    if ttp_number is not None:
        client = Client(Urls.CITRAM_CARD_SERVICE.value)
        result = client.service.ConsultaSaldo1(sNumeroTTP=ttp_number)
    else:
        raise NotEnoughParametersException('You must specify a transport card number.')

    final_result = {'status': result['iCallLogField'],
                    'card_info': xmltodict(result['sResulXMLField'])}

    return final_result
