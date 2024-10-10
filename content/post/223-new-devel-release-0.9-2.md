---
author: Michael Prokop
categories:
- general
date: Sun, 28 Jan 2007 19:52:00 +0000
layout: post
slug: 223-new-devel-release-0.9-2
title: 'new devel release: 0.9-2'

---
We have a new develrelease. grml 0\.9\-2 is available for [beta\-testers](https://grml.org/beta-tester/) and grml\-developers.
Quoting the main changelog:

```
  * *no* kernel update, I'm lacking time and 2.6.20 should be
     available soon, I don't want to put further work into 2.6.19 now
  * some updates for "utf8 mode by default", main issues should be
    resolved now (some problems are present inside GNU screen though)
    [notice: handling of unicode_start for hd-installation is on the
    todo-list: http://bts.grml.org/grml/issue75 ]
  * several bugfixes and updates in grml-network's netcardconfig,
    in grml-rebuildfstab and grml-scanpartitions
  * extended zsh configuration
  * big update and rewrite of zsh-lovers, thanks to Christian Schneider:
    {{< relref "221-update-of-zsh-lovers-in-asciidoc-format" >}}
  * added script gsuggest.pl: google suggest - ask google for
    keyword suggestions
  * Packages removed since 0.9 (excluding lib* and 2.6.18-grml):
    ethereal-common linux-wlan-ng linux-wlan-ng-firmware lout
    lout-common olsrd-plugin opie-server unionfs-utils xen-tools
    xen-utils-common
  * Packages added since 0.9 (excluding lib* and 2.6.19-grml):
    advchk cryopid dnsproxy fatresize flashplugin-nonfree funionfs
    gatling gems genisoimage icedax imsniff keyutils keyutils-lib
    kvm mcabber ncc olsrd-plugins pnputils python-urwid
    recordmydesktop scalpel smbnetfs tesseract-ocr-data uncrustify
    urlscan vde2 vinetto xserver-xorg-input-aiptek
    xserver-xorg-input-elo2300 xserver-xorg-input-elographics
    xserver-xorg-input-hyperpen xserver-xorg-input-joystick
    xserver-xorg-input-penmount xserver-xorg-input-void xwatchwin
```
