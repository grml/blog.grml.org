---
author: Michael Prokop
categories:
- general
date: Tue, 12 Sep 2006 09:05:00 +0000
layout: post
slug: 174-new-develrelease-grml-0.8-1
title: 'new develrelease: grml 0.8-1'

---
I just uploaded a new develrelease for [beta\-testers](http://grml.org/beta-tester/) and grml\-devs. All the mounting\-stuff as discussed on the [grml\-user mailinglist](http://grml.org/mailinglist/) has been implemented. Quoting the main part of the Changelog:

```
* Fixed the issues of grml 0.8 mentioned on
  http://wiki.grml.org/doku.php?id=grml_0.8 (only the bt-net stuff
  does not work yet, Gebi is working on it)
* /mnt/usb-sd* feature - see Thread "RFC: handling of external usb
  devices" on grml-user mailinglist for details =>
  http://thread.gmane.org/gmane.linux.distributions.grml.user/466/focus=466
* grml-rebuildfstab (that's an shell command now as well, just run'grml-rebuildfstab' to rebuild /etc/fstab!) supports fs-LABELs and
  UUIDs; rebuilfstab now takes care of /mnt/*-directories as well - see
  http://thread.gmane.org/gmane.linux.distributions.grml.user/466/focus=507
  http://article.gmane.org/gmane.linux.distributions.grml.user/508
  and "man rebuildfstab" for details.
  Notice: Running "apt-get update ; apt-get install grml-autoconfig \
  grml-rebuildfstab grml-scanpartitions udev" should bring you the
  /mnt/usb-sd* and new fstab features to your harddisk installation
  of grml.
* Removed the bitmap-fonts packages xfonts-100dpi-transcoded and
  xfonts-75dpi-transcoded. I couldn't notice any font-related
  problems, if you do notice some please let me know!
* Added FreeDOS 1.0 from the Balder project; boot into it using the
  bootoption 'dos'
* Updated the adp94xx scsi kernel module [also in the initrd]
  (thanks, jimmy)
* Extended grml-tips: several new tips regarding mdadm, lvm-stuff,...
* Updated packages to debian-pool by 2006-09-11
* New packages (excluding lib*):
  aria2 ccontrol cdrskin classpath-gtkpeer ddccontrol ddccontrol-db
  firmware-qlogic iwatch medusa openbsd-inetd python-jaxml
  python-selinux python-semanage queuegraph reniced smap stealth
  unionfs-modules-2.6.17-grml wodim xen-utils-common xmms2
  xmms2-client-cli xmms2-core xmms2-plugin-alsa xmms2-plugin-id3v2
  xmms2-plugin-jack xmms2-plugin-mad xmms2-plugin-vorbis
* Removed packages (excluding lib*):
  jaxml netkit-inetd ppmtofb python2.4-selinux scanerrlog
  xfonts-100dpi-transcoded xfonts-75dpi-transcoded
```
