---
author: Michael Prokop
categories: []
date: Thu, 07 Jan 2016 09:27:53 +0000
layout: post
slug: 394-Is-Grml-still-alive
title: Is Grml still alive?

---
Grml's latest stable release as of today still is 2014\.11 and folks are poking us about the current state of Grml and upcoming stable releases. Thanks to our daily ISOs available at [daily.grml.org](http://daily.grml.org/) more up2date versions *are* available, though we understand and agree that a new stable release is overdue.

Sadly since quite some time we're stuck with a release stopper, being a [regression in udev](http://bts.grml.org/grml/issue1568) which is visible only if you do *not* use systemd. Grml is using file\-rc as its init system and while the migration to systemd was on our agenda no one took care of this so far. Support for systemd is work in progress though now. We hope to have a new stable release of Grml available in Q1 of 2016!

**tl;dr:** Grml is still alive :)
