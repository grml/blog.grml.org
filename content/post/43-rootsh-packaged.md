---
author: Michael Prokop
categories:
- packages
date: Sun, 10 Apr 2005 13:08:00 +0000
layout: post
slug: 43-rootsh-packaged
title: rootsh packaged

---
I packaged [rootsh](http://sourceforge.net/projects/rootsh/) and added it to the grml\-chroot.

Rootsh is a wrapper for shells which logs all echoed keystrokes and
terminal output to a file and/or to syslog. It's main purpose is the
auditing of users who need a shell with root privileges. They start
rootsh through the sudo mechanism.
