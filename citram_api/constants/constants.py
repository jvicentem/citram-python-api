import enum
from enum import Enum
import re
import unicodedata

from citram_api.api.others.others import get_transport_modes, get_municipalities


def _create_dynamic_enum(func, key_1, key_2, name_key, value_key):
    aux = {}

    for mode in func()[key_1][key_2]:
        name = mode[name_key].replace(' ', '_').replace(',', '').upper()

        nfkd_form = unicodedata.normalize('NFKD', name)
        name = nfkd_form.encode('ASCII', 'ignore').decode('UTF-8')

        name = re.sub('[^A-Z_]+', '_', name)

        aux[name] = int(mode[value_key])

    return aux


TransportModes = enum.Enum('TransportModes', _create_dynamic_enum(get_transport_modes, 'modes', 'Mode',
                                                                  'name', 'codMode'))

Municipalities = enum.Enum('Municipalities', _create_dynamic_enum(get_municipalities, 'municipalities', 'Municipality',
                                                                  'name', 'codMunicipality'))


class OfficeTypes(Enum):
    RECARGA = 'RECARGA'
    OFICINA = 'OFICINA'
