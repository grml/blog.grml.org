---
author: Michael Prokop
categories:
- general
date: Sat, 02 Dec 2006 15:54:00 +0000
layout: post
slug: 208-new-Debian-repositories-for-grml
title: new Debian repositories for grml

---
Please notice that grml has new Debian package repositories as announced on [the grml user mailinglist](http://lists.mur.at/mailman/listinfo/grml). Please adjust the line containing grml.org/repos/ in your /etc/apt/sources.list to something like:

```
# stable grml repository:
  deb     http://deb.grml.org/ grml-stable  main
  deb-src http://deb.grml.org/ grml-stable  main
```
See [the announce mail](http://lists.mur.at/pipermail/grml/2006-December/001159.html) for more details.
