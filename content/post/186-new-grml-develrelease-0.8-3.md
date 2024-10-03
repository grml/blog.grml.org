---
author: Michael Prokop
categories:
- general
date: Wed, 11 Oct 2006 09:09:00 +0000
layout: post
slug: 186-new-grml-develrelease-0.8-3
title: 'new grml-develrelease: 0.8-3'

---
We have a new develrelease. grml 0\.8\-3 is available for [beta\-testers](http://grml.org/beta-tester/) and grml\-developers.
Quoting the main changelog:

```
  * added acx100, drbd8, spca5xx and truecrypt (for 2.6.18-grml)
  * new script random-hostname (print random hostname to stdout),
    integrated within grml2hd as well:)
  * grml-setlang: support all languages defined in
    /etc/grml/language-functions. Don't set $LC_ALL and $COUNTRY by
    default anymore.  Support non-interactive use via 'grml-setlang'.
  * rebuildfstab/scanpartitions:
    - added support for /dev/md*
    - improved fs-detection
    - support bootoption nolabel (don't generate label based fstab
      entries but plain, old style); use 'NOLABEL=1 grml-rebuildfstab'
      if you want to regenerate fstab without labels; force usage
      of labels via 'LABEL=1 grml-rebuildfstab' if you booted with'nolabel' but want to use labels anyway
    - support /etc/fstab.local (will be appended to end of
      /etc/fstab if the file exists)
    Please take a look at /etc/fstab and report any problems you consider!
  * hwinfo: using new release from Debian's pool, if you notice any
    problems with grml-x you didn't have until now, please report
    them!
  * new scripts (under development):
    - grml-bridge: set up your box as bridge
    - grml-router: set up your box as NAT-router
    - grml-ap: set up access point on your box
  * added /etc/skel/.irbrc ($HOME/irbrc), new shell aliases,...
```
