#  A Python SOCKS client module.

#  Github:  https://github.com/Anorov/PySocks
#  PyPi:  https://pypi.org/project/PySocks/

# pip install PySocks
# pip install -U requests[socks] 

#  Usage
import socks


s = socks.socksocket() # Same API as socket.socket in the standard lib

s.set_proxy(socks.SOCKS5, "localhost") # SOCKS4 and SOCKS5 use port 1080 by default
# Or
s.set_proxy(socks.SOCKS4, "localhost", 4444)
# Or
s.set_proxy(socks.HTTP, "5.5.5.5", 8888)

# Can be treated identical to a regular socket object
s.connect(("www.somesite.com", 80))
s.sendall("GET / HTTP/1.1 ...")
print s.recv(4096)


#  Monkeypatching
import urllib2
import socket
import socks


socks.set_default_proxy(socks.SOCKS5, "localhost")
socket.socket = socks.socksocket

urllib2.urlopen("http://www.somesite.com/") # All requests will pass through the SOCKS proxy
 
 
"""
 # SOCKS5 proxy for HTTP/HTTPS proxiesDict = { 'http' : "socks5://1.2.3.4:1080", 'https' : "socks5://1.2.3.4:1080" }
 # SOCKS4 proxy for HTTP/HTTPS proxiesDict = { 'http' : "socks4://1.2.3.4:1080", 'https' : "socks4://1.2.3.4:1080" }
 # HTTP proxy for HTTP/HTTPS proxiesDict = { 'http' : "1.2.3.4:1080", 'https' : "1.2.3.4:1080" } 
"""

"""
import urllib2
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "myprivateproxy.net",port=9050)
socket.socket = socks.socksocket res=urllib2.urlopen(url).read() 
"""
