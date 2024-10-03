---
author: Michael Prokop
categories:
- general
date: Fri, 01 Apr 2005 11:38:42 +0000
layout: post
slug: 35-grml-running-with-vesafb-tng
title: grml running with vesafb-tng

---
I patched the grml\-kernel (2\.6\.11\-grml) with [vesafb\-tng](http://dev.gentoo.org/~spock/projects/vesafb-tng/index.php):

```
grml@grml ~ % fbset -i  
  
mode "1024x768-60"  
    # D: 65.003 MHz, H: 48.365 kHz, V: 60.006 Hz  
    geometry 1024 768 1024 1536 16  
    timings 15384 160 24 29 3 136 6  
    rgba 5/11,6/5,5/0,0/0  
endmode  
  
Frame buffer device information:  
    Name        : VESA VGA  
    Address     : 0xe9000000  
    Size        : 3145728  
    Type        : PACKED PIXELS  
    Visual      : TRUECOLOR  
    XPanStep    : 0  
    YPanStep    : 1  
    YWrapStep   : 0  
    LineLength  : 2048  
    Accelerator : No  
grml@grml ~ %
```
I'll do some more testing, if everything works fine the next devel\-release will include the vesafb\-tng\-stuff.
