---
author: Michael Prokop
categories:
- packages
date: Fri, 25 Feb 2005 17:13:58 +0000
layout: post
slug: 7-schedtool
title: schedtool

---
I stumbled upon [schedtool](http://freequaos.host.sk/schedtool/) via [ck's audio hints](http://ck.kolivas.org/audio_hints.txt) and just packaged it. As usual it's available via [the grml\-repository](http://grml.org/repos/).

Seems to work:

    root@grml ~ # schedtool $$  
    PID 1903: PRIO 0, POLICY N: SCHED_NORMAL, NICE 0  
    root@grml ~ #
