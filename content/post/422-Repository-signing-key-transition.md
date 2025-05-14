---
author: Chris Hofstaedtler
categories: []
date: Wed, 14 May 2025 12:30:43 +0200
layout: post
slug: 422-Repository-signing-key-transition
title: New signing key for deb.grml.org repositories

---
Starting today, our [package respositories on https://deb.grml.org/](https://grml.org/files/) are signed with a new key.

With input and feedback from the community, especially from anarcat and Guillem Jover, we have chosen ECC keys, specifically ed25519.

There are known compatibility issues with EOL Debian versions, like buster.
If you are using such an old version, please either upgrade, or remove the Grml repositories from your setup.

## How to get the new key?

The `grml-keyring` package provided in the repositories contains the new key since March 2025.
If you updated the package on your system since then, you are all set.
Alternatively you can also get the `grml-keyring` package [from Debian testing](https://packages.debian.org/trixie/grml-keyring).

The new key's details are:
```
sec   ed25519 2025-02-24 [C]
      40CC7451383EE22A512C95D6C86CE754CF55033A
uid           [ unknown] Grml Archive Automatic Signing Key (https://grml.org/) <team@grml.org>
ssb   ed25519 2025-02-24 [S]
ssb   cv25519 2025-02-24 [E]
```

More discussion and details can be found in [grml-keyring issue #4](https://github.com/grml/grml-keyring/issues/4).
