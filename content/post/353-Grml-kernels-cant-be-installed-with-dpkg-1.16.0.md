---
author: Christian Hofstaedtler
categories:
- kernel
date: Sat, 02 Apr 2011 20:26:22 +0000
layout: post
slug: 353-Grml-kernels-cant-be-installed-with-dpkg-1.16.0
title: Grml kernels can't be installed with dpkg 1.16.0

---
dpkg 1\.16\.0 has entered Debian/unstable yesterday, and contains a change which currently prevents installation of Grml kernel packages. Quoting the changelog from dpkg version 1\.16\.0:

> Do not allow versions starting with non\-digit when doing strict parsing, warn otherwise.

We have opened a [bug against dpkg (\#620566\)](http://bugs.debian.org/620566) as we believe that the new behavior in dpkg is more strict than the current Debian policy.

Also, we are currently working on updated Grml kernel 2\.6\.38 packages providing a version number that won't cause problems with dpkg 1\.16\.0 in the meanwhile.

  
**Update:** Updated kernel packages which work around the dpkg bug have been uploaded to the grml\-testing repository.