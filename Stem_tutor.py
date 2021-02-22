#  Stem is a Python controller library that allows applications to interact with Tor (https://www.torproject.org/).

#  PyPi: https://pypi.org/project/stem/

#  Docs: https://stem.torproject.org/
#  Tutorial: https://stem.torproject.org/tutorials.html

# pip install stem

from stem.control import Controller


with Controller.from_port(port = 9051) as controller:
    controller.authenticate()  # provide the password here if you set one

    bytes_read = controller.get_info("traffic/read")
    bytes_written = controller.get_info("traffic/written")

    print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))

