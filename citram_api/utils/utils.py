import requests


def common_request(url):
    res = requests.get(url)

    return res.json()
