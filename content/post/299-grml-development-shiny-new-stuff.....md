---
author: Michael Prokop
categories:
- general
date: Mon, 02 Mar 2009 22:09:00 +0000
layout: post
slug: 299-grml-development-shiny-new-stuff....
title: grml development - shiny new stuff....

---
After the [bug squashing party](http://wiki.grml.org/doku.php?id=bsp) lots of further development took place. The most important stuff:* grml2usb: initial public version of the redesign, providing multi\-ISO support and many more features, check out [grml.org/grml2usb](https://grml.org/grml2usb/) and my [mail to the grml mailinglist](http://lists.mur.at/pipermail/grml/2009-March/004397.html)
* boot process: when using the "forensic" or the new "readonly" bootoption all local harddisks will be *forced* to read\-only mode
* grml\-autoconfig: dropped /etc/grml/autoconfig.small
* grml\-live: several bugfixes, integration of bsd4grml (available via 'bsd' on the bootprompt \- more details will follow later),... \- check out [the changelog](http://ml.grml.org/pipermail/grml-testing-changes/2009-February/000354.html)
* grml\-etc\-core: using "zsh: $REPOSNAME" as GNU screen title name when standing inside a repository of a version control system (thanks, ft!)
* git\-commits: the [git\-commits mailinglist](http://ml.grml.org/mailman/listinfo/git-commits) finally provides the according hook so updates are sent to the list
