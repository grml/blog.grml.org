---
author: Michael Prokop
categories:
- general
date: Sun, 17 Dec 2006 23:08:00 +0000
layout: post
slug: 211-new-develrelease-0.9-1
title: 'new develrelease: 0.9-1'

---
We have a new develrelease. grml 0\.9\-1 is available for [beta\-testers](http://grml.org/beta-tester/) and grml\-developers.
Quoting the main changelog:

```
  * kernel 2.6.19-grml
  * use utf8 by default:
    - when using lang=$LANG it defaults to utf8, it's possible to
      use lang=$LANG-utf8 as well for backward compability
    - fallback to iso is possible through bootoption lang=$LANG-iso
    - now using Uni3-Terminus14 as default font instead of
      Lat15-Terminus16 which should improve use of utf8 on console;
      very probably I'll change the font to Uni3-Terminus16
  * update Debian packages to pool by today (except initramfs-tools
    which is once again broken, using an older version therefore)
  * grml2hd should work on SW-RAID again, installs
    /etc/grml2hd/config with permissions 600 now so possible sensible
    data can't be read by non-root
  * zsh: use of global dirstack, this allows switching directories
    via "cd -<press_tab>" also when running a new/fresh shell
    session (thanks schula + ft)
  * some minor bugfixes, improvements,...
```
