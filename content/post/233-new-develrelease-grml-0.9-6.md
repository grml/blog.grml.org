---
author: Michael Prokop
categories:
- general
date: Sun, 25 Mar 2007 17:16:00 +0000
layout: post
slug: 233-new-develrelease-grml-0.9-6
title: 'new develrelease: grml 0.9-6'

---
After uploading [grml64]({{< relref "232-grml64-64-bit-version-of-grml" >}}) I also uploaded a new develrelease of grml (the 32bit version ;\-)) for beta\-testers and developers. So, what's new? Read yourself:

```
This release is a very special one for me. There are many updates,
fixes, addons - I could remove most of the release-stoppers
(http://bts.grml.org/release-stoppers). From my POV we are pretty
close to grml 1.0-rc1 now. But due to several updates it needs heavy
testing of course. So if you want to help us please test this
release and report *anything* you find and think should be fixed for
grml 1.0!
Main changelog:
===============
  * update of kernel 2.6.20-grml, now based on 2.6.20.3
    You're missing a feature/module/...? Report!
  * grml-terminalserver: big improvements like better module loading
    and switch to atftpd (thanks gebi) - give it a try!
  * grml2hd: added grml-setservices (interface for basic
    configuration of system startup/shutdown via
    /etc/runlevel.conf), improved grub code, some minor stuff...
  * added bootoption 'qemu', currently it does nothing else than
    copying /etc/X11/xorg.conf.example to /etc/X11/xorg.conf (if you
    have further ideas please inform me)
  * grml-autoconfig: dropped userspace/powernowd stuff in
    cpufrequeny scaling in favour of the ondemand-governor. If you
    notice any problems with powermanagement on your laptop please
    let me know.
  * news from grml-scripts:
    - added dirvish-setup: a simple script for setting up a basic
      configuration for backup software dirvish.
    - grml-setlang: do not set $TZ anymore, we want to handle it via
      /etc/timezone instead of /etc/default/locale; notice: the
      timezone configuration has been documented detailed at
      https://grml.org/faq/#timezone and within 'grml-tips timezone'
      Questions? Problems? Report!
    - integrated grml-quickconfig within zsh-login. grml-quickconfig
      has been contributed by Michael Schierl - thanks! [Needs some
      more tweaking though...]
    - added iso-term (wrapper script to run x-terminal-emulator in
      iso885915 mode).
    - added alignmargins (adjust the margins and the position of the
      printed contents on the paper)
  * /etc/zsh/zshrc: added aliases for better iso<->utf handling
    (term2iso, term2utf, utf2iso, iso2utf), big update of swspeak
    alias, added function ytdl (download video from youtube), and
    tons of other fixes, updates, additions...
```
