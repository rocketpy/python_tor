import socks
import socket
import requests
from stem import Signal
from stem.control import Controller


socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

print(requests.get('http://icanhazip.com')).content

#  To use a different ip address for each request

with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password='your password set for tor controller port in torrc')
    print("Success !")
    controller.signal(Signal.NEWNYM)
    print("New Tor connection processed")
