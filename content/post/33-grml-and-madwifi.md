---
author: Michael Prokop
categories:
- packages
date: Sun, 27 Mar 2005 20:51:00 +0000
layout: post
slug: 33-grml-and-madwifi
title: grml and madwifi

---
Thanks to beta\-tester Jürgen 'Stormchild' Oesterle who reported that grml lacks of madwifi\-support. I just added the necessary stuff:

```
grml@grml ~ % locate ath_pci  
/lib/modules/2.6.11-grml/kernel/drivers/net/ath_pci.ko  
grml@grml ~ % dpkg --get-selections|grep madwifi  
madwifi                                         install  
madwifi-module-2.6.11-grml                      install  
madwifi-tools                                   install
```
