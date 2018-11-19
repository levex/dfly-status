#!/usr/bin/env python
import socket
import sys
import os

debug = False
if len(sys.argv) == 2 and sys.argv[1] == "-d":
    debug = True

def get_ip_of(hostname):
    try:
        return socket.gethostbyaddr(hostname)[2][0]
    except socket.gaierror:
        return None

def get_status(hostname):
    ip = get_ip_of(hostname)
    if debug:
        print("%s has IP %s" % (hostname, ip))
    if debug is not None:
        res = os.system("ping -c 1 %s 1>/dev/null 2>/dev/null" % ip)
        if res == 0:
            return "\033[32mONLINE\033[39m"
        return "\033[31mOFFLINE\033[39m"
    else:
        return "N/A"


# Configure the websites here
websites = {
        'Main Website': 'dragonflybsd.org',
        'Mirror Master': 'mirror-master.dragonflybsd.org',
        'Leaf': 'leaf.dragonflybsd.org',
        }

for key, val in websites.items():
    print("%s (at %s) is %s" % (key, val, get_status(val)))
