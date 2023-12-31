# Ethernet Remote Control for RDK

This is a VERY simple application to emulate the remote control commands of RDK ( https://wiki.rdkcentral.com/ ) using you PC's keyboard and network connection. It uses the [RDK Services API](https://rdkcentral.github.io/rdkservices/#/README)

# Pre-requisites: #

Before start, please ensure you know your device's IP and API port (default is 9998).

# How to use it #


```
usage: rdk-keyboard.py [-h] [--port PORT] IP

Keyboard for RDK

positional arguments:
  IP           The RDK IP (mandatory). Ex: python3 rdk-keyboard.py 192.168.0.200

options:
  -h, --help   show this help message and exit
  --port PORT  RDK's Port number to connect (Default: 9998)
```

After starting the script, click on the shell and the following keys will be able to control RDK as a remote:

`KEY_LEFT`,`KEY_RIGHT`,`KEY_UP`,`KEY_DOWN`,`Enter`,`Backspace`

## Example ##

```
python3 rdk-keyboard.py 192.168.0.15 --port 9998
```
