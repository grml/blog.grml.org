---
author: Michael Prokop
categories:
- packages
date: Mon, 17 Jul 2006 22:49:00 +0000
layout: post
slug: 162-language-selection-within-grml2hd,-status-report
title: language-selection within grml2hd, status report

---
Currently I'm working on language support within grml2hd so you can easily select your prefered language and keyboard settings via grml\-setlang and grml\-setkeyboard. Works fine so far, we just have to do some more testing.
Jimmy wrote a partition selector for grml2hd which should make live easier for grml2hd\-newbies. :\-)
I slightly improved some configuration files and scripts. An absolutely great feature has been integrated: osd\_server.py by Ulrich Dangel, Rico Schiekel and Alexander Bernauer. Special thanks to Ulrich 'schula' Dangel for his work in \#grml. osd\_server.py allows you to be notified about remote stuff via On Screen Display when running X. Expect to find a hint for setup in grml\-tips(1\) soon.
Another feature waiting for being published: grml\-policy\-rc.d, to avoid automatical startup of init scripts via invoke\-rc.d. More details will be available in its manpage as soon as we consider it working and stable.
And I'm still working on the patchset for 2\.6\.17\-grml. I'm waiting for the next stable release (should be available on 19th of july) before providing a final build of 2\.6\.17\-grml.
We will have a grml\-develmeeting today (tuesday) where we will talk about grml 0\.8\. We have some release\-stoppers left and try to reduce todo\-list within the next few days so we can release grml 0\.8 at beginning of august. Stay tuned...
