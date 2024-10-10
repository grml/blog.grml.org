---
author: Michael Prokop
categories:
- general
date: Thu, 18 Oct 2007 21:20:00 +0000
layout: post
slug: 261-Daily-grml-snapshots
title: Daily grml snapshots

---
[![Build statistics - screenshot](/images/build-stats.serendipityThumb.png)](/images/build-stats.png)

In the last few weeks I've been busy working on **[grml\-live](https://grml.org/grml-live/)** (the build framework based on [FAI](http://www.informatik.uni-koeln.de/fai/) for generating a grml and Debian based Linux Live system). As generating a new grml\-ISO using grml\-live can be done with *one single command*(!) we could finally build an autobuild system which generates daily snapshots of grml. Thanks to hosting by [formorer](https://grml.org/team/#formorer) and [jimmy](https://grml.org/team/#jimmy) we can provide a wide range of different flavours of grml now:

* **[grml\-small](https://grml.org/faq/#whatissmall):** as usual that's the smallest version of grml; due to growing packages the ISO size is \~110MB currently \- we are trying to reduce the ISO size further....
* **grml\-medium:** a *new grml flavour* with the purpose of closing the gap between grml\-small and normal/large/full grml. Currently it's pending at about 140MB ISO, we want to keep the ISO size at a maximum of 200MB
* **grml:** as usual, the big, normal, large, full version of grml with a maximum ISO size of 700MB, providing *all* the grml features

That's not all. We provide all these versions in a **32bit version** (grml) as well as in a **64bit version** (grml64\). But stop! We even provide all the versions in a **Debian/stable based** and a **Debian/unstable based** version.

You can choose your favourite grml\-ISO from a total of 3x2x2 \= **12 different ISOs**. They are available from [daily.grml.org](http://daily.grml.org/) and are built full automatic on a daily base. This should help us in tracking down possible problems in Debian packages as well as keeping [the truck factor](http://www.agileadvice.com/archives/2005/05/truck_factor.html) in our team as low as possible and improve quality management furthermore. On the other side users can get brand new software for testing, or if they need a special feature (like a [brand new kernel version]({{< relref "260-kernel-2.6.23-grml" >}})) they can get it without the need for waiting for a new devel\-/stable\-release. So just grab the current snapshot for testing from [daily.grml.org](https://daily.grml.org/), or if you want to build your own Linux live\-cd based on Debian and grml consider the use of [grml\-live](https://grml.org/grml-live/).
