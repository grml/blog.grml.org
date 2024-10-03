---
author: Michael Prokop
categories:
- general
date: Tue, 26 Apr 2005 10:19:46 +0000
layout: post
slug: 53-grml-running-on-reiserfs
title: grml running on reiserfs

---
Today I added support for reiserfs to grml2hd:

```
mika@grml ~ % mount | grep reiser
/dev/hda5 on / type reiserfs (rw)
```
