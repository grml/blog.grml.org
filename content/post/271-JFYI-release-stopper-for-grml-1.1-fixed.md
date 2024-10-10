---
author: Michael Prokop
categories:
- general
date: Fri, 15 Feb 2008 16:05:00 +0000
layout: post
slug: 271-JFYI-release-stopper-for-grml-1.1-fixed
title: 'JFYI: release stopper for grml 1.1 [fixed]'

---
We have a new release stopper, see [issue 400 in grml's BTS](http://bts.grml.org/grml/issue400). Current grml release candidate doesn't boot on older hardware. We are investigating on that issue, please read the according [thread on the syslinux mailinglist](http://syslinux.zytor.com/archives/2008-February/009401.html) for further details. If you you have an affected system as well ("my box does not boot with grml 1\.1\-rcX but does with grml 1\.0") [please let us know](https://grml.org/contact/)!
**Update:** Thanks to Andrea Mayr and Wernfried Haas for testing lots of ISOs we could locate the problem finally. Read my [mail on syslinux mailinglist](http://syslinux.zytor.com/archives/2008-February/009444.html) for details. Now we are working on finalizing the ISOs and do some last regression tests. If murphy does not catch us again we will release the stable version this weekend.
