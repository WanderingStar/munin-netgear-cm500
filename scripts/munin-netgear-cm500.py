#!/usr/bin/env python3.6

import os
import sys

from cm500 import get_channels


def config(host, user, password, mode='power'):
    print(f'''graph_title CM500 downstream channel {mode}
graph_vlabel {mode}
graph_category network''')
    us, ds = get_channels(host, user, password)
    for c in ds:
        id = c.id
        if mode == 'power':
            print(f'dn{id}_power.label dn {id} power')
            print(f'dn{id}_snr.label dn {id} snr')
        if mode == 'errors':
            print(f'dn{id}_corr.label dn {id} correctable')
            print(f'dn{id}_corr.type COUNTER')
            print(f'dn{id}_uncorr.label dn {id} uncorrectable')
            print(f'dn{id}_uncorr.type COUNTER')


def fetch(host, user, password, mode='power'):
    us, ds = get_channels(host, user, password)
    for c in ds:
        id = c.id
        if mode == 'power':
            print(f'dn{id}_power.value {c.power}')
            print(f'dn{id}_snr.value {c.snr}')
        if mode == 'errors':
            print(f'dn{id}_corr.value {c.corr}')
            print(f'dn{id}_uncorr.value {c.uncorr}')


if __name__ == "__main__":
    host = os.environ.get('cm500_host', '192.168.100.1')
    user = os.environ.get('cm500_user', 'admin')
    # you changed the default password on your cable modem... right?
    password = os.environ.get('cm500_password', 'password')

    if sys.argv[0].endswith('_errors'):
        mode = 'errors'
    else:
        mode = 'power'

    if len(sys.argv) > 1 and sys.argv[1] == 'config':
        config(host, user, password, mode)
    else:
        fetch(host, user, password, mode)
