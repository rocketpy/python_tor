#  Python powered way to get a unique Tor IP

#  Docs:  https://pypi.org/project/toripchanger/

#  pip install toripchanger

# Basic example
from toripchanger import TorIpChanger


# Tor IP reuse is prohibited.
tor_ip_changer_0 = TorIpChanger(reuse_threshold=0)
current_ip = tor_ip_changer_0.get_new_ip()

# Current Tor IP address can be reused after one other IP was used (default setting).
tor_ip_changer_1 = TorIpChanger(local_http_proxy='127.0.0.1:8888')
current_ip = tor_ip_changer_1 .get_new_ip()

# Current Tor IP address can be reused after 5 other Tor IPs were used.
tor_ip_changer_5 = TorIpChanger(tor_address="localhost", reuse_threshold=5)
current_ip = tor_ip_changer_5.get_new_ip()
 
