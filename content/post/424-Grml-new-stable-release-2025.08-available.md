---
author: Chris Hofstaedtler
categories: []
date: Sat, 16 Aug 2025 16:00:00 +0200
layout: post
slug: 424-Grml-new-stable-release-2025.08-available
title: Grml - new stable release 2025.08 available

---
We are proud to announce our new stable release 🚢 version 2025.08, code-named ['Oneinonein'](https://grml.org/faq/#releasename)!

Grml is a bootable live system (Live CD) based on Debian. Grml 2025.08 is based on the newly released Debian 13 `trixie` and addresses known bugs from previous releases.

Like in the previous release 2025.05, Live ISOs 📀 are available for 64-bit x86 (`amd64`) and 64-bit ARM CPUs (`arm64`).

### ❤️ Thanks ❤️

Without [Debian](https://www.debian.org/) this project would not exist, and we would like to celebrate with Debian their [32nd birthday](https://bits.debian.org/2025/08/debian-turns-32.html)!

Once again [netcup](https://www.netcup.com/) contributed financially, this time specifically to this release. Thank you, [netcup](https://www.netcup.com/) ❤️

We also want to thank our [individual sponsors](https://github.com/sponsors/grml) donating through GitHub.
If you like what we are doing, please join in!

Thanks to everyone who contributed to Grml and this release, stay healthy and happy Grml-ing! ❤️🧡💛💚💙💜

### grml-live changes

While the Live ISO release was focused on Debian 13, in our build-tool [grml-live](https://github.com/grml/grml-live/) more housekeeping and tidying up happened.
If you remaster Grml ISOs or build your own, please take a look at the grml-live changelog.
We want to highlight the merging of previously separate packages grml-autoconfig, grml-etc, grml-scripts and grml-udev-config into the grml-live config space.

For a detailed overview of the changes from Grml 2025.05 to 2025.08, please check out [the official release announcement](https://grml.org/changelogs/README-grml-2025.08/).

### keyring changes

Users of our [deb.grml.org repository](https://grml.org/files/#grmlrepos) need to have updated their grml-keyring package to have the current signing key. With the 2025.08 release we have stopped signing the repository with the old key.

If you want just the Grml console configuration, check out the [install instructions](https://grml.org/console/) without using the deb.grml.org repository.

### Get your copy

Now head over to our [download page](https://grml.org/download/) and grab your own copy.


🪩 Please join us in celebrating [20 Years of Grml Releases]({{< ref "417-20-years-grml-releases" >}}) and send us a 🌆 postcard!
