# munin-netgear-cm500

This is a simple [Munin](http://munin-monitoring.org/) plugin to get scrape data
from the web interface of a Netgear CM500 Cable Modem.

This plugin requires Python 3.6 (sorrynotsorry).

Install with
```
python3 setup.py install
```

This should place `munin-netgear-cm500.py` in `/usr/local/bin` or some similar
suitable place.

Install it as a Munin plugin. Following Munin convention, the name you choose
specifies some of the options.

```
ln -s `which munin-netgear-cm500.py` /etc/munin/plugins/cm500_power
ln -s `which munin-netgear-cm500.py` /etc/munin/plugins/cm500_errors
```

Configure it by adding a stanza to `/etc/munin/plugin-conf.d/munin-node`
```
[cm500*]
env.cm500_host 192.168.100.1
env.cm500_user admin
env.cm500_password password
```
You did change the terrible default password on your modem, right?