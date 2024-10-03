---
author: Michael Prokop
categories:
- general
date: Thu, 28 Feb 2013 12:11:00 +0000
layout: post
slug: 380-Warning-broken-grml96-full_2013.02.iso-download
title: 'Warning: broken grml96-full_2013.02.iso download'

---
There was a "broken" grml96\-full ISO on our mirrors for a few hours. All our checksum files as well as the signature files are OK, just the file grml96\-full\_2013\.02\.iso has a few different bits, resulting in a file which doesn't correspond to the expected checksum. Note: the broken ISO doesn't do *any harm* (it even boots) but you should still grab the correct one.

We've updated the grml96\-full\_2013\.02\.iso file but it might take a few hours until it's propagated to all our mirrors. To check whether you're affected execute 'md5sum \-c grml96\-full\_2013\.02\.iso.md5' or 'sha1sum \-c grml96\-full\_2013\.02\.iso.sha1'.

The **broken** file is:

```
% md5sum grml96-full_2013.02.iso
b2ae41161908751c4ba6ac4db0855a70  grml96-full_2013.02.iso
% sha1sum grml96-full_2013.02.iso
f61a87223ca02482f7f7e8d674c444c40ca91b3a  grml96-full_2013.02.iso
```
The **known\-to\-be\-good** file should return:

```
% md5sum grml96-full_2013.02.iso
ceaec04b29f9263e384a54cda8c3bab0  grml96-full_2013.02.iso
% sha1sum grml96-full_2013.02.iso
c95df860f1c08cd7e82ddeac4918bb29cb3f0b7d  grml96-full_2013.02.iso
```
Sorry for the annoyance. Thanks to zeldor for bringing this issue to our attention.
