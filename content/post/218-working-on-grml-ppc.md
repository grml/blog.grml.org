---
author: Michael Prokop
categories:
- general
date: Mon, 22 Jan 2007 22:02:00 +0000
layout: post
slug: 218-working-on-grml-ppc
title: working on grml-ppc

---
As written in [my personal blog](http://michael-prokop.at/blog/) I'm running [Debian on my ppc efika board](http://michael-prokop.at/blog/2007/01/17/debian-on-the-efika-board/) already. Now I've a first, working grml\-kernel for ppc:

```
# uname -a
Linux grmlppc 2.6.19-grml #2 PREEMPT Sat Jan 20 20:26:15 CET 2007 ppc GNU/Linux
```
Now I can really start working on grml\-ppc on my own. The plan is to have grml64 and grml\-ppc available with release of grml 1\.0\.
Currently I'm [crosscompiling the kernel on x86](http://michael-prokop.at/blog/2007/01/21/cross-compile-the-linux-kernel-on-debian/). It works but it would be nice to have a more powerful compile system, especially another (native) ppc system would be fine....
