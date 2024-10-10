---
author: Michael Prokop
categories:
- general
date: Sun, 16 Aug 2009 20:22:00 +0000
layout: post
slug: 319-grml-development-new-bootsplash
title: 'grml development: new bootsplash'

---
Today I decided to implement a new bootsplash layout. Vesamenu of the isolinux project worked fine during our tests so I decided we should think about making it to grml's default. My implementation in grml\-live allows you to fall back to the old bootsplash layout via enabling one single configuration option (being: `ISOLINUX_METHOD=console`) and you can even get the old function keys layout back during runtime using the 'Further boot options...' entry. It should become part of the [daily ISOs](http://daily.grml.org/) soon. Hopefully our next development release shows that users like it and it doesn't cause any problems.

So that's what I'm talking about \- grml's new bootsplash in its current layout:

[![screenshot of new grml bootsplash](/images/new-grml-splash.serendipityThumb.png)](/images/new-grml-splash.png)