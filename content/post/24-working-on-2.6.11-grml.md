---
author: Michael Prokop
categories:
- general
date: Thu, 10 Mar 2005 23:41:58 +0000
layout: post
slug: 24-working-on-2.6.11-grml
title: working on 2.6.11-grml

---
I'm busy working on kernel 2\.6\.11\-grml. Currently the kernel includes the following patches:

```
1900_lowmem-reserve-oops.patch  
4100_skge-0.5.patch  
4300_2.6.11-rc3-udm2.patch  
4305_dm-bbr.patch  
4900_speakup-20050303.patch  
iteraid.patch  
linux-2.6.11-mppe-mppc-1.3.patch  
patch-2.6.11.1  
patch-2.6.11.2  
patch-2.6.11-ck1  
squashfs2.1-patch
```

Some other patches are waiting for integration (reiser4, orinoco\-rfmon\-dragorn,...). Some of them aren't ready for 2\.6\.11 but the kernel should be useful for testing already at this stage of development. I'll test it on my development machines, if everything works fine so far I'll integrate the kernel into the grml\-chroot so I can provide an updated devel\-ISO.
