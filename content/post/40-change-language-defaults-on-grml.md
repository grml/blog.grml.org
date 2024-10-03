---
author: Michael Prokop
categories:
- general
date: Sat, 09 Apr 2005 15:11:00 +0000
layout: post
slug: 40-change-language-defaults-on-grml
title: change language defaults on grml

---

```
sed -i 's#init=/etc/init lang=us#init=/etc/init lang=de#' grml_0.3.iso
```
That's all you have to do if you don't want to manually set bootoption 'grml lang\=de'. :\-)
Notice: Please verify md5sum of ISO (not just the ISO itself but also the CD\-ROM via booting with 'grml testcd') **before** modifiying the ISO because the modification breaks the md5sum of course. ;\-)
