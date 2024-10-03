---
author: Michael Prokop
categories:
- general
date: Fri, 13 Jul 2007 22:15:00 +0000
layout: post
slug: 253-new-develrelease-grml-1.0-1
title: 'new develrelease: grml 1.0-1'

---
Lots of development took place in the last weeks, finally we have a new develrelease. Quoting the main changelog for the new develreleases:

```
  * featuring new stable kernel 2.6.22
    See http://bts.grml.org/grml/issue216 for details regarding
    development and progress.
  * *no* further speakup patch inside the kernel, see
    http://braille.uwo.ca/pipermail/speakup/2007-June/043478.html
    for the reason
  * update to libc 2.6; packages from Debian pool by 2007-07-13
  * grml-x with multihead support using Xinerama ->
      % grml-x -xinerama ...
    Notice: this is limited to two monitors currently and I can test
    it only on my intel based Samsung X20 laptop. Please report
    feedback if you give it a try! Patches are welcome as well. :)
  * some small improvements in bootsequence when running inside
    VirtualBox
  * grml2hd supports installation on LVM devices through
    'LVM=/dev/mapper/target grml2hd'
  * added bootoption startup=$script to startup the provided
    $script/application instead of grml-quickconfig
  * support LVM (logical volumes) in boot sequence:
    - bootoption 'lvm' activates them
    - no special bootoption just runs 'lvdisplay' and if something
      can be found the user gets a hint to execute 'Start lvm2' to
      set it up
    - bootoption 'nolvm' completely disables the lvm code/checks
  * Due to the emacs21 to emacs22 migration the following packages are not
    yet available:
      auctex:      http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=432206
      python-mode: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=424973
    Whereas the other removed packages "gnus gnus-bonus-el w3-el-e21
    w3-url-e21" shouldn't be necessary with the new emacs version
    AFAICS.
  * the fluxbox theme (~/.fluxbox/styles/Sn33z) is broken with the
    current version. Just delete it manually or choose another theme
    from the fluxbox menu. Would be great if someone could take a
    closer look at fixing this issue!
  * the windows/ directory on the ISO has been renamed (currently
    only for now) due to space problems....
  * several bugfixes, updated configuration files,...
```
