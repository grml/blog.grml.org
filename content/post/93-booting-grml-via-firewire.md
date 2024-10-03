---
author: Michael Prokop
categories:
- general
date: Mon, 15 Aug 2005 00:22:00 +0000
layout: post
slug: 93-booting-grml-via-firewire
title: booting grml via firewire

---
grml boots via firewire. Thanks to Martin Buchleitner for helping me to locate the problem, now we will officially support booting grml via firewire starting with the upcoming release(s).

BTW: I renamed the `usb`-cheatcode to scandelay and slightly improved it. Now it's possible to add a delay of some seconds to the boot sequence so the modules in the initrd have enough time to access the devices. Currently scandelay uses a default of 10 seconds, using a parameter makes it more flexible - e.g. `scandelay=3` will add a delay of only 3 seconds.  

