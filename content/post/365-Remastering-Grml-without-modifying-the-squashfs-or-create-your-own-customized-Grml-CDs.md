---
author: Ulrich Dangel
categories:
- general
date: Wed, 21 Dec 2011 13:00:00 +0000
layout: post
slug: 365-Remastering-Grml-without-modifying-the-squashfs-or-create-your-own-customized-Grml-CDs
title: Remastering Grml without modifying the squashfs or create your own customized
  Grml CDs

---
In [our last Blog entry about remastering Grml 2011\.12]({{< relref "364-Remastering-Grml-2011.12-will-be-as-easy-as-never-before" >}}) we described a method remastering Grml with [grml\-live](https://grml.org/grml-live/), the tool used to generate the official Grml ISOs.

Often you don't need all the power and flexibility of grml\-live but just want to add or change some default boot parameters and use this as your default image. For example you may want to have an ISO image which automatically starts sshd and sets the password to a specific value or downloads an executable and run it at startup. This can easily be done with *grml2iso* a tool based on [grml2usb](https://grml.org/grml2usb/) which allows you to create customized iso images.

Grml will automatically start sshd and set the password for the grml user if you specify the [ssh boot\-parameter](http://git.grml.org/?p=grml-live.git;a=blob_plain;f=templates/GRML/grml-cheatcodes.txt;hb=HEAD). This allows you to remotely control your Grml CD. To create such a CD just run:
> grml2iso \-b "ssh\=grml\-password" \-o my\_grml.iso ./grml64\_2011\.12\.iso

This will create a modified Grml ISO named *my\_grml.iso* and add the bootparameter *ssh\=grml\-password* to all the existing boot\-entries.

grml2usb does not offer the same flexibility as grml\-live but grml2usb/grml2iso is often good enough to help you to achieve what you want without the need to modify the squashfs file.
