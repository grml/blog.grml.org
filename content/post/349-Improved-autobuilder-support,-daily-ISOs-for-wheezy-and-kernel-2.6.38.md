---
author: Michael Prokop
categories:
- general
date: Fri, 18 Mar 2011 15:15:00 +0000
layout: post
slug: 349-Improved-autobuilder-support,-daily-ISOs-for-wheezy-and-kernel-2.6.38
title: Improved autobuilder support, daily ISOs for wheezy and kernel 2.6.38

---
[daily.grml.org](http://daily.grml.org/) includes ISOs for the upcoming Debian release with codename "wheezy" (being Debian/testing nowadays). All daily ISOs starting with 18th of march also provide [the brand new kernel 2\.6\.38\-grml](http://blog.grml.org/archives/358-Kernel-2.6.38-grml-available.html).
The workflow for grml\-live distribution to the build server has been improved as well: once a day, right before the daily ISOs are being built, the build server automatically builds a Debian package based on the git tree of grml\-live. This means all changes to grml\-live.git end up on the daily ISOs on the next day without any manual intervention. The autobuilt packages are available at [http://amd64\.grml.org/grml\-live\-daily/](http://amd64.grml.org/grml-live-daily/).
