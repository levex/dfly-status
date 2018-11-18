#!/usr/bin/env python

# Configure the websites here
websites = {
        'Main Website': 'dragonflybsd.org',
        'Mirror Master': 'mirror-master.dragonflybsd.org',
        'Leaf': 'leaf.dragonflybsd.org'
        }

for key, val in websites.items():
    print("%s (at %s) is N/A" % (key, val))
