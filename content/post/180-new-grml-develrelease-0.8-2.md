---
author: Michael Prokop
categories:
- general
date: Sun, 24 Sep 2006 18:11:00 +0000
layout: post
slug: 180-new-grml-develrelease-0.8-2
title: 'new grml-develrelease: 0.8-2'

---
Hurray, we have a new develrelease! grml 0\.8\-2 is available for beta\-testers and grml\-developers.
[![grml 0.8-2](/images/gkrellShoot_09-24-06_200208.serendipityThumb.png)](/images/gkrellShoot_09-24-06_200208.png)Quoting the main changelog:

```
  * Features brand new kernel 2.6.18-grml
    Notice: the fglrx and nvidia modules are available at
    http://dufo.tugraz.at/~prokop/grml-kernel/2.6.18-grml/
    Notice2: not all modules are available yet; the missing ones are:
    reiser4 (not yet in kernel), acx100, adp94xx, bcm5700, dazuko,
    drbd8, lufs, nozomi, spca5xx, qc-usb, sl-modem, thinkpad,
    truecrypt
  * grml2hd checks whether you're installing to something like
    /dev/hdb3 and if /dev/[sh]da are harddisks, the lilo-dialog
    provides the possibility to install lilo into MBR of /dev/[sh]da
    instead of /dev/hdb3 or /dev/hdb. (Thanks for idea and code-base
    goes to Alexander Bernauer!)
  * Unicode support!
    {{< relref "178-basic-unicode-support-for-grml" >}}
    What does this mean? You can use something like 'grml
    lang=at-utf8' to set environment variable for unicode.
    Just use "lang=$YOURLANGUAGE-utf8" to use this feature.
    The script grml-setlang allows to configure environment
    variables through /etc/default/locale. (Some more documentation
    will be available as soon as I upload the packages to the
    grml-repos.)
  * Split grml-etc into grml-etc-core: this provides the possibility
    to use grml-etc-core (which ships only some core config files
    for zsh, vim,...) on *plain* Debian (stable/testing/unstable)
    systems without interference.
  * Support truecrypt in our reboot/shutdown scripts (make sure no
    mapped volumes are left behind).
  * Check whether a swap partition is in use already and display
    info message during boot process (instead of an error message).
  * When running pump finished (which happens in background during
    bootup) it writes "finished_running_pump" into
    /etc/network/status/$DEVICE so you/we can check for it.
  * Bugfixes, improvements in rebuildfstab and other grml-packages...
  * Fixed the "Booting from external devices (SCSI/USB/Firewire)
    does not work" issue.
```
Get it as long as it's fresh and hot! :\-)
