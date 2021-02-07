#  pip install -U requests[socks]
import requests


#  Tor browser listens on port 9150
proxies = {'http': 'socks5://localhost:9150',  # or 9050  or 9151
           'https': 'socks5://localhost:9150'}  # or 9050  or 9151

url = 'http://httpbin.org/ip'

print(requests.get(url, proxies=proxies).text)


"""
resp = requests.get('http://...', 
                     proxies=dict(http='socks5://user:pass@host:port',
                     https='socks5://user:pass@host:port'))                      
"""

# sometimes need change  socks5://proxyhost:1234 to socks5h://proxyhost:1234  # add  h  to socks5
 
