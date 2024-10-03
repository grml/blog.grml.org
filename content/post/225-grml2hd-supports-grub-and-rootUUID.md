---
author: Michael Prokop
categories:
- packages
date: Thu, 15 Feb 2007 12:29:00 +0000
layout: post
slug: 225-grml2hd-supports-grub-and-rootUUID
title: grml2hd supports grub and root=UUID

---
I just finished main work of supporting grub directly within grml2hd and uploaded grml2hd\_0\.9\.3\_all.deb to the grml\-testing pool in those minutes. Now there's a new dialog in grml2hd which lets you choose between lilo and grub as bootloader:

[![screenshot of grml2hd](/images/grml2hd-grub.serendipityThumb.png)](/images/grml2hd-grub.png)[![screenshot of grub on grml-small](/images/grml2hd-grub2.serendipityThumb.png)](/images//grml2hd-grub2.png)

Notes:

* using grub on SW\-RAID devices is not yet supported
* grub configuration does not provide artwork currently. I'd be happy if someone could contribute a nice bootsplash for grub at grml!
* please do **not** use the testing version of grml2hd on your productive environment yet! It needs some further heavy testing before entering stable... any feedback is welcome of course.

Oh, and another nifty feature within grml2hd: installation now uses root\=UUID by default. This feature requires an initrd/initramfs so we use initramfs by default now (a dialog less within grml2hd) but you can make sure booting your grml system always choses the right partition, no matter how you are booting your system (like via external usb device):

[![screenshot of using root-uuid](/images/root-uuid.serendipityThumb.png)](/images/root-uuid.png)
