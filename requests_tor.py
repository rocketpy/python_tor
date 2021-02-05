import requests


#  Tor browser listens on port 9150
proxies = {'http': 'socks5://localhost:9150',
           'https': 'socks5://localhost:9150'}

url = 'http://httpbin.org/ip'

print(requests.get(url, proxies=proxies).text)
