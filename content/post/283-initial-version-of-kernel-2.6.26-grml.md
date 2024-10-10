---
author: Michael Prokop
categories:
- kernel
date: Sun, 27 Jul 2008 09:59:00 +0000
layout: post
slug: 283-initial-version-of-kernel-2.6.26-grml
title: initial version of kernel 2.6.26-grml

---
A first version of kernel 2\.6\.26\-grml is ready to go:
```
% uname -a
Linux okely-dokely 2.6.26-grml #1 SMP PREEMPT Sun Jul 27 00:10:16 CEST 2008 i686 GNU/Linux
```

Now work on external modules will start, if you want to follow progress of work on kernel 2\.6\.26\-grml check out our [grml\-kernel mercurial repository](http://hg.grml.org/grml-kernel/). If you want to get the kernel using Debian's package management even before it's available through grml's repository add the following line to your /etc/apt/sources.list and install linux\-image\-2\.6\.26\-grml then:
```
deb https://grml.org/2.6.26 ./
```

Please notice that we are testing migration to libata with this kernel so if you use root\=/dev/hd.. in your bootloader config make sure to switch to root\=/dev/sd.. or even better use root\=UUID\=... (see [stable root device aka UUID](http://michael-prokop.at/blog/2006/08/11/stable-root-device-aka-uuid/) for more details) instead.