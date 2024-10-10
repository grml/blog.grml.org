---
author: Christian Hofstaedtler
categories:
- general
date: Tue, 20 Dec 2011 13:00:00 +0000
layout: post
slug: 364-Remastering-Grml-2011.12-will-be-as-easy-as-never-before
title: Remastering Grml 2011.12 will be as easy as never before

---
For the final release of Grml 2011\.12 we will no longer ship the so called "release\-chroots" \- and this will not make it harder for you to remaster, but only easier!  
  
[grml\-live](https://grml.org/grml-live/), the build tool for Grml, has gained a new feature: it can now **extract ISOs** and use their contents as the base for your remastering needs. This feature will be released with the next grml\-live release, but it's available today in [grml\-live git](https://github.com/grml/grml-live).  
  
**How you'd use this:**  
  
* Download grml64\_2011\.12\.iso
* Install the new grml\-live (git rev. 11baa336b55 and newer)
* Edit config in /etc/grml/fai/\*
* Build:  
sudo grml\-live \-A \-V \-u \-e \~/Downloads/grml64\_2011\.12\.iso \-s testing \\  
\-c DEBORPHAN,GRMLBASE,GRML\_FULL,RELEASE,AMD64,IGNORE \\  
 \-r "Remastered" \-g grml64 \-o /tmp/grml64
* Enjoy your new ISO in /tmp/grml64/grml\_isos/
