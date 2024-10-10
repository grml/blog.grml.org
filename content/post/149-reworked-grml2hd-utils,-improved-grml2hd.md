---
author: Michael Prokop
categories:
- packages
date: Thu, 27 Apr 2006 21:21:00 +0000
layout: post
slug: 149-reworked-grml2hd-utils,-improved-grml2hd
title: reworked grml2hd-utils, improved grml2hd

---
grml2hd\-utils seems to be quite unknown as it isn't visible in any interfaces by default. Now I've reworked it for better integration within grml2hd. You might know remove\-packages\-server already, the script which removes packages you probably don't want on your grml harddisk system. The new 'install\-packages\-useful' script is similar to [Ubuntu's 'Easy Ubuntu'](http://easyubuntu.freecontrib.org/overview.html) and provides very simple installation of some useful packages (guess why the name ;\-)). install\-packages\-office allows you to install OpenOffice, Gimp and some other packages useful at offices. grml2hd\-fix fixes some small issues from the grml Live\-CD, nothing serious to worry about \- it's just for getting debsums running without warnings. ;\-)
Finally: grml2hd allows you to set hostname, as too many people don't know how to manage this using Debian's available mechanism.
The features will be shipped with the next develrelease which will be available soon for [betatesters](https://grml.org/beta-tester/).
