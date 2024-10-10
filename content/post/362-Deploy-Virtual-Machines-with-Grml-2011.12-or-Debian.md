---
author: Ulrich Dangel
categories:
- general
date: Fri, 16 Dec 2011 12:00:00 +0000
layout: post
slug: 362-Deploy-Virtual-Machines-with-Grml-2011.12-or-Debian
title: Deploy Virtual Machines with Grml 2011.12 or Debian

---
The upcoming Grml release 2011\.12 as well as Debian/testing and unstable ship an updated [grml\-debootstrap](https://grml.org/grml-debootstrap/) version supporting the installation of Debian not only into directories or hardisks but also into virtual images.

[grml\-debootstrap](https://grml.org/grml-debootstrap/) is designed to help you install complete Debian Systems. Typically if you install a Debian system with debootstrap you have to install the kernel, bootloader, /etc/fstab, ssh server, … yourself. grml\-debootstrap automates this boring tasks and allows you to install Debian systems from within a running system within minutes.

Nowadays physical installations get less and less important but virtual installation gain importance. New servers are often run inside virtual environments like Xen, KVM or VMware. grml\-debootstrap supports the automated installation of Debian into a virtualized environment without the need to use a preseeded installation medium. You can create a *raw* image with grml\-debootstrap which boots per default with KVM and Xen. To boot the image file with other virtualization solutions you may have to convert the generated image with *qemu\-img*

To install a plain Debian System into a raw image you just have to run
> grml\-debootstrap \-\-password root\-pw \-\-vmfile \-\-vmsize 3G \-\-target ./squeeze.img
  

This will set the root pasword to *root\-pw*, install openssh and the latest kernel package, create /etc/fstab with the necessary entries and configure the bootloader for your virtualized system.

If you want to customize or extend grml\-debootstrap have a look at [the manpage](https://grml.org/grml-debootstrap/) or look at the scripts and package definitions in */etc/debootstrap*
