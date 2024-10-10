---
author: Ulrich Dangel
categories:
- general
date: Thu, 15 Dec 2011 12:00:00 +0000
layout: post
slug: 361-ATA-over-Ethernet-and-Grml
title: ATA over Ethernet and Grml

---
**Update on 2011\-12\-20 by Grml team:** while iscsitarget isn't available any longer on Grml [the new iSCSI implementation of the Linux kernel 3\.1](http://kernelnewbies.org/Linux_3.1#head-392b21286de0ce98e30ee8e561ca2f567522ea59) is available and open\-iscsi, targetcli and tgt are shipped with Grml. We don't have any finished documentation for that yet, but if you know how to use targetcli (or optionally open\-iscsi and tgt) you should have everything you need to provide a iscsi target with Grml 2011\.12\.

The upcoming Grml Release 2011\.12 (check the changelog for our [new Grml 2011\.12\-rc1](https://grml.org/changelogs/README-grml-2011.12-rc1/?pk_campaign=Blog&pk_kwd=201112rc1)) will not have any iSCSI support integrated due to build issues with dkms. Instead Grml 2011\.12 will provide all the necessary tools to provide and access a ATA over Ethernet Device.

ATA over Ethernet, also known as AoE, is a protocol designed to access Block devices via Ethernet. Compared to iSCSI it does not work with IP but with Ethernet. Unfortunately this means that AoE is error\-prone against Ethernet attacks like ARP spoofing. Do not use it in hostile enviornments. That being said AoE is quite simple to use.

#### Export a blockdevice
 
On the server side use vblade to export a block device:
> vblade \-m 11:22:33:44:55:66 160 2 eth0 /dev/sdb1

  
This will allow the host with the MAC 11:22:33:44:55:66 to access /dev/sdb1 via eth0, using the shelf and slot numbers 160 and 2\. These numbers are arbitrary but should be unique within the network.

#### Access a blockdevice

On the client load the module "aoe", or do

> aoe\-discover
  
You should find the device shared above as /dev/etherd/e160\.2

I would like to thank to Christoph Biedl for providing this short and comprehensive documentation
