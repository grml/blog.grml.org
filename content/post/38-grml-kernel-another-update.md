---
author: Michael Prokop
categories:
- general
date: Sat, 02 Apr 2005 09:28:00 +0000
layout: post
slug: 38-grml-kernel-another-update
title: 'grml-kernel: another update'

---
Another update of kernel 2\.6\.11\-grml. Tobias Klauser and me applied some additional patches from kernel\-source\-2\.6\.11 by Debian:

```
1900_lowmem-reserve-oops.patch
2900_alps-tapping.patch
4100_skge-0.6.patch
4300_2.6.11-rc3-udm2.patch
4305_dm-bbr.patch
4900_speakup-20050303.patch
aml_method_exec_hack.patch
drivers-add-scsi_changer.patch
drivers-ide-dma-blacklist-toshiba.patch
drivers-media-video-v4l-mpeg-support.patch
fs-asfs-2.patch
iteraid.patch
linux-2.6.11-mppe-mppc-1.3.patch
orinoco-2.6.11-rfmon-dragorn-1.diff
patch-2.6.11.6
reiser4.allinone
squashfs2.1-patch
tty-locking-fixes9.patch
vesafb-tng-0.9-rc6-2.6.11-rc1.patch
```

The kernel and several modules are [available online](http://dufo.tugraz.at/~prokop/grml-kernel/). Please [report any problems](https://grml.org/contact/) you notice!
