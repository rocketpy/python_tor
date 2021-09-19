# Tor Browser automation with Selenium

# PyPi: https://pypi.org/project/tbselenium/
# Github: https://github.com/webfp/tor-browser-selenium 

# pip install tbselenium

# Install geckodriver from the geckodriver releases page. Make sure you install version v0.23.0 version or newer;
# older versions may not be compatible with the current Tor Browser series.


# Basic usage:
# Using with system tor

# tor needs to be installed (apt install tor) and running on port 9050.
from tbselenium.tbdriver import TorBrowserDriver

with TorBrowserDriver("/path/to/TorBrowserBundle/") as driver:
    driver.get('https://check.torproject.org')

