---
author: Chris Hofstaedtler
categories:
- general
- kernel
date: Mon, 07 Oct 2024 11:55:11 +0200
layout: post
slug: "416-grml32-sunset"
title: "Sunsetting grml32 releases"

---
Since [2007](https://blog.grml.org/archives/232-grml64-64-bit-version-of-grml.html) Grml is available for two different architectures for PCs: grml32 ("i386", 32-bit) and grml64 ("amd64", 64-bit). The grml64 releases, and the underlying Debian "amd64" were introduced for PCs with more than 4GB of memory, and the then "upcoming" new CPUs, spear-headed by AMD.

In the meantime the PC landscape changed a lot. [Intel jumped](https://en.wikipedia.org/wiki/X86-64) on the "amd64" train, and abandoned their own ia64 ("Itanium") design. Modern PCs often do not properly support the old 32-bit architecture anymore. Even PCs manufactured ten years ago can boot grml32 and grml64. No new 32-bit only CPUs are manufactured, and no new features got added. Testing grml32 became a lot harder, and testing on a "real 32-bit only" hardware is now impossible for us.

Linux kernel upstream also is losing interest and time to support the 32-bit architecture (just called "x86") there. The Debian kernel team decided to [stop building Linux kernel packages](https://salsa.debian.org/kernel-team/linux/-/commit/a18e683900b4f5ffb30dd18b8481cbdc66e7a34a) starting with Linux 6.11.

As Grml releases are dependent on Debian kernel packages, this decision also *ends the line* for grml32.

Users who really need grml32 due to lack of 64-bit support on their hardware can still use Grml 2024.02, which will be the last release with a grml32 build. However, we encourage users to migrate to more modern, possibly used, hardware instead.

***

Only one thing left to say, to the classic Intel 32-bit x86, "i386", or whatever you want to call it architecture:

> So long, and thanks for all the fish.
