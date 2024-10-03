---
author: Michael Prokop
categories:
- general
date: Sun, 24 Apr 2005 11:42:24 +0000
layout: post
slug: 51-developing-grml-on-grml
title: developing grml on grml

---
The box where I'm working on the grml\-kernel is a grml\-system and is running since grml 0\.2 without any problems. It has been installed using one of the earliest versions of grml2hd (the program for installing grml to harddisk).
Now it was time to install grml on my main developing machine: my laptop. That's the box where I'm doing my main work on grml.

Steps:

* booting grml (currently grml 0\.3\-4a)
* `grml2hd /dev/hda2 -mbr /dev/hda`
* adjusted `/etc/fstab` and `/etc/passwd` (I took over my old `/home` and of course `/Grml`)
* rebooting

That's it. It took not even 30 minutes to get a running and **working** Linux.
