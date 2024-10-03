---
author: Michael Prokop
categories:
- general
date: Thu, 27 Jul 2006 21:39:00 +0000
layout: post
slug: 166-new-develrelease-0.7-6
title: 'new develrelease: 0.7-6'

---
A new develrelease is available. Quoting the main changelog from my mail to [beta\-testers](http://grml.org/beta-tester/) and developers:

```
* includes the final build of 2.6.17-grml (based on 2.6.17.7):
  - reiser4 is part of the kernel again
  - SMP enabled (this means we also have dual-core support!)
  - featuring all extra modules
* bootoption noblank: disable console blanking
* grml2hd:
  - partition selector
  - grml-setlang: set language system-wide on grml system
  - grml-setkeyboard: set keyboard layout system-wide on grml system via
    /etc/sysconfig/keyboard
* grml-policy-rc.d: a wrapper script for invoke-rc.d to avoid
  automatical startup of init scripts via invoke-rc.d
* osd_server.py: listen for incoming messages on a specific port and
  print them via osd_cat; run 'grml-tips osd' for more details
  (thanks to Ulrich Dangel, Alexander Bernauer and Rico Schickel)
* myip: return IP address of running system on stdout
* updated hwinfo to version 12.9 (with backporting hw-ids from 13.0)
* updated packages to debian-pool by 2006-07-27
```
Notice: this is a pre\-release of grml 0\.8, the next few days are meant for testing, testing and testing so we can ship a new stable release soon.
