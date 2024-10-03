---
author: Michael Prokop
categories:
- general
date: Mon, 02 May 2005 13:35:00 +0000
layout: post
slug: 55-kernel-2.6.11.8-and-some-other-stuff...
title: kernel 2.6.11.8 and some other stuff...

---
grml release 0\.4 will be based upon kernel 2\.6\.11\.8\. The kernel build has been finished, documentation has been updated (see http://grml.org/kernel\-devel/ \- but not yet finished) and grml 0\.3\-7 is running with the kernel:

```
grml@grml ~ % uname -a  
Linux grml 2.6.11-grml #1 SMP Sun May 1 15:09:55 CEST 2005 i686 GNU/Linux
```

On friday Gebi presented me his grml\-terminalserver which let's you boot on computers without CD\-ROM but with PXE\-cabable NICs. It works even on computers witout PXE using a floppy\-drive. Woot! Some minor issues have to be fixed before releasing grml 0\.4 with the grml\-terminalserver, Gebi is working hard. ;\-)

I wrote and tested the script grml\-vpnc\-tugraz which let's you connect to WLAN at TU Graz via vpnc. It will be part of grml 0\.4 of course.
Now grml\-hwinfo collects information of your hardware and writes everything to a file namend info.tar.bz2\. Now we can get all information required to fix bugs reported by grml\-users quite easy.

Several useful scripts also got part of grml\-scripts, many updates in grml\-etc. Just some minor issues have to be resolved, documentation has to become up2date and then grml 0\.4 will be available!
