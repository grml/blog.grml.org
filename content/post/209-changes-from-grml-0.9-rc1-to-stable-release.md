---
author: Michael Prokop
categories:
- general
date: Tue, 05 Dec 2006 17:08:00 +0000
layout: post
slug: 209-changes-from-grml-0.9-rc1-to-stable-release
title: changes from grml 0.9-rc1 to stable release

---
The final release is on its way, should be available on 6th of december. JFTR:

```
Changes from grml 0.9-rc1 to stable release:
* Update packages to Debian pool by 4th of december 2006
* sw-raid: do not automatically assemble md arrays anymore,
  instead create /etc/mdadm/mdadm.conf by default (disable via
  bootoption noswraid) and boot using swraid to enable automatic
  assembling of swraid/md arrays or run 'Start mdadm-raid' then
* added iscsitarget-2.6.18-grml
* removed thc-ipv6, ipmasqadm, tex-refs, open-iscsi, pnpbios-tools
  thc-pptp-bruter, ndiswrapper-utils-1.8, giflib-bin, giflib3g
* renamed script fma into qma (quick manual access) and provide
  less-like vim (thanks to wuehlmaus)
* zsh: new default umask setting is 002
* grml-terminalserver: some small fixes (including the
  /etc/resolv.conf issue, thanks to Wolfgang Karall)
* fixed problem when booting via firewire (thanks for noticing,
  Hendrik Scholz!)
```
