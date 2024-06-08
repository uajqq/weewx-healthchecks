# installer for weewx-healthchecks
# Copyright 2024 uajqq

from weecfg.extension import ExtensionInstaller

def loader():
    return healthchecksInstaller()

class healthchecksInstaller(ExtensionInstaller):
    def __init__(self):
        super(healthchecksInstaller, self).__init__(
            version="1.1",
            name='Healthchecks',
            description='Send pings to any URL, like healthchecks.io, for monitoring purposes',
            author="uajqq",
            report_services="user.healthchecks.Healthchecks",
            config={
                'Healthchecks': {
                    'url': '<replace with custom URL>',
                },
            },
            files=[('bin/user', ['bin/user/healthchecks.py'])],
        )
