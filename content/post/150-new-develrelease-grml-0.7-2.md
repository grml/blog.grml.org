---
author: Michael Prokop
categories:
- general
date: Sun, 30 Apr 2006 20:21:00 +0000
layout: post
slug: 150-new-develrelease-grml-0.7-2
title: new develrelease grml 0.7-2

---
We have a new develrelease. A lot of work took place. Quoting main changelog of my mail to betatesters and grml developers :
* added new packages (excluding xserver\* and lib\* stuff):  
 aircrack\-ng cdck cedet\-common classpath classpath\-common cpuid
 debian\-goodies fvwm fvwm\-crystal grep\-dctrl habak jamvm jikes
 mktemp mysql\-client\-5\.0 ndiswrapper\-common ndiswrapper\-utils\-1\.7
 openafs\-modules\-2\.6\.16\-grml pktstat pymacs python\-minimal
 python\-mode remind trayer tzdata unionfs\-tools wpagui wyrd
* updated to X.org 7\.0
* new default font (Lat15\-Terminus16\) on plain console* fixed problems mentioned @ [grml\-wiki grml 0\.7](http://wiki.grml.org/doku.php?id=grml_0.7)
* removed kaffe, added jikes and jamvm instead
* added scripts blacklist \+ unblacklist: \[un]blacklist a specific kernelmodule during runtime via /etc/modprobe.d/grml
* grml\-network: big update (see yourself :))
* grml\-postfix: reworked, now executing 'dpkg\-reconfigure postfix'
* grml\-autoconfig interface: read in already set values so the current configuration is visible to the user
* grml2hd: added support for setting hostname through script 'grml\-hostname'
* [reworked grml2hd\-utils](http://blog.grml.org/archives/154-reworked-grml2hd-utils,-improved-grml2hd.html)
* grml\-x completion: check for present window\-managers and don't use a static list
* added window manager fvwm\-crystal: we have to tune it a little bit (reduce size, adjust wallpaper, keybindings), but it definitely rocks! Give it a try and also take a look at [the keyboard bindings](http://linux.net.pl/~harnir/fvwm-crystal/doc/Keyboard%20bindings.txt)
