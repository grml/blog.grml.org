---
author: Michael Prokop
categories:
- general
date: Fri, 30 Oct 2009 23:56:00 +0000
layout: post
slug: 325-Changes-between-grml-2009.10-rc1-and-grml-2009.10
title: Changes between grml 2009.10-rc1 and grml 2009.10

---
If you're interested in the main changes between rc1 of 2009\.10 and the final stable release:
Changes in all flavours:
* updated grml2hd: bugfixes (adjust grub handling to support grub2, fix handling of custom bootoptions in bootloaders, fix grub support in non\-interactive mode), added support for ext4 and some further minor updates/bugfixes
* updated grml2usb: integration of grml2usb\-compat, updates for new features in grml\-live, updated grml2iso (copy additional files to ISO, better support for grml2usb), support removal of bootoptions, use dynamic check for addons as current grml\-small includes addons, support running on a generated grml2usb iso/directory
* updated grml\-autoconfig: bugfixes (font\-handling in non\-framebuffer mode, handling of grml.sh)
* updated grml\-debootstrap: added support for and use support grub2 by default, dropped $GROOT and modified usage of $GRUB, replaced vol\_id command with blkid, use cdn.debian.net as default mirror
* updated grml\-docs: update files for release
* updated grml\-etc: bugfixes (eject handling)
* updated grml\-tips: added further tips, updated existing ones
* updated grub\-pc \+ grub\-common (stable release)
* kernel 2\.6\.31\-grml\[64]: update to new version based on stable release 2\.6\.31\.5
Changes in flavour grml/grml64:
* added ewf\-tools, fio \+ guymager
* updated grml\-live: direct integration of grub1, update and direct integration of grub2, gPXE, update of ldbsd.com
* updated firmware\-iwlwifi, firmware\-qlogic \+ firmware\-ralink (feature update)
* updated grml\-terminalserver: drop support for grub.img (fails to build with recent toolchains, use gPXE/etherboot instead), integrated grml2usb for generating pxeconfig
* dropped deprecated grml\-terminalserver\-data \+ ash packages
Changes in flavour grml\-medium/grml64\-medium:
* updated firmware\-iwlwifi \+ firmware\-ralink (feature update)
* updated grml\-live: direct integration of grub1, update and direct integration of grub2, gPXE, update of ldbsd.com
* updated grml\-terminalserver: drop support for grub.img (fails to build with recent toolchains, use gPXE/etherboot instead), integrated grml2usb for generating pxeconfig
* dropped deprecated grml\-terminalserver\-data \+ ash packages
Changes in flavour grml\-small/grml64\-small:
* added parted
