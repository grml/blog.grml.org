---
author: Michael Prokop
categories:
- packages
date: Fri, 03 Nov 2006 17:54:00 +0000
layout: post
slug: 194-grml-debootstrap-wrapper-around-debootstrap-for-installing-plain-Debian-via-grml
title: 'grml-debootstrap: wrapper around debootstrap for installing plain Debian via
  grml'

---
[![grml-debootstrap screenshot](/images/gkrellShoot_11-03-06_184224.png)](/images/gkrellShoot_11-03-06_184224.png)I assume you already know [debootstrap](http://packages.debian.org/unstable/admin/debootstrap). Quoting the package description "debootstrap is used to create a Debian base system from scratch, without requiring the availability of dpkg or apt. It does this by downloading .deb files from a mirror site, and carefully unpacking them into a directory which can eventually be chrooted into." I already described the procedure for [installing Debian sarge and etch via grml in my private blog](http://michael-prokop.at/blog/2006/08/11/install-debian-etch-via-grml/).
I usually install plain Debian systems via debootstrap, because it's simple, fast and just works. Especially because grml provides recent hardware detection I can often install Debian on systems where the official debian installer might not work at all. But running debootstrap is a boring task, especially if you often do this kind of installation the tasks during installation are boring. Therefore I decided to write a wrapper around debootstrap, and there we are:

```
% apt-cache show grml-debootstrap
 Description: wrapper around debootstrap for installing plain Debian via grml
  This package provides a wrapper suite around deboostrap and
  cdebootstrap for installing a plain Debian system via grml.
  .
  All you have to do is adjust a few variables in configuration
  file /etc/debootstrap/config and invoke grml-debootstrap then.
  A plain and base Debian system will be installed on the given
  device then. Customization of this process is possible as well.
```
Installation of a plain and base Debian etch system is pretty fast and easy this way. The first public version of grml\-debootstrap is available in [the grml repository](https://grml.org/repos/). Just apt\-get it when running the [grml live\-cd](https://grml.org/). As usual: [feedback is welcome](https://grml.org/contact/).
