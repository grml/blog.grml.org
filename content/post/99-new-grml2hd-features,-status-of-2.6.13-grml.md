---
author: Michael Prokop
categories:
- packages
date: Mon, 05 Sep 2005 02:49:00 +0000
layout: post
slug: 99-new-grml2hd-features,-status-of-2.6.13-grml
title: new grml2hd features, status of 2.6.13-grml

---
Today I worked a lot on grml2hd (the grml\-installer) and it's features. First of all it's possible to use grml2hd with grml\-small now. This means you can get a linux installation on a \>\=200MB harddisk system. ;\-)

I also integrated the grml\-autoconfig framework within grml2hd. There's a script namend grml\-autoconfig which is the interface to the grml\-autoconfig framework's configuration file /etc/grml/autoconfig. And finally there are some other small improvements not visible to the user but useful for the bootup sequence. I also improved the grml\-autoconfig\-framework itself \- some parts of the config\-framework have been merged into the code. I also worked on the script mkpersistenthome and the home\=...\-bootparam: both are essential parts of the config\-framework and have to work with grml 0\.5\.

Kernel 2\.6\.13\-grml works quite fine but it does not work on the live\-cd\-system yet. The reason is that there's one bug left in unionfs and therefor I'll have to wait until unionfs\-developers resolve the bug and release a snapshot supporting kernel 2\.6\.13\. In the meanwhile I'm working on the config\-framework...