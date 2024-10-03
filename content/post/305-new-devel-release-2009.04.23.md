---
author: Michael Prokop
categories:
- general
date: Thu, 23 Apr 2009 23:58:00 +0000
layout: post
slug: 305-new-devel-release-2009.04.23
title: 'new devel-release: 2009.04.23'

---
I just pushed a new devel release [to our mirror](http://debian.netcologne.de/www.grml.org/devel/). Quoting the main changelog:
* updated to kernel based on 2\.6\.28
* grml2usb: initial public version of the redesign, providing multi\-ISO support and many more features, check out [grml.org/grml2usb/](http://grml.org/grml2usb/)
* persistency feature: booting with bootoption 'persistent' activates a feature providing persistency for the ISO (so you can store all your changes on a partition and re\-use them\- cool, or?). Check out [live\-initramfs.en.7\.html](http://grml.org/online-docs/live-initramfs.en.7.html) and [live\-snapshot.en.1\.html](http://grml.org/online-docs/live-snapshot.en.1.html) (search for 'persistent' and 'live\-rw') until we have our own docs/instructions available. Note: Any help in this area is highly welcome!
* grml\-autoconfig: dropped /etc/grml/autoconfig.small
* * grml\-live: several bugfixes, integration of bsd4grml \- a special version of [MirBSD](https://www.mirbsd.org/) (available via 'bsd' on the bootprompt \- more details will follow later)
* grml\-etc\-core: using "zsh: $REPOSNAME" as GNU screen title name when standing inside a repository of a version control system (thanks, ft!)
* re\-added support for hardware based speakup modules, loadable via speakup.synth\=...
* new bootoption 'hwspeak' for probing speakup hardware modules
* new bootoption 'readonly': mark ALL /dev/\[hs]\*dX devices as read\-only, this is important for forensic investigations and automatically activated as well when booting via 'forensic'
