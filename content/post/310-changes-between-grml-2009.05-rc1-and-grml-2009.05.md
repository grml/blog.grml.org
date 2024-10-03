---
author: Michael Prokop
categories:
- general
date: Mon, 01 Jun 2009 11:11:00 +0000
layout: post
slug: 310-changes-between-grml-2009.05-rc1-and-grml-2009.05
title: changes between grml 2009.05-rc1 and grml 2009.05

---
If you're interested in the main changes between rc1 of 2009\.05 and the stable release:
* software related changes: security updates; re\-added bitlbee, dnsproxy, farpd, tor and trickle; dropped ifupdown\-scripts\-zg2 and open\-vm\-tools
* grml64: windows directory (featuring putty, psftp,...) has been removed due to lack of space
* zsh: added support for [directory specific shell configuration using profiles](http://michael-prokop.at/blog/2009/05/30/directory-specific-shell-configuration-with-zsh/)
* bugfix: grml\-autoconfig: device with label GRMLCFG without file config.tbz causes error message \[[issue672](http://bts.grml.org/grml/issue672)]
* bugfix: grml2hd: mount /dev/pts and /dev to chroot to support execution within GNU screen; fix setting password via chpasswd
* bugfix: unmount boot device when using findiso\=... in combination with toram
