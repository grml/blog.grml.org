---
author: Ulrich Dangel
categories:
- general
date: Thu, 22 Dec 2011 13:00:00 +0000
layout: post
slug: 366-Upcoming-accessibility-changes-for-Grml-2011.12
title: Upcoming accessibility changes for Grml 2011.12

---
The upcoming Grml 2011\.12 will have some changes in the accessibility features shipped with Grml. Until Grml 2011\.12 it was possible to start brltty automatically via the bootoption brltty. The problem with this approach was that it was never clear when you had to enter the bootoptions as there was no sound to indicate boot menu. We also do not have the necessary hardware to test the releases with brltty. With that in mind and the integration of speakup in the kernel we decided to remove the additional accessibility boot\-parameters for Grml 2011\.12 as we never tested them anyway.   
 

But we added some important changes to improve the accessibility. Starting with Grml 2011\.12 the bootloader will either beep once (if you use the default syslinux one) or will play 3 beeps (grub) to indicate the boot menu. Afterwards you can easily change the boot parameters if you press TAB (syslinux) or e (Grub). After the bootup Grml will play some tunes to indicate the finished boot. As per default Grml starts a text based menu you will have to press enter after the beep to enter the commandline

We think with the additional sound indicators in the boot\-menu as well as the default sound to indicate the finished boot\-process, Grml 2011\.12 will be more accessible then ever.

I would like to thank Richard Hartmann for creating the different sound indicators for the upcoming Release
