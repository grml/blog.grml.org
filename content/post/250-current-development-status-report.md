---
author: Michael Prokop
categories:
- general
date: Sun, 01 Jul 2007 21:26:00 +0000
layout: post
slug: 250-current-development-status-report
title: current development status report

---
I continued work on shortening our [bugreports, wish\- and todolist](http://bts.grml.org/grml/) in the last few weeks. New features include:
* bootoption startup for starting a script when booting finished, usage example: 'grml startup\=netcardconfig'
* LVM (logical volumes) support in the booting process, providing bootoption 'lvm' now
* grml2hd supports installation on LVM devices also in interactive mode, all you have to do is set up LVM is you want it to and then invoke 'LVM\=/dev/mapper/$target grml2hd'
* support dvorak keyboard layout via bootoption lang\=dvorak and lang\=dvorak\-iso as well as keyboard\=dvorak and xkeyboard\=dvorak
More to come in the next few days... going back to development now...
