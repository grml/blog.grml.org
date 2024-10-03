---
author: Michael Prokop
categories:
- kernel
date: Mon, 23 Oct 2006 21:24:00 +0000
layout: post
slug: 191-updated-kernel-2.6.18-grml
title: updated kernel 2.6.18-grml

---
An updated version of [kernel 2\.6\.18\-grml is available](http://dufo.tugraz.at/~prokop/grml-kernel/2.6.18-grml/). The [patchlist for 2\.6\.18\-grml](http://hg.grml.org/grml-kernel?mf=bf5b83244328;path=/2.6.18/;style=gitweb):

```
1000_2.6.18.1.patch
2500_via-irq-quirk-revert.patch
4005_sky2-v1.9.patch
4010_r8169-8168.patch
4105_dm-bbr.patch
4110_promise-pdc2037x.patch
4150_iteraid.patch
4300_squashfs-3.0.patch
4400_speakup-20060814.patch
5000_grml-version.patch
5001_grml_logo.patch
5002_linux-2.6.17-commandline.patch
```
As you might notice reiser4 is not part of the kernel (and unless there's an official patch this won't change for the upcoming grml\-release). The external modules lufs, nozomi, thinkpad and vaiostat don't compile against 2\.6\.18 yet, the rest of the work has been done. I'm already running grml 0\.8\-3d with this kernel version. A new develrelease will be available within the next few days...
