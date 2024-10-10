---
author: Michael Prokop
categories:
- packages
date: Sun, 17 Aug 2008 23:00:00 +0000
layout: post
slug: 285-Current-state-of-grml-live-with-squashfs-tools-and-kernel
title: Current state of grml-live with squashfs-tools and kernel

---
I was busy working on getting [grml\-live](https://grml.org/grml-live/) in a good shape together with squashfs\-tools, live\-initramfs and the new kernel version 2\.6\.26\-grml. A new squashfs\-tools package is available as well as an updated live\-initramfs package. It does not support LZMA compression (yet) but it's working fine with ZLIB compression so far. Right now I'm building an updated 2\.6\.26\-grml kernel, 2\.6\.26\-grml64 will follow.
As soon as the new kernels are ready\-to\-go I will upload them together with grml\-live 0\.9 to the grml\-testing repository. Updating our [daily.grml.org](http://daily.grml.org/) buildhost will provide daily ISOs featuring 2\.6\.26\-grml . New development versions of grml will follow so we can provide a new stable release in the near future.
See the "[Current state of grml\-live with squashfs\-tools and kernel](https://grml.org/grml-live/#X8)" section if you are interested in further details.
