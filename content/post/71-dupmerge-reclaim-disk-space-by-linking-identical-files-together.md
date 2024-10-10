---
author: Michael Prokop
categories:
- packages
date: Thu, 09 Jun 2005 13:34:00 +0000
layout: post
slug: 71-dupmerge-reclaim-disk-space-by-linking-identical-files-together
title: 'dupmerge: reclaim disk space by linking identical files together'

---
I just packaged dupmerge 1\.5:

*This is a utility that scans a UNIX directory tree looking for pairs of distinct files with identical content. When it finds such files, it deletes one file to reclaim its disk space and then recreates its path name as a link to the other copy. The first version of this program circa 1993 worked by computingMD5 hashes of every file, sorting the hashes and then looking for duplicates. This worked, but it was unnecessarily slow. The comparison function I use now stops comparing two files as soon as it determines their lengths are different, which is a win when you have many large files with unique lengths.*

<http://sourceforge.net/projects/dupmerge/>

As usual you can find the package in [the grml\-repos](https://grml.org/repos/). Feedback welcome.
