---
author: Michael Prokop
categories:
- kernel
date: Sun, 17 Aug 2008 23:09:00 +0000
layout: post
slug: 284-the-way-grml-kernels-are-being-developed
title: the way grml kernels are being developed

---
In [news from the grml development front](http://blog.grml.org/archives/290-news-from-the-grml-development-front.html) a grml user named Dave [asked some questions](http://blog.grml.org/archives/290-news-from-the-grml-development-front.html#c207) regarding the grml kernel. As this seems to be not clear enough yet I'll write some sentences about the way the grml developers work on the grml kernel.
Daily grml builds (see [daily.grml.org](http://daily.grml.org/)) use a recent grml kernel version from the [grml\-testing](http://deb.grml.org/) repository. As the daily ISOs are being built automatically we have the need for a known\-to\-work kernel. grml wouldn't work in live mode without kernel modules like aufs and squashfs. Finally grml users are used to get [some additional kernel modules](http://grml.org/kernel/#modules) as well.
We *could* wait for a stable kernel 2\.6\.x.y with y being a stable patch/release with a version number \>\=10\. But then we would have the problem that our kernel might be pretty out of date when we release a new grml version. grml users expect to get good hardware support \- to acchieve that we need recent kernel versions. On the other side we don't want to upload a completely fresh and untested kernel to the grml repository even though it's "just" grml\-testing. grml\-testing is the place where we put stuff that will be available as a stable release once we consider it rocking solid. Of course there MIGHT be any issues left even though it's called a stable release, but thanks to our release cycle we have a pretty good test parcoure and try to identify and solve any possible breakages which shouldn't happen on any productive boxes outside the test world.
During our initial tests, configuration checks and verifying the upgrade path we also build external modules and in the meanwhile new stable updates (the y in the 2\.6\.x.y) appear which we can integrate into our kernel then. Therefor when releasing a new stable grml version we can provide an up2date kernel without forgetting about "rocking solid". HTH.
