---
author: Michael Prokop
categories:
- general
date: Mon, 15 Aug 2005 00:14:00 +0000
layout: post
slug: 92-grml-and-bootchart
title: grml and bootchart

---
[![bootchart image](/images/bootchart.serendipityThumb.png "bootchart image")](/images/bootchart.png "view image as fullscreen")

I just booted grml via a new bootparam called 'bootchart' inspired by [an article on debian\-administration.org](http://www.debian-administration.org/articles/211).

To generate the picture you will have to save /var/log/bootchart.tgz and copy it to the same location on a system where bootchart\-view is available. As you can see in the picture it takes 54 seconds to boot the grml(\-large).iso via CD\-ROM using default options on my laptop.  
