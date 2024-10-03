---
author: Michael Prokop
categories:
- general
date: Tue, 21 Jun 2005 10:52:00 +0000
layout: post
slug: 75-kernel-2.6.12-grml
title: kernel 2.6.12-grml

---
A first public version of Kernel 2\.6\.12\-grml is available. It includes support for reiser4, vesafb\-tng, squashfs, mppe/mppc and iteraid:

```
mika@grml ~ % uname -a  
Linux grml 2.6.12-grml #1 SMP Mon Jun 20 15:20:40 CEST 2005 i686 GNU/Linux
```

The debian\-package plus several modules built against 2\.6\.12\-grml are available [online](http://dufo.tugraz.at/~prokop/grml-kernel/2.6.12-grml/).
I'm working on a (better) framework for the grml\-kernel (using dpatch\+debian/...). Expect to find broken\-out (d)patches and some more information on [grml.org/kernel\-devel/](http://grml.org/kernel-devel/ "grml kernel-devel") soon. Feedback and help welcome!
