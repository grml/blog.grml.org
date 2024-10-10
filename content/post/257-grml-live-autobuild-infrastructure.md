---
author: Michael Prokop
categories:
- general
date: Fri, 28 Sep 2007 23:01:00 +0000
layout: post
slug: 257-grml-live-autobuild-infrastructure
title: grml-live - autobuild infrastructure

---
Thanks to the infrastructure provided by [IBM's x305 server donation](https://grml.org/donations/) and [Jimmy's](https://grml.org/team/) work I just finished a first prototype setup of an autobuild system for building grml\-ISOs using [grml\-live](https://grml.org/grml-live/). Currently I've a working system for building "*grml\-medium*" ISOs based on etch/stable and sid/unstable on a daily base. Normal/full grml ISOs (the \~700MB version) of etch/stable and sid/unstable will follow soon. I plan to provide new develreleases as soon as I finished the autobuild setup. Hopefully we'll find ressources for a 64bit environment (so we can provide autobuilded ISOs of grml64\) as well.
