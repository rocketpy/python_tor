import os
import json
import time
import requests
import subprocess

#  Checking a Tor onion links active status !


class TorActivation:
    def __ini__(self):
        pass

    def StartTor(self):
        subprocess.Popen([f"{os.getcwd()}\\Tor\\tor.exe"])
        time.sleep(10)
        print("Tor Proxy is started !")
        print("Start of checking  !")

    def proxy_build(self):
        try:
            self.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
            }
            print("proxy setup is succefully done")
    
        except:
            print("Tor is not activated please run the program again!!!")
