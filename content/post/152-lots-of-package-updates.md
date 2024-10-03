---
author: Michael Prokop
categories:
- packages
date: Sun, 14 May 2006 09:49:00 +0000
layout: post
slug: 152-lots-of-package-updates
title: lots of package updates

---
In the last two days I stepped through [the complete grml repository](http://grml.org/repos/) and updated most packages: updated to latest upstream version, some cleanups and finally I removed some packages (apachetoolbox, ccdv, ftester, mwcollect, shunit) which are deprecated nowadays (either not necessary at all or replaced by another package). Run 'apt\-get update ; apt\-get upgrade' on your grml\-box and see the changelog for more details.
