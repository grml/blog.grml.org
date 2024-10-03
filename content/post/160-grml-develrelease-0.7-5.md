---
author: Michael Prokop
categories:
- general
date: Sat, 24 Jun 2006 18:10:00 +0000
layout: post
slug: 160-grml-develrelease-0.7-5
title: grml develrelease 0.7-5

---
Last wednesday I uploaded the new grml develrelease 0\.7\-5\. Quoting the changelog:

```
* 2.6.17-grml:
  http://blog.grml.org/archives/163-2.6.17-grml.html
  - reiser4 is *not* part of the kernel. Anyone out there missing it?
  - ipw3495 is part of the kernel, the daemon is missing though
[...]
  - I'm thinking about integration of swsusp2 - any votes?
  TODO-list for 2.6.17-grml:
  http://dufo.tugraz.at/~prokop/grml-kernel/2.6.17-grml/TODO
* integrated fvwm-crystal-minimal (packaged by myself, you can find
  it in the grml-repos; replaces fvwm-crystal for space-reasons)
* dropped gcc/g++ 4.0, providing 4.1 instead as the kernel is
  compiled with 4.1
* vi points to vim instead of elvis (thanks, Wolfgang Karall)
* updated packages to debian-pool by 2006-06-21
```
Now I've finished work on the ipw3495 stuff: ipw3945\-ucode and ipw3945d are available in the grml repository. The ipw3495 module works out\-of\-the\-box on grml now.
Running some more tests with different kernel configurations showed that swsusp2 very probably won't find its way to the grml\-kernel. On the other hand the tests with SMP were very good, so we might have SMP\-support in grml 0\.8\. Stay tuned. :\-)
The TODO list for the the current build of 2\.6\.17\-grml is also very short now: only ivtv and linux\-wlan\-ng are missing. I'll package truecrypt, tpm\-emulator and grml\-kerneladdons for 2\.6\.17\-grml as soon as the final build of 2\.6\.17\-grml is available.
