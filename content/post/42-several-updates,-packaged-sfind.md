---
author: Michael Prokop
categories:
- packages
date: Sat, 09 Apr 2005 23:32:00 +0000
layout: post
slug: 42-several-updates,-packaged-sfind
title: several updates, packaged sfind

---
Yesterday I updated all my packages to latest upstream source (md5deep\-1\.5, mg\-5\.0\.1\.3, ptunnel\-0\.55, sitar\-0\.9\.0, spl\-0\.0\.svn\+r301, trapdoor2\-1\.2, weplab\-0\.1\.4,...). I also added manpages to some packages which don't bring one out of the box (aesutil, apachetoolbox, bashburn, bkhive, ccdv, edictionary, httpf,...).

Thanks to Gebi, now we have a clean patch against upstream/debian sysvinit for grml\-sysvinit\-0\.3\.

A few weeks ago one user reported feedback about [iteraid.patch for 2\.6\.11](http://grml.org/kernel-devel/iteraid.patch). I/O was quite slow but worked in general. Today another user reported problems with his setup (two disks on the ITE\-RAID). As the patch isn't supported neither by Gigabyte nor by kernelupstream I'm thinking about dropping the patch for release 0\.4\. Feedback welcome.

Today I packaged [sfind](http://freshmeat.net/projects/sfind/) (Jörg Schilling's find\-implementation). I also added [smake](http://packages.debian.org/unstable/devel/smake) (Schily make) to the grml\-chroot.
