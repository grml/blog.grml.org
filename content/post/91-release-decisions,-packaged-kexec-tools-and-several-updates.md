---
author: Michael Prokop
categories:
- general
date: Mon, 08 Aug 2005 20:06:00 +0000
layout: post
slug: 91-release-decisions,-packaged-kexec-tools-and-several-updates
title: release-decisions, packaged kexec-tools and several updates

---
We decided to release grml 0\.5 as soon as the config\-framework is "finished" (I'm still working on it). In the meanwhile kernel 2\.6\.13 should be released. 2\.6\.12\-grml is working quite well on grml\-small, (the still unreleased) grml\-usb and grml(\-large). SMP is causing some troubles with cpufreq and ACPI :\-(( \- so it will be deactivated in the next release. BTW: Tobias is doing a great job with packaging udev (currently version 0\.065\) for the grml\-system, thanks to him!
Yesterday I packaged [kexec\-tools](http://www.xmission.com/~ebiederm/files/kexec/) so we can test it with 2\.6\.13 as soon it is available. As usual it's available [in the grml\-repos](https://grml.org/repos/).  

Yesterday I wrote a small script named [grml2usb](https://grml.org/scripts/grml2usb) to install a grml\-iso to an usb\-stick. The script should work on any linux\-system and [reduces the necessary manual steps](http://wiki.grml.org/doku.php?id=usb). Testing and feedback welcome!
Several updates, bugfixes and improvements have taken place in grml\-autoconfig, grml\-scripts and grml\-etc.
And I just implemented the bootoption 'startx' so grml can boot directly into the X window system using grml\-x.
