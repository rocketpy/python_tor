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


# Using with Stem
# First, make sure you have Stem installed (pip install stem). The following will start a new tor process using Stem.
# It will not use the tor installed on your system.

import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

tbb_dir = "/path/to/TorBrowserBundle/"
tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
    driver.load_url("https://check.torproject.org")

tor_process.kill()

