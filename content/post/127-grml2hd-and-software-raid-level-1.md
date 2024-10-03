---
author: Michael Prokop
categories:
- general
date: Sun, 11 Dec 2005 00:20:00 +0000
layout: post
slug: 127-grml2hd-and-software-raid-level-1
title: grml2hd and software raid (level 1)

---
I just added support for installing grml on software RAID level 1 with grml2hd. As we already have support for initrds it wasn't such a big deal. \[Disclaimer: it's not a frontend for mdadm, you have to use mdadm manually on your own. If you want to use software RAID you should know how to handle it anyway.]
So if you want to use RAID1 with '/' on software\-raid run mdadm and install grml afterwards on the new created device using the environment variable SWRAID which passes the provided option to the raid\-extra\-boot\-option in lilo.conf:  

```
# mdadm --create --verbose /dev/md0 --level=raid1 \  
        --raid-devices=2   /dev/hda1  /dev/hdc1  
# SWRAID='mbr-only' grml2hd /dev/md0 -mbr /dev/md0
```
That's it. :\-)
