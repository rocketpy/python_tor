#  Pure python tor protocol implementation

#  PyPi:  https://pypi.org/project/torpy/
#  Github:  https://github.com/torpyorg/torpy

#  pip install torpy
#  for using TorHttpAdapter with requests library you need install extras: pip3 install torpy[requests]

#  Features
"""
No Stem or official Tor client required
Support v2 hidden services (v2 specification)
Support Basic and Stealth authorization protocol
Provide simple TorHttpAdapter for requests library
Provide simple urllib tor_opener for making requests without any dependencies
Provide simple Socks5 proxy
"""

#  Usage examples:

# A basic example of how to send some data to a clearnet host or a hidden service
from torpy import TorClient


hostname = 'ifconfig.me'  # It's possible use onion hostname here as well
with TorClient() as tor:
    # Choose random guard node and create 3-hops circuit
    with tor.create_circuit(3) as circuit:
        # Create tor stream to host
        with circuit.create_stream((hostname, 80)) as stream:
            # Now we can communicate with host
            stream.send(b'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % hostname.encode())
            recv = stream.recv(1024)
