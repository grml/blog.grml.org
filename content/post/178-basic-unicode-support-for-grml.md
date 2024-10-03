---
author: Michael Prokop
categories:
- general
date: Sat, 23 Sep 2006 22:50:27 +0000
layout: post
slug: 178-basic-unicode-support-for-grml
title: basic unicode support for grml

---
Today I completely rewrote the language stuff in grml\-autoconfig. After designing a much more capabable and cleaner system I rewrote the code (e.g. removed the functions config\_environment and config\_keyboard which are integrated more smoothly in config\_language now) and added support for Unicode/UTF\-8\. Now you just have to boot using 'grml lang\=$LANG\-utf8' and all the environment stuff is adjusted without any further manual input for you! Thanks to a new shellscript named grml\-setlang it's also possible to adjust language related environment variables when booting your harddisk installation. grml\-setlang also allows you to \*interactive\* configure your language stuff on grml. After running lots of tests I couldn't notice any problems so far \- the new code should be completely backwards compatible. But I've to do some more regression testing and test X\-related stuff before the new packages are going into the grml\-repos (including some documentation). Expect to find the new features in the next grml develrelease (and of course in grml 0\.9 afterwards ;\-)).
