---
author: Michael Prokop
categories:
- general
date: Sun, 19 Feb 2006 21:18:00 +0000
layout: post
slug: 137-develrelease-grml-0.6-2
title: develrelease grml 0.6-2

---
Chemnitzer LinuxTage 2006 and the [grml CLT06 release]({{< relref "134-grml-chemnitzer-linuxdays-2006" >}}) are coming closer. grml 0\.6\-2 is available for [betatesters](https://grml.org/beta-tester/) and developers. See the changelog for more details:
*Changelog from grml 0\.6\-1:*
* updated isolinux to version syslinux\-3\.20\-pre6
* removed mysql\-server package
* rebuildfstab (/etc/fstab):
+ partitions have new mount\-options: 'noauto,nouser,dev,suid,exec'
+ improved partition detection (e.g. reiser4 is detected now)
*Changelog from grml 0\.6\-2:*  
* updated all packages (including some kernel module updates)
* boot cheatcode 'vmware' \- disable usb/firewire detection during bootprocess, load some SCSI\-modules instead
* reworked zsh completion (no error correction on rm and mv commands)
* grml2hd: check for given mbr option and prompt for activating it if not set
* bt\-audio: script to connect bluetooth headset to computer
* /bin/sh now points to /bin/bash; reason: Debian does not support zsh as /bin/sh. Take a look at [\#329288](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=329288) and [\#340058](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=340058) for example. zsh is used as interactive shell anyway of course
* grub can be called from bootmenu (in isolinux) through running 'grub' now; thanks a lot to Rafael Steiner!
* implemented [sw\-raid related stuff as mentioned on grml\-user mailinglist](http://article.gmane.org/gmane.linux.distributions.grml.user/5)
Now I just implemented a function to detect suspend\-to\-disk signatures on swap partitions so grml does not touch them unless you are requesting via using bootoption 'anyswap'.
This entry is brought to you by mika running grml 0\.6\-2\-a. :\-)
