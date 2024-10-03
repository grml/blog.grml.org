---
author: Michael Prokop
categories:
- kernel
date: Mon, 07 Sep 2009 16:38:00 +0000
layout: post
slug: 322-kernel-2.6.31-grml64
title: kernel 2.6.31-grml[64]

---
After busy development days the kernel 2\.6\.31\-grml and 2\.6\.31\-grml64 entered the grml\-testing pool today. This kernel version is based on upstream's 2\.6\.31\-rc9 and features the squashfs file format version 4 with lzma support.
Please note that you need [squashfs\-lzma\-tools 4\.0\-1](http://ml.grml.org/pipermail/grml-testing-changes/2009-September/000490.html) for remastering with grml\-live if you plan to use LZMA compression. grml\-live has been adjusted to be as backwards friendly as possible. Check out '[current state of grml\-live with squashfs\-tools and kernel](http://grml.org/grml-live/#current_state)' for further details if you plan to build your own ISOs.
An updated [live\-initramfs 1\.157\.3\-1grml.00](http://ml.grml.org/pipermail/grml-testing-changes/2009-September/000489.html) package is available as well. Starting with tomorrow (2009\-09\-08\) the [daily builds of grml](http://daily.grml.org/) should feature kernel 2\.6\.31\-grml\[64] already. This means we are coming closer to a new stable release...
