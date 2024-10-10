---
author: Michael Prokop
categories:
- packages
date: Wed, 20 May 2009 20:02:22 +0000
layout: post
slug: 308-grml2usb-supports-installation-of-running-system-to-USB-device
title: grml2usb supports installation of running system to USB device

---
News from grml2usb: I just implemented the feature to be able to install the currently running grml system to a USB device running 'grml2usb /live/image /dev/sdx1'. This means the rewritten grml2usb script provides all the features the old script used to provide and will become part of the upcoming stable release therefor. Of course the new grml2usb script provides several new, additional features \- like support for multi\-ISOs, specifiying default bootoptions,... (so you can even run 'grml2usb \-\-bootoptions\="persistent" /live/image /home/grml/grml\_2009\.05\.iso /dev/sdx1'!). Check out [grml.org/grml2usb/](https://grml.org/grml2usb/) for further details and make sure to grab grml2usb 0\.9\.6\.