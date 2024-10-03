---
author: Michael Prokop
categories:
- packages
date: Sat, 12 Apr 2008 23:08:00 +0000
layout: post
slug: 278-bug-475783-mounting-loopback-device-fails-in-initrd
title: 'bug #475783 - mounting loopback device fails in initrd'

---
Using current versions of busybox (1:1\.9\.2\-2\) fails with kernel 2\.6\.23\-grml and [grml\-live](http://grml.org/grml-live/), see my bugreport [\#475783](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=475783) for more details. I've just uploaded an older version of busybox (1:1\.1\.3\-5\) to the [grml\-live repository](http://deb.grml.org/) for use with [grml\-live](http://grml.org/grml-live/) which brings back a working setup.