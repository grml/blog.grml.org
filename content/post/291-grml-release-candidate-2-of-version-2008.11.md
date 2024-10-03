---
author: Michael Prokop
categories:
- general
date: Fri, 28 Nov 2008 16:25:00 +0000
layout: post
slug: 291-grml-release-candidate-2-of-version-2008.11
title: grml release candidate 2 of version 2008.11

---
Release candidate 2 of grml 2008\.11 is available via [debian.netcologne.de/www.grml.org/devel/](http://debian.netcologne.de/www.grml.org/devel/). Main changes from rc1 to rc2:* Updated Debian packages by 2008\-11\-20
* Implemented [isofrom and tohd bootoptions](http://git.grml.org/?p=grml-live.git;a=blob_plain;f=templates/GRML/grml-cheatcodes.txt;hb=HEAD).
* Disabled NOPERSISTENT\='Yes' in live\-initramfs configuration
* Removed CONFIG\_SECURITY\_SMACK from kernel, fixes [issue568](http://bts.grml.org/grml/issue568)
* Major update of [grml\-debootstrap (version 0\.23\)](http://ml.grml.org/pipermail/grml-testing-changes/2008-November/000316.html)
* Some minor updates and fixes in grml related scripts and configurations.
* Updated documentation.

The stable release is expected to be released on this weekend (end of november), so please grab rc2 and give it a try.