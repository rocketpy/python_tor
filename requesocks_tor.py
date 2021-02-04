#  Github:  https://github.com/dvska/requesocks

#  pip install requesocks 


import requests
import requesocks


requests = requesocks.session()
requests.proxies = {"http": "socks5://127.0.0.1:8118",
                   "https": "socks5://127.0.0.1:8118"}


"""
import requests


proxy = { 'http':'127.0.0.1:8118','https':'127.0.0.1:8118' }
r = requests.get('https://www.whatismyip.com/', proxies=proxy)
#r = requests.get('http://www.whatsmyip.org/')
print(r)
"""

#  customization privoxy
"""
forward-socks4a / localhost:9050 .  # try 9150
forward-socks5 / localhost:9050 .   # try 9150
"""
