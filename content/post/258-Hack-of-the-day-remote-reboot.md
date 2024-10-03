---
author: Michael Prokop
categories:
- general
date: Sat, 29 Sep 2007 09:54:00 +0000
layout: post
slug: 258-Hack-of-the-day-remote-reboot
title: 'Hack of the day: remote-reboot'

---
I had to clone a server to another server (1:1 copy using dd\+netcat) but didn't want to stay at the customer's place until the task finished. So I executed 'Start ssh; passwd' to be able to login remotely. But how to reboot the server and get rid of the CD so the harddisk system boots instead of the grml\-CD without manual interaction at customer's place? Server systems usually don't move in/re\-insert an ejected CD on reboot \- that's nice for what we need. So all I had to do was:

```
eject &>/dev/null
umount -l /cdrom
eject /dev/cdrom
echo b > /proc/sysrq-trigger
```
