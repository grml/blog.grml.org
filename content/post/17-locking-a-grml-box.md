---
author: Michael Prokop
categories:
- general
date: Wed, 02 Mar 2005 16:37:00 +0000
layout: post
slug: 17-locking-a-grml-box
title: locking a grml box

---
I was thinking of a reliable way to lock a grml box. Logging out is not possible due to the respawn\-feature of init.

The solution is to run `passwd && vlock -a`.

This sets a password for the current user (which is disabled by default for security reasons) and then locks the current console and disables switching to other consoles.
