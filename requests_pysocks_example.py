import socks
import socket 
import requests 


ip = 'localhost'
# change your proxy's ip port = 0000
# change your proxy's port socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port) 
# socket.socket = socks.socksocket
# url = u'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=inurl%E8%A2%8B'
# print(requests.get(url).text) 


  """Connect to *address* and return the socket object. Convenience function.
  Connect to *address* (a 2-tuple ``(host, port)``) and return the socket object. Passing the optional
  *timeout* parameter will set the timeout on the socket instance before attempting to connect. 
  If no *timeout* is supplied, the global default timeout setting returned by
  :func:`getdefaulttimeout` is used. If *source_address* is set it must be a tuple of (host, port) 
  for the socket to bind as a source address before making the connection.
  An host of '' or port 0 tells the OS to use the default.
  """

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 1080) 

def create_connection(address, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None, socket_options=None):
    host, port = address
    if host.startswith('['):
        host = host.strip('[]')
        err = None
        for res in socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            sock = None
            try: 
                sock = socks.socksocket(af, socktype, proto)
                urllib3.util.connection._set_socket_options(sock, socket_options) 
                if timeout is not socket._GLOBAL_DEFAULT_TIMEOUT: 
                    sock.settimeout(timeout)
                    if source_address: 
                        sock.bind(source_address) 
                        sock.connect(sa)
                        return sock
             except socket.error as e:
                 err = e if sock is not None: sock.close()
                  sock = None
                  if err is not None: 
                      raise err raise socket.error("getaddrinfo returns an empty list")
                    
# monkeypatch
urllib3.util.connection.create_connection = create_connection 
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 1080)

