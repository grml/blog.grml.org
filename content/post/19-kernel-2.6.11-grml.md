---
author: Michael Prokop
categories:
- general
date: Thu, 03 Mar 2005 00:56:00 +0000
layout: post
slug: 19-kernel-2.6.11-grml
title: kernel 2.6.11[-grml]

---
While creating the grml ISOs for release 0\.3 I'm running same basic patching \+ compile tests with kernel 2\.6\.11\.

Compiling unionfs 1\.0\.9 against the new kernel worked like a charme, integration of squashfs2\.1\-r2 and patch\-2\.6\.11\-ck1 was also an easy task. 

iteraid.patch required some small adjustments (see [MOD\_\*\_USE\_COUNT macros were deprecated](https://lwn.net/Articles/103160/)).

Several other patches are waiting for integration.

Remember: if you want to see any special patches inside 2\.6\.11\-grml please drop me a mail \[mika (at) grml.org].
