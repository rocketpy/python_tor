import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


torexe = os.popen(r'C:\Users\...\Tor\tor.exe')
profile = FirefoxProfile(r'C:\Users\...\TorBrowser\Data\Browser\profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe')
driver.get("http://check.torproject.org")

