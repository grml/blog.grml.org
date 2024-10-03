---
author: Michael Prokop
categories:
- general
date: Thu, 16 Nov 2006 06:33:00 +0000
layout: post
slug: 199-new-grml-develrelease-0.8-5
title: 'new grml-develrelease: 0.8-5'

---
We have a new develrelease. grml 0\.8\-5 is available for [beta\-testers](http://grml.org/beta-tester/) and grml\-developers.
Quoting the main changelog:

```
   * Added support for detection and activation of SW-RAIDs in
     live-cd mode. Can be disabled via bootoption noraid (and is
     disabled as well through forensic and raid=noautodetect).
   * Added grml-debootstrap: wrapper around debootstrap for
     installing plain Debian via grml very simple and fast
   * Added script fma: shipped with grml 0.8-4 already but not yet
     mentioned, provides "fast manual access" (take a look at it!)
   * zsh:
     - new alias hidiff (highlight important stuff in diff
       output using histring) [thanks for the idea, T!]
     - added power completion, thanks wuehlmaus!
       See http://zshwiki.org/home/examples/zleiab for details.
       Notice: this deactivates the global aliases by default now,
       just use the global aliases as well but press ',.' afterwards
       to expand the abbreviation! Trust me: you should know and use
       it! :-)
   * Fixed some issues in configuration framework handling, thanks
     for the reports, Marc Haber!
   * language stuff: added support for Norsk environment, thanks to
     Arnt Karlsen! [not yet visible in grml-setlang though]
   * grml-bootsplash: replaced the clear command with
     "echo -ne '\033[H\033[25l'" to avoid flickering at bootoption'splash'. Thanks a lot, Michael Schierl!
```
