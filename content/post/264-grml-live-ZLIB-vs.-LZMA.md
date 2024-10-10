---
author: Michael Prokop
categories:
- general
date: Sun, 09 Dec 2007 15:53:00 +0000
layout: post
slug: 264-grml-live-ZLIB-vs.-LZMA
title: 'grml-live: ZLIB vs. LZMA'

---
I just made some benchmarks between ZLIB and LZMA compression at squashfs, thanks to [grml\-live](https://grml.org/grml-live/) (which provides a commandline option and config option for switching) that's a trivial task now:

* grml flavour: grml\-medium
* using LZMA: 164MB ISO, build time 725 seconds
* using ZLIB: 183MB ISO, build time 254 seconds

So whereas the build time increases the benefit is a smaller ISO, which is quite important for live systems that want to ship as many useful tools as possible. :\-)

