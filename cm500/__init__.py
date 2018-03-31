import re
from collections import namedtuple

import requests
import urllib3
from requests.auth import HTTPBasicAuth

UsChannel = namedtuple('UsChannel', ['n', 'lock', 'type', 'id', 'rate', 'freq', 'power'])
DsChannel = namedtuple('DsChannel', ['n', 'lock', 'mod', 'id', 'freq', 'power', 'snr', 'corr', 'uncorr'])


def chunk(size, collection):
    '''Divide collection into chunks of size'''
    while collection:
        this, collection = collection[:size], collection[size:]
        yield this


def get_channels(host, user, password):
    '''Fetch the lists of upstream and downstream channels from the CM500 status page'''
    url = f'https://{host}:8443/DocsisStatus.htm'
    urllib3.disable_warnings()
    for _ in range(3):
        result = requests.get(url, auth=HTTPBasicAuth(user, password), verify=False)
        if result:
            break
    text = result.text

    # for some reason, this page is littered with confusing comments
    text = re.sub('/\*.*?\*/', '', text, flags=re.DOTALL)

    us, ds = [], []

    # the actual data is written into the page by JavaScript functions...
    match = re.search("function InitUsTableTagValue\(\)\s+{\s+var tagValueList = '\d+\|([^']+)\|'", text)
    if match:
        us = [UsChannel(*c) for c in chunk(7, match.group(1).split('|'))]

    match = re.search("function InitDsTableTagValue\(\)\s+{\s+var tagValueList = '\d+\|([^']+)\|'", text)
    if match:
        ds = [DsChannel(*c) for c in chunk(9, match.group(1).split('|'))]

    return us, ds
