---
author: Michael Prokop
categories:
- packages
date: Wed, 21 Sep 2005 19:06:00 +0000
layout: post
slug: 106-fullautomatic-grml-installation
title: fullautomatic grml-installation

---
I just implemented the code for running grml2hd in full automized mode. This means you can run:

    # GRML2HD_NONINTERACTIVE=yes grml2hd

... drink some coffee and some minutes later \- without any further interaction \- you have a full functional linux system on your harddisk. Configuration of grml2hd is possible via /etc/grml2hd/config. You can even run pre\- and post\-commands to partition your harddisk automatically, run upgrades without interaction or whatever you like.
Now I will implement a bootoption 'grml2hd' which allows booting and installing grml without any further interaction right out of the box. This means it will be possible to set up a cluster of \- let's say for example \- 30 computers in a computer lab without any further interaction just via using grml with grml2hd and grml\-terminalserver.
