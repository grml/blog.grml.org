---
author: Michael Prokop
categories:
- kernel
date: Tue, 07 Nov 2006 22:32:00 +0000
layout: post
slug: 196-updated-kernel-2.6.18-grml-version-03
title: updated kernel 2.6.18-grml - version 03

---
I updated the kernel [2\.6\.18\-grml](http://dufo.tugraz.at/~prokop/grml-kernel/2.6.18-grml/) once more. Summary: inclusion of 2\.6\.18\.2 and sync with Debian's svn kernel repository. The patch\-list in detail:

```
1000_2.6.18.2.patch
2400_net-netpoll.patch
2500_via-irq-quirk-revert.patch
2510_sym2-dont-claim-raid-devs.patch
4000_net-r8169-1.patch
4001_net-r8169-hotplug_loop.patch
4002_net-r8169-no_mac_adress_change.patch
4003_net-r8169-pci_id-corega.patch
4005_sky2-v1.9.patch
4010_net-forcedeth-swsusp.patch
4100_cciss-support-for-gt-2TB-volumes.patch
4105_dm-bbr.patch
4110_promise-pdc2037x.patch
4115_advansys-pci-id-table.patch
4120_buslogic-pci-id-table.patch
4150_iteraid.patch
4200_drm-i965.patch
4300_squashfs-3.1.patch
4310_fs-asfs.patch
4400_speakup-20060814.patch
4410_scsi-ahci-cleanup-1.patch
4411_scsi-ahci-cleanup-2.patch
4412_scsi-ahci-cleanup-3.patch
4413_scsi-ahci-cleanup-4.patch
4420_scsi-ahci-suspend-1.patch
4421_scsi-ahci-suspend-2.patch
4422_scsi-ahci-suspend-3.patch
4430_scsi-arcmsr-1.patch
4431_scsi-arcmsr-2.patch
4432_scsi-arcmsr-3.patch
4440_fintek-f75375.patch
5000_grml-version.patch
5001_grml_logo.patch
5002_commandlinesize.patch
```
More details available in the [grml\-kernel repository](http://hg.grml.org/grml-kernel/).
