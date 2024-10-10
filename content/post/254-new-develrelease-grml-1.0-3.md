---
author: Michael Prokop
categories:
- general
date: Wed, 05 Sep 2007 22:25:00 +0000
layout: post
slug: 254-new-develrelease-grml-1.0-3
title: 'new develrelease: grml 1.0-3'

---
After the [Froscon event]({{< relref "251-grml-at-FrOSCon-2007-and-Linux-User-Group-Moenchengladbach" >}}) took place we have a new develrelease. Quoting the main changelog for the new develreleases:

```
  * several updated configuration files, bugfixes and
    up2date Debian packages as of 20070905
  * atl2 kernel driver added
  * grml2hd: display '***' in password box so user gets feedback when
    typing the password
  * ctrl-alt-del triggers reboot instead of powerdown now
  * use of live-initramfs: the biggest change inside 1.0-3 and the
    one which will break everything. ;-) But: as a long-term
    side-effect it will dramatically simplify customizing grml and
    provide new options like including firmware for booting.
    'ls -la /' looks completely different now as you will notice.
    We have a new unionfs overlay layout. Let's see whether it's
    working for us.
    So please: test all the grml bootoptions and let us know what's
    broken!
```
