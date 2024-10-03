---
author: Michael Prokop
categories:
- general
date: Sun, 18 Feb 2007 22:07:00 +0000
layout: post
slug: 226-new-develrelease-0.9-3
title: 'new develrelease: 0.9-3'

---
We have a new develrelease. grml 0\.9\-3 is available for [beta\-testers](http://grml.org/beta-tester/) and grml\-developers.
Quoting the main changelog:

```
  * kernel 2.6.20-grml
    Notice: not all *extra*, external modules are available yet but
    I think the most important ones are there, see
    http://dufo.tugraz.at/~prokop/grml-kernel/2.6.20-grml/ for details
  * several updates regarding utf8 handling: all known issues should
    be resolved now - if you notice any further problems regarding
    utf8/language/... please report them!
  * grml2hd: support for grub and use of UUID by default
    http://blog.grml.org/archives/233-grml2hd-supports-grub-and-rootUUID.html
    Notice: the grub code is new, there *might* be bugs present
    even though I tested it carefully, so don't use it on your
    productive environment unless you really want to. :)
  * fixed issues known from previous develreleases
  * several updates of configuration files
  * Does anyone of you suffer from the "timezone problem" with grml?
    http://bts.grml.org/grml/issue82
    If so please contact me! Thanks to Jan-Pieter Jacobs we might
    have a fix for the problem but I need your feedback.
```
