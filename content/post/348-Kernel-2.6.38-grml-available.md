---
author: Michael Prokop
categories:
- kernel
date: Thu, 17 Mar 2011 22:13:00 +0000
layout: post
slug: 348-Kernel-2.6.38-grml-available
title: Kernel 2.6.38-grml available

---
Only two days after Linus released Kernel 2\.6\.38 we already have it in the grml\-testing repository! Besides the usual AUFS support it also features mainline's squashfs XZ support, meaning no extra squashfs patch needed anymore to get support for LZMA (now known as XZ). Our build tool [grml\-live(8\)](http://grml.org/grml-live/) already supports this kernel version and uses XZ compression with squashfs\-tools \>\=1:4\.2\-1 by default.
Please note: If you want to use current grml\-live version (\>\=0\.13\.1\) with older kernel versions than 2\.6\.38 don't forget to point SQUASHFS\_BINARY to the according mksquashfs binary and set SQUASHFS\_OPTIONS accordingly. If you want to build older versions without any hassles you can still use old grml\-live versions of course (as provided and shipped with each Grml release).
Bottom line, XZ support in mainline (kernel \>\=2\.6\.38 and squashfs\-tools \>\=4\.2\) will provide a better upgrade cycle for grml\-live and the grml environment.
