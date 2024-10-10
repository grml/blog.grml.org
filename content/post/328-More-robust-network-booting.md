---
author: Michael Prokop
categories:
- general
date: Tue, 29 Dec 2009 22:00:00 +0000
layout: post
slug: 328-More-robust-network-booting
title: More robust network booting

---
**Summary:** Grml gets more robust support for network booting.
**Background information:** A customer uses [Grml](https://grml.org/) for the deployment process of their systems. Grml isn't just used for the deployment but also as part of the netboot environment in the High\-Availability (HA) setup running on [IBM BladeCenter](http://www-03.ibm.com/systems/bladecenter/hardware/) systems. The netboot setup is used for hardware inventory and to be able to replace bladesystems without the need for *any* manual configuration (implementing features of [IBM BladeCenter Open Fabric Manager](http://www-03.ibm.com/systems/bladecenter/news/openfabricmanager/) using Debian/Linux). As being part of a HA setup the netboot setup should work no matter which server is unavailable or which network connection is broken. The software stack is redundant thanks to [DRBD](http://www.drbd.org/), [Heartbeat](http://www.linux-ha.org/)\& CO while the hardware stack itself is redundant due to the bladeserver infrastructure.
**Problem description:** If you have more than one network card (NIC) inside your system you might encounter problems with network booting as soon as the first/preferred NIC doesn't work. This is a common problem in netboot environments, usually solved by crude hacks and workarounds.
**Solution:** The last [Grml release](https://grml.org/) (2009\.10\) already invented the ethdevice\= bootoption which allows you to specify a specific NIC for booting. I just extended ethdevice and its surrounding code so it is possible to specify **multiple** devices at once that should be configured. If you don't have any specific configuration all present NICs will be used for configuration via DHCP **automatically**. The [resulting code](http://git.grml.org/?p=live-initramfs-grml.git;a=blob;f=debian/patches/10_support_ethdevice.dpatch) is quite tricky because ipconfig of klibc\-utils might fail in several situations. I just uploaded live\-initramfs (1\.157\.4\-1grml.01\) to [the grml\-testing repository](http://deb.grml.org/), the [daily ISOs](http://daily.grml.org/) will provide the feature within the next few days as well.
**Available bootoptions and behaviour:**
* default bootoptions (grml's default, no specific settings): configure any present network interface automatically
* bootoption 'ethdevice\=eth1': forces configuration of network device eth1 only
* bootoption 'ethdevice\=eth0,eth1': try configuration of eth0 and eth1
* bootoption 'ethdevice\=eth0,eth1 ethdevice\-timeout\=30': try configuration of eth0 and eth1 and raise timeout of configuration from default (being 15 seconds) to 30 seconds
**Screenshot of netboot in action:**
[![Screenshot of netboot in action](/images/pxeboot.serendipityThumb.png)](/images/pxeboot.png)