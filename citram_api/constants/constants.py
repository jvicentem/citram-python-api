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


# extra:


Companies = {
            'INTERBUS, S.A.': '001',
            'HEREDEROS DE J. COLMENAREJO, S.A.': '002',
            'SANJUAN ABAD, S.L.': '004',
            'EMPRESA MARTÍN, S.A.': '008',
            'ARGABUS, S.A.': '009',
            'LA VELOZ, S.A.': '010',
            'LARREA, S.A.': '014',
            'AUTOCARES JULIAN DE CASTRO, S.A.': '015',
            'CASTROMIL, S.A.U.': '079',
            'LLORENTE BUS, S.L.': '023',
            'AUTOMNIBUS INTERURBANOS, S.A.': '024',
            'FRANCISCO LARREA, S.A.': '025',
            'AUTOPERIFERIA, S.A.': '026',
            'TC': '029',
            'DE BLAS Y CIA, S.L.': '034',
            'EMPRESA TURÍSTICA DE AUTOBUSES, S.L.': '036',
            'US': '037',
            'TRANSPORTES ALACUBER, S.A.': '038',
            'C.E.V.E.S.A.': '042',
            'EL GATO, S.L.': '043',
            'IRUBUS S.A': '039',
            'CA': '049',
            'EMPRESA RUIZ, S.A.': '050',
            'CN': '057',
            'ALSA METROPOLITANA, S.A.U.': '129',
            'AUTOCARES MOSAMO, S.L.': '005',
            'AUTOBUSES PRISEI, S.L.': '006',
            'AUTOCARES BELTRAN, S.A.': '011',
            'TRANSPORTES SANTO DOMINGO, S.L.': '027',
            'EMDO, S.A.': '028',
            'CASADO MONTES S.L.': '030',
            'ALCALABUS, S.L.': '080',
            'AYUNTAMIENTO DE LA PUEBLA DE LA SIERRA': '040',
            'AUTOBUSES SAMAR, S.A.': '058',
            'AYUNTAMIENTO PEDREZUELA': '066',
            'SEAL, S.A.': '067',
            'AVANZA LINEAS INTERURBANAS, S.A. (SEPULVEDANA)': '068',
            'AUTO RES, S.L.': '069',
            'MAITOURS': '070',
            'FLORA VILLA, S.A.': '071',
            'AYUNTAMIENTO EL MOLAR': '072',
            'TRANSPORTES URBANOS DEL NOROESTE, S.L.': '073',
            'NEXCONTINENTAL HOLDINGS': '076',
            'AVANZA INTERURBANOS, S.L.U.': '077',
            'AVANZA INTERURBANOS DEL SUR, S.L.U.': '078',
            'MANCOMUNIDAD ALTO JARAMA': '099',
            'METROS LIGEROS DE MADRID, S.A.': '210',
            'METRO LIGERO OESTE, S.A.': '220',
            'TRANVÍA DE PARLA, S.A.': '700',
            'AUTOBUSES URBANOS DE ARGANDA, S.A.': '082',
            'EMPRESA MUNICIPAL DE TRANSPORTES': '100',
            'RENFE CERCANIAS': '301',
            'METRO MADRID': '200',
            'EMT Fuenlabrada': '053'
        }
