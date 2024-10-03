---
author: Michael Prokop
categories:
- general
date: Sat, 28 Oct 2006 11:30:00 +0000
layout: post
slug: 192-new-grml-develrelease-0.8-4
title: 'new grml-develrelease: 0.8-4'

---
We have a new develrelease. grml 0\.8\-4 is available for [beta\-testers](http://grml.org/beta-tester/) and grml\-developers.
Quoting the main changelog:

```
  * fixed known issues from develrelease 0.8-3
  * updated kernel 2.6.18-grml:
    http://blog.grml.org/archives/199-updated-kernel-2.6.18-grml.html
  * grml2hd has a new feature: it's possible to customize grml2hd's
    execution via a configuration file named
    /etc/grml2hd/customization. Using this feature you can toggle
    which functions of grml2hd should be executed when running
    grml2hd.
  * switched to mplayer version available in Debian/unstable
  * OOTB support for vmmouse driver if running grml inside vmware
  * many minor updates, lots of cleanups, new shell
    aliases/functions,... [just too many too mention all]
Packages removed since 0.8 (excluding lib* and *2.6.17-grml*;
notice: some of them are available under a differnet name now):
  apache2-common bluez-pin bookmarkbridge camgrab cdw cdw-common
  cthumb divine dnotify drbd0.7-utils gcj-4.1-base gconf2-common
  grml-kerneladdons grml-reportbug ht jaxml lout-doc lpr
  mozilla-mplayer mplayer-nogui ndiswrapper-utils-1.7 netkit-inetd
  ppmtofb python2.3-pymad python2.3-pyopenssl python2.3-pyparsing
  python2.3-twisted-bin python2.4-selinux python2.4-semanage
  scanerrlog stunnel turkey xfonts-100dpi-transcoded
  xfonts-75dpi-transcoded xorg x-window-system-core
Packages added since 0.8 (excluding lib* and *2.6.18-grml*):
  ace-of-penguins afflib apache2.2-common aria2 automake ccontrol
  cdrskin classpath-gtkpeer conntrack cupsys-bsd ddccontrol
  ddccontrol-db diakonos diction drbd8-utils dwm-tools dynafont
  emacs emelfm firmware-qlogic glipper grml-etc-core
  grml-kerneladdons-2.6.18 guessnet ink inotail inotify-tools iwatch
  konwert konwert-filters latex-ucs mathomatic medusa misdn-utils
  mpg123-alsa mplayer ne obexpushd openbsd-inetd pax-utils ptfinder
  python2.5 python2.5-minimal python-jaxml python-pymad
  python-selinux python-semanage python-twisted-bin qtparted rake
  rdoc rdoc1.8 reniced reportbug resolvconf ruby-prof sic smap
  ssdeep stealth stunnel4 synergy sysvinit-utils update-inetd
  vim-python vim-ruby wodim xen-utils-common xmms2 xmms2-client-cli
  xmms2-core xmms2-plugin-alsa xmms2-plugin-id3v2 xmms2-plugin-jack
  xmms2-plugin-mad xmms2-plugin-vorbis xserver-xorg-input-vmmouse
  youtube-dl
```
