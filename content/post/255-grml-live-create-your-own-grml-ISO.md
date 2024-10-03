---
author: Michael Prokop
categories:
- packages
date: Sat, 15 Sep 2007 21:10:00 +0000
layout: post
slug: 255-grml-live-create-your-own-grml-ISO
title: 'grml-live: create your own grml-ISO'

---
Ever wanted to build your very own [grml](http://grml.org/)\-ISO without having to deal with all the remastering details? Want to include your very own kernel? Want to change configuration of some files? Then grml\-live might be what you ever dreamed of. :)
Check out [the grml\-live documentation](http://grml.org/grml-live/) to get an idea what I'm talking about. As you might notice grml\-live is based on [FAI](http://www.informatik.uni-koeln.de/fai/) (Fully Automatic Installation), this will provide us the possibility to deploy grml even faster, better and more customized than we already do (using [grml2hd](http://grml.org/grml2hd/), [grml\-debootstrap](http://grml.org/grml-debootstrap/) and [grml\-terminalserver](http://grml.org/terminalserver/)).
Want to get an idea how fast you can build an ISO using grml\-live? Check out:
[![Screenshot of grml-live (1)](/images/grml_live1.png)](/images/grml_live1.png)So all I did was invoking 'grml\-live'. Not even 7 minutes later I've a working grml live\-CD which is based on Debian\-stable, providing kernel 2\.6\.22\-grml and all the basic grml features:
[![Screenshot of grml-live (2)](/images/grml_live2.png)](/images/grml_live2.png)Stay tuned for an official release of grml\-live. We are working on reducing the todo list \- like porting it to other architectures, providing different flavours, some more customisation hooks and finally providing a full\-grml\-built using grml\-live.
