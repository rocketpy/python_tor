import socks
import socket
import requests


socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

print(requests.get('http://icanhazip.com')).content
