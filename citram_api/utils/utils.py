import requests


def common_request(url):
    res = requests.get(url)

    return res.json()


def create_line_cod(mode_cod, line):
    return str(mode_cod) + '__' + str(line) + '___'


def create_stop_cod(mode_cod, stop_cod):
    return str(mode_cod) + '_' + str(stop_cod)