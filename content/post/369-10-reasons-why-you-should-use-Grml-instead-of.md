---
author: Ulrich Dangel
categories: []
date: Tue, 27 Dec 2011 13:00:00 +0000
layout: post
slug: 369-10-reasons-why-you-should-use-Grml-instead-of
title: "10 reasons why you should use Grml instead of \u2026"

---
With the release of [Grml 2011\.12](https://grml.org/changelogs/README-grml-2011.12/?pk_campaign=blog&pk_kwd=10reasons) we were regularly asked what distinguishes Grml from other Live\-CDs. The following items lists some reasons why you should consider using Grml instead of another Distribution for Installation\&Rescue :
* handy scripts, like [grml\-chroot](https://grml.org/online-docs/grml-chroot.8.html), a wrapper around chroot which will automatically bind /dev, /sys and /proc to the chroot
* the **```
netscript
```** boot option. This option will download an executable from the network and execute as root
* [grml\-debootstrap](https://grml.org/grml-debootstrap/), a tool for automated Debian installations
* [grml2usb](https://grml.org/grml2usb/) simple but powerful tools to create customized Grml images within minutes
* ZSH as default shell with a very good and comfortable [zshrc](http://git.grml.org/f/grml-etc-core/etc/zsh/zshrc)
* the **```
netconfig
```** boot option. This option will download an archive from the network and unpack it on top of the current root filesystem
* automatically start the ssh server with the **```
ssh
```** boot\-parameter
* Boot your Grml ISO\-image directly from your existing GRUB setup with [loopback.cfg](http://www.supergrubdisk.org/wiki/Loopback.cfg)
* Create your own customized Grml Distribution with the same tool we release our ISO\-images: [grml\-live](https://grml.org/grml-live/)
* start arbitrary services without remastering the squashfs, just specify the the **```
service
```** boot option
* EFI support, we arrived late with it but we support it now out of the box even with grml2usb



What are your reasons using [Grml](https://grml.org/?pk_campaign=blog&pk_kwd=10reasons) instead of other Live CDs? What are you missing from Grml?
