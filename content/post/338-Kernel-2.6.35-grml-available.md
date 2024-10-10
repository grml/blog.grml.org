---
author: Michael Prokop
categories:
- kernel
date: Sun, 05 Sep 2010 10:24:00 +0000
layout: post
slug: 338-Kernel-2.6.35-grml-available
title: Kernel 2.6.35-grml available

---
Thanks to excellent work by Gebi the squashfs\-lzma issue for the new kernel could be solved. Now I'm proud to be able to announce a full\-featured kernel 2\.6\.35\-grml\[64] which is available from the Grml grml\-testing repository.
grml\-live 0\.11\.0 is available as well, featuring support for kernel 2\.6\.35\-grml. The new squashfs\-lzma patches in kernel 2\.6\.35 aren't using the openwrt style format any longer but instead use the official on disk layout from mainline. That's why a new squashfs\-tools package is required to properly support kernel 2\.6\.35\-grml\[64]. This package is available as *squashfs\-lzma\-tools4*. All you've to do to get a kernel 2\.6\.35\-grml\[64] based live system is upgrading to grml\-live \>\=0\.11\.0, install squashfs\-lzma\-tools4 and grml\-live will take care of the rest *automatically* for you. For further details regarding the current state of squashfs\-lzma in Grml please have a look at [the official grml\-live documentation](https://grml.org/grml-live/#current_state).
BTW: The current [daily ISOs](http://daily.grml.org/) feature the new kernel version already, so give it a shot while it's hot! :)
