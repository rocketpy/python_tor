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

#  Example 2
import time, socks, socket
from urllib2 import urlopen
from stem import Signal
from stem.control import Controller

numb_ip_address = 3

with Controller.from_port(port = 9051) as controller:
   controller.authenticate(password = 'my_pwd')
   socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)  # 9150
   socket.socket = socks.socksocket   

   for i in range(0, numb_ip_address):
       new_ip = urlopen("http://icanhazip.com").read()
       print("NewIP Address: %s" % new_ip)
       controller.signal(Signal.NEWNYM)
       if controller.is_newnym_available() == False:
        print("Waitting time for Tor to change IP: "+ str(controller.get_newnym_wait()) +" seconds")
        time.sleep(controller.get_newnym_wait())
   controller.close()
    
