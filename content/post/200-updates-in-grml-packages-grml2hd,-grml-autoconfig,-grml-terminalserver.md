---
author: Michael Prokop
categories:
- packages
date: Thu, 16 Nov 2006 23:03:00 +0000
layout: post
slug: 200-updates-in-grml-packages-grml2hd,-grml-autoconfig,-grml-terminalserver
title: updates in grml-packages (grml2hd, grml-autoconfig, grml-terminalserver)

---
Just to keep developers and beta\-testers informed (assuming that you don't follow my [hg commits](http://hg.grml.org/) \[time for a hg\-commit mailinglist, yes]): today I spent several hours in reducing the todo list for grml 0\.9\. So make sure you have recent packages on [your brand new develrelease](http://blog.grml.org/archives/207-new-grml-develrelease-0.8-5.html) (run 'apt\-get update; apt\-get install $PACKAGES') when trying out. Quoting some important stuff of the changelogs:

```
grml2hd: adjust /etc/default/rcS according to bootoption utc/gmt
              and /etc/localtime according to bootoption tz
grml-autoconfig:
              * deprecate CONFIG_KERNEL, CONFIG_LANGUAGE,
                CONFIG_DMA and CONFIG_MIXER as they are not really
                relevant on hd installations.
              * do *not* use swap by default anymore, thanks for feedback
                 goes to Wolfgang Karall!
grml-terminalserver: a maintenance release to fix some outstanding issues:
             * big update of linuxrc - do not use discover anymore (broken)
                but instead try modprobing all available network modules
             * reject tcp/113 via iptables to speed up PXE boot
```
I consider the current state as pretty stable, in the next few days I'll do some more regression testing so hopefully we'll have a first release\-candidate of grml 0\.9 soon...
