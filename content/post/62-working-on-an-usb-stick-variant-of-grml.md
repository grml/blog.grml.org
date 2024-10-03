---
author: Michael Prokop
categories:
- general
date: Mon, 16 May 2005 11:04:00 +0000
layout: post
slug: 62-working-on-an-usb-stick-variant-of-grml
title: working on an usb-stick variant of grml

---
Yesterday I've been working for an USB\-stick variant of grml. I could reduce the ISO from nearly 700 MB down to 307 MB:

```
% ls -lah grml_0.4b.iso
-rw-r--r--  1 root root 307M 2005-05-16 12:40 grml_0.4b.iso
```
All the documentation, LaTeX and stuff like emacs had to leave. Booting still works as intented to, even X is running. ;\-) Now I've to reduce the iso for another 51 MB so we can provide a grml\-ISO for a 256 MB stick.
