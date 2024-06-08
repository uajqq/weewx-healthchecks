"""A service to send a ping to any URL with every archive interval, for example
healthchecks.io, to monitor system uptime and allow notifications if something
isn't working.

This service is adapted from the Alarm example extension included with weewx.

*******************************************************************************

To use this extension, add the following to the weewx configuration file:

[Healthchecks]
    url = "<your URL>"
  
With every archive interval, the specified url will be pinged. If you are using
healthchecks.io, you can specify the length of time before you get a warning.

*******************************************************************************

To enable this service, either install as specified in the readme, or:

1) Copy this file to the user directory. See https://bit.ly/33YHsqX for where your user
directory is located.

2) Modify the weewx configuration file by adding this service to the option
"report_services", located in section [Engine][[Services]].

[Engine]
  [[Services]]
    ...
    report_services = weewx.engine.StdPrint, weewx.engine.StdReport, user.healthchecks.Healthchecks

"""

import socket
import urllib.request
import logging
import threading

import weewx
from weeutil import logger
from weewx.engine import StdService

log = logging.getLogger(__name__)


# Inherit from the base class StdService:
class Healthchecks(StdService):
    """Service that sends a ping to the specified URL with every archive"""

    def __init__(self, engine, config_dict):
        # Pass the initialization information on to my superclass:
        super(Healthchecks, self).__init__(engine, config_dict)

        try:
            # Dig the needed options out of the configuration dictionary.
            # If the URL is missing, an exception will be raised and
            # the ping will not be sent.
            self.url = config_dict["Healthchecks"]["url"]
            if "http" not in self.url:  # Simple check to see if the url looks valid
                raise KeyError("url")
            log.info(
                "Healthchecks: Using url {}".format(self.url),
            )
            # If we got this far, it's ok to start intercepting events:
            self.bind(weewx.NEW_ARCHIVE_RECORD, self.new_archive_record)
        except KeyError as e:
            log.info(
                "Healthchecks: Healthchecks not set up. Missing parameter: {}".format(e)
            )

    def new_archive_record(self, event):
        """Gets called on a new archive record event."""

        # Launch in a separate thread so it doesn't block the main LOOP thread:
        try:
            log.debug("Healthchecks: sending ping")
            t = threading.Thread(target=Healthchecks.send_ping(self))
            t.start()
        except Exception as e:
            log.error("Healthchecks: Attempt to ping failed: {}".format(e))

    def send_ping(self):
        """Send the ping to the specified URL"""
        try:
            urllib.request.urlopen(self.url, timeout=10)
        except Exception as e:
            # Log ping failure here...
            log.error("Healthchecks: Attempt to ping failed: {}".format(e))
