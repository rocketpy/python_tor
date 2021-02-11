import os
from selenium import webdriver


# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT

torexe = os.popen(r'C:\Users\...\Tor\tor.exe')
PROXY = "socks5://localhost:9150" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
driver.get("http://check.torproject.org")
