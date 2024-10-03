---
author: Michael Prokop
categories:
- packages
date: Mon, 16 Apr 2007 21:20:00 +0000
layout: post
slug: 238-grml-debootstrap-0.7
title: grml-debootstrap 0.7

---
I just uploaded a new version of [grml\-debootstrap](http://grml.org/grml-debootstrap/) to the grml\-testing pool providing many new features. One nifty feature is setting variables via commandline. This allows you to install Debian with just one command and 2 keystrokes(!) (one 'y' for starting execution of grml\-debootstrap and another one for setting the password of user root, this can be automated as well of course if you want to). I just installed a plain Debian system via running:

```
# grml-debootstrap --target /dev/hda2 --grub hd0 --groot hd0,1
```
But that's not all. You can install a plain Debian system full automatic(!) via bootoption debian2hd. I just did a full automatic installation with grml\-debootstrap 0\.7 and grml\-autoconfig 0\.6\.39 running on grml\-small via booting with:

```
debian2hd target=/dev/hda1 grub=hd0 groot=hd0,0 mirror=ftp://ftp.tugraz.at/mirror/debian password=foobar
```
Not a single keystroke behind the commandline on the bootprompt. Rocking! :\-)
