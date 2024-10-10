---
author: Michael Prokop
categories:
- general
date: Thu, 17 Nov 2005 21:54:00 +0000
layout: post
slug: 122-compile-farm-using-grml
title: compile farm using grml

---
At [Graz University of Technology](http://www.tugraz.at/) (TUG) several software projects have big compile jobs. Yesterday I've been working on a specialized grml version to create a compile farm within some few minutes. And the result: grml\-distcc. grml\-distcc includes a 2\.6\.14\-kernel optimized for up to 32 processors. There's a new bootparam named 'distcc' with the options $NETWORK and $INTERFACE which provides access to the distcc\-daemon for the defined network listening on the ip address of the given interface. Usage example: 'grml distcc\=192\.168\.0\.1,eth0'.
Today [Hecka and me](https://grml.org/team/) tested grml\-distcc at TUG. As we are lazy guys and don't want to play disc jokey with a lot of grml\-CDs ;\-) we booted grml\-distcc via network. Running 'grml\-terminalserver' on the server, configuring bootoptions for distcc within the interface of grml\-terminalserver and booting client via PXE was everything we had to do. Afterwards access to the distcc\-clients was possible through "export DISTCC\_HOSTS\=$HOSTS\_WHERE\_DISTCC\_IS\_RUNNING". Running 'make \-j' was fun of course. :\-)
The distcc bootparam will be probably part of the upcoming grml release.
[![](/images/distcc.serendipityThumb.jpg)](/images/distcc.jpg)
