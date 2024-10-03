---
author: Michael Prokop
categories:
- general
date: Mon, 28 Feb 2005 14:27:07 +0000
layout: post
slug: 15-new-bootparams-nocolor-+-log
title: 'new bootparams: nocolor + log'

---
Finally we have working `nocolor` and `log` bootparams. nocolor disables colorized output while booting, log starts bootlogd and logs all stderr\-output to an extra file. (nocolor isn't just for pragmatists but avoids color sequences in the bootlog ;\-))
