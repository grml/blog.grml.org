---
author: Michael Prokop
categories:
- packages
date: Sat, 26 Feb 2005 22:02:00 +0000
layout: post
slug: 10-create-a-perl-debian-package
title: create a perl debian package

---
I wanted to add ACME::Bleach, ACME::EyeDrops and ACME::Smirch to grml. So I had to create my first perl debian packages.

It couldn't be easier:

    % dh-make-perl --cpan Acme::Smirch --build
