---
author: Michael Prokop
categories:
- packages
date: Sat, 26 Feb 2005 22:53:42 +0000
layout: post
slug: 11-removed-packages
title: removed packages

---
I added several packages since release 0.2 to my `grml-chroot`. As usual I try to create an ISO with exactly 700 MB. My last ISO had 710MB.

    # apt-get remove --purge printconf foomatic-db-gimp-print

The result was an ISO with still about 705MB. So:

    # apt-get remove --purge autotrace libautotrace3 libmagick++6 libplot2 libpstoedit0

I hope to get a 700MB version now. Notice: If you have any special wishes on software which should be removed/included please let me know, last chance for grml 0\.3\. :\-)
