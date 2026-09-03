---
author: Chris Hofstaedtler
categories: []
date: Thu, 03 Sep 2026 16:00:00 +0200
layout: post
slug: 426-Grml-new-stable-release-2026.09-available
title: Grml - new stable release 2026.09 available

---
We are proud to announce our new stable release 🚢 version 2026.09, code-named ['Hättiwaritätti'](https://grml.org/faq/#releasename)!

Grml is a bootable live system (Live CD) based on Debian. Grml 2026.09 brings you fresh software packages from Debian testing/forky and enhanced hardware support. Known bugs from previous releases are fixed.

GNU screen 5.0.1 is shipped with adapted Grml configuration.

Like in the previous release 2026.04, Live ISOs 📀 are available for 64-bit x86 (`amd64`) and 64-bit ARM CPUs (`arm64`).

For a detailed overview of the changes from Grml 2026.04 to 2026.09, please check out [the official release announcement](https://grml.org/changelogs/README-grml-2026.09/).

Don't forget to use a current grml2usb (0.20.14 or newer) with this new release.

### ❤️ Thanks ❤️

Once again [netcup](https://www.netcup.com/) contributed financially, this time specifically to this release. Thank you, [netcup](https://www.netcup.com/) ❤️

We also want to thank our [individual sponsors](https://github.com/sponsors/grml) donating through GitHub.
If you like what we are doing, please join in!

Thanks to everyone who contributed to Grml and this release, stay healthy and happy Grml-ing! ❤️🧡💛💚💙💜

### grml-live changes

Our build and customization tool `grml-live` underwent a lot of changes, prompted by `systemd` not working inside `/proc`-less chroots anymore.

`grml-live` now uses Linux user namespaces.
Unfortunately these are often unavailable inside containers (think Docker, podman).

To unblock the release of Grml 2026.09, we have implemented the workflows we need for releasing.
Support for chroot-based workflows is forthcoming; feedback on how these workflows are used exactly is welcome.

In the meantime please take a look at the [grml-live changes in git](https://github.com/grml/grml-live/compare/v0.56.0...master).

As previously announced, `grml-live` is no longer part of the `GRML_FULL` ISO flavour.

### Get your copy

Now head over to our [download page](https://grml.org/download/) and grab your own copy.
