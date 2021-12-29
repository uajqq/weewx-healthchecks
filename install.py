# Installer file for Healthchecks.io extension for WeeWX
# Distributed under the terms of the GNU Public License (GPLv3)

from bin.user.healthchecks import Healthchecks
import configobj
from setup import ExtensionInstaller

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO


def loader():
    return healthchecksInstaller()


class healthchecksInstaller(ExtensionInstaller):
    def __init__(self):
        super(healthchecksInstaller, self).__init__(
            version="1.0",
            name="Healthchecks",
            description="Send pings to healthchecks.io for monitoring purposes",
            author="uajqq",
            report_services="user.healthchecks.Healthchecks",
            config=config_dict,
            files=[("bin/user", ["bin/user/healthchecks.py"])],
        )


# Config stanza
extension_config = """

[Healthchecks]
    url = <insert custom url>

"""
config_dict = configobj.ConfigObj(StringIO(extension_config))
