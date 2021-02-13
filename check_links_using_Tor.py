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
            self.proxies = {'http': 'socks5h://127.0.0.1:9050',  # 9150
                            'https': 'socks5h://127.0.0.1:9050'  # 9150
                           }
            print("Proxy setup is done")
    
        except:
            print("Tor is not activated, please run the program again !")
            
            
    def check(self,onion,save):
        print()
        try:
            data = requests.get(f"http://{onion}", proxies=self.proxies)
            status=data.status_code
        except:
            status = 404
        if status == 200:
            print(f"{onion} : Active")
            print(f"Status Code : {status}")
        else:
            print(f"{onion} : nonActive")
            print(f"Status Code : {status}")

        if save == True:
            w = open("Status.txt","a")
            if status == 200:
                w.write(f"http://{onion} : Active")
            else:
                w.write(f"http://{onion} : nonActive")
            w.close()
        print()
        return 
    
if __name__ == "__main__":
    
    run = TorActivation()
    run.StartTor()
    run.proxy_build()
    while True:
        print("1. Single Url Checking")
        print("2. Multiplt Url Checking")
        print("3. Quit")
        option = input("Enter your option: ")
        if str(option) == '1':
            onion=input("Enter the url: ")
            run.check(onion,False)
        elif str(option) == '2':
            filename = input("Enter the txt filename: ")
            f = open(filename, "a")
            f.readlines()
            for x in f:
                x=x.rstrip("\n")
                run.check(x, True)
            f.close()
        elif option == '3':
            break            
 
