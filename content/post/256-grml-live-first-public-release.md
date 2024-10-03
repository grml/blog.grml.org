---
author: Michael Prokop
categories:
- packages
date: Thu, 20 Sep 2007 16:06:00 +0000
layout: post
slug: 256-grml-live-first-public-release
title: grml-live - first public release

---
Time for an update on the [grml\-live front](http://blog.grml.org/archives/263-grml-live-create-your-own-grml-ISO.html). I just uploaded the first public version of [grml\-live](http://grml.org/grml-live/) to [the grml\-repos](http://deb.grml.org/pool/main/g/grml-live/).
Lots of development [took place](http://hg.grml.org/grml-live/). New features include support for local mirrors (thanks to Michael Schmitt for providing test infrastructure), new command line options and unified classes. Oh, and you ever wanted to use grub as bootloader instead of isolinux on your grml ISO? Now it's as trivial as setting BOOT\_METHOD\=grub in /etc/grml/grml\-live.conf before running grml\-live itself, giving you something like:
[![](/images/gkrellShoot_07-09-20_151049.serendipityThumb.png)grub as bootloader for grml](/images/gkrellShoot_07-09-20_151049.png)So what are you waiting for? [Grab grml\-live](http://deb.grml.org/pool/main/g/grml-live/), build your very own grml version and send me your feedback, feature requests and bugreports. :\-)
