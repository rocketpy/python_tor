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

"""
The default location for Firefox’s profile folder differs depending on some platform.
The default locations are:

Windows 7, 8.1, and 10: C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\xxxxxxxx.default

Mac OS X El Capitan: Users/<username>/Library/Application Support/Firefox/Profiles/xxxxxxxx.default

Linux: /home/<username>/.mozilla/firefox/xxxxxxxx.default
"""
 
 """
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary(r"C:\Users\Admin\Desktop\Tor Browser\Browser\firefox.exe")
profile = FirefoxProfile(r"C:\Users\Admin\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")


 """
 
