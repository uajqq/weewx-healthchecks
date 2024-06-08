# weewx-healthchecks
Extension for weewx that pings any specified URL, like [healthchecks.io](https://healthchecks.io), on every archive interval. This allows you to be notified via email, text message, etc. if weewx stops updating. You can even get a phone call.

Visit [healthchecks.io](https://healthchecks.io) to get set up and obtain a custom url for your installation.


### Installation


1) Download the driver:

```
wget -O weewxhealthchecks.zip https://github.com/uajqq/weewx-healthchecks/zipball/main
```

2) Install the driver:

```
sudo wee_extension --install weewxhealthchecks.zip
``` 

3) [this should be done automatically by the installer -- check to make sure] Add the service as a `report_service` under the  `[Engine][[Services]]` stanza in `weewx.conf`:

```
[Engine]
    [[Services]]
        report_services = [...], user.healthchecks.Healthchecks
```

4) Add your custom url (for example, from healthchecks.io) in the appropriate place in `weewx.conf`:

```
[Healthchecks]
    url = <insert custom url>
```

5) Restart weewx to see your changes. Check the logs to make sure the service is set up correctly. Pings are sent out on every weewx archive interval (default every 5 minutes).
