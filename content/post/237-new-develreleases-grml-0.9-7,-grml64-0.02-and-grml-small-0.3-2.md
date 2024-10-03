---
author: Michael Prokop
categories:
- general
date: Sun, 15 Apr 2007 15:58:00 +0000
layout: post
slug: 237-new-develreleases-grml-0.9-7,-grml64-0.02-and-grml-small-0.3-2
title: 'new develreleases: grml 0.9-7, grml64 0.02 and grml-small 0.3-2'

---
I was working very hard the last few days, the result is a bunch of new develreleases. The stable releases are coming closer now, I've just to write the release notes and find artwork for the new releases (want to contribute? let me know!) first. Quoting the main changelog for the new develreleases:

```
=======================================================================
Main changelog for grml:
  * updated kernel 2.6.20-grml based on 2.6.20.6
  * updated libc6 (2.5)
  * updated Debian packages by 2007-04-15
  * several fixes, including the ones mentioned on
    http://wiki.grml.org/doku.php?id=grml_devel
  * LaTeX: switch from tetex to texlive
  * grml-debootstrap is aware of stages (canceling is possible now),
    supports lenny (additionally to Etch of course) now as well
  * grml-x: use of evdev, please test it with all your mouses and
    report whether it works or not!
  * tons of other nifty updates/addons/... I've to dig through the
    changelogs first.... :)
Removed packages since grml 0.9:
  aircrack classpath classpath-common classpath-gtkpeer cpp-3.3 ddd
  debsig-verify doc-base emacspeak ethereal ethereal-common gcc-2.95
  gcc-3.3 gcc-3.3-base glibc-doc grml-btnet grml-kerneladdons-2.6.18
  grml-sysvinit gs-gpl jamvm java-common kdoc latex-ucs
  libavahi-core4 libbind9-0 libclamav1 libcman1 libdlm1 libdns21
  libexiv2-0.10 libgcj-common libgtk-perl libgulm1 libinklevel3
  libisc11 libisccc0 libisccfg1 liblwres9 libncurses5-dev
  libnet-pcap-perl libnet-perl libnids1.20 libpam-opie libqdbm14
  libreadline5-dev librudiments0.29 libsasl2 libsqlrelay-0.37
  libstdc++2.10-glibc2.2 libstdc++5 libtorrent9 libuclibc0
  libxmltok1 linux-wlan-ng linux-wlan-ng-firmware lout lout-common
  lufs-utils lvm-common lvm10 madwifi-doc misdn-utils mutt-ng
  muttprint nxclient olsrd-plugin openafs-client openafs-krb5
  opie-server postgresql-client-8.1 prosper python-clamav
  python-jaxml python2.3 samdump scapy simh tclx8.3 tesseract-ocr
  tetex-base tetex-bin tetex-extra tethereal tftp-hpa tftpd-hpa
  tk-brief unionfs-utils unzsplit valgrind wellenreiter wmi
  xen-tools xen-utils-common xlibmesa-gl zsplit
Added packages since grml 0.9:
  advchk array-info ascii2binary atftpd blktrace bluetooth-alsa cbm
  clive concalc cryopid dnsproxy dvb-utils fatresize funionfs
  gaffitter gatling gems genisoimage grml-desktop
  grml-kerneladdons-2.6.20 grml-pylib icedax ii imsniff keyutils
  kqemu-common kvm mcabber mtp-tools ncc newsbeuter odt2txt
  olsrd-plugins oss-compat pdfcube perl-tk pnputils podget
  postgresql-client-8.2 python-scapy python-urwid recordmydesktop
  samdump2 scalpel sigit smbnetfs speedometer texlive-base
  texlive-base-bin texlive-common texlive-doc-base
  texlive-fonts-recommended texlive-lang-german texlive-latex-base
  texlive-latex-recommended treil tss uncrustify urlscan vde2
  vinetto xserver-xorg-input-aiptek xserver-xorg-input-elo2300
  xserver-xorg-input-elographics xserver-xorg-input-evtouch
  xserver-xorg-input-hyperpen xserver-xorg-input-joystick
  xserver-xorg-input-penmount xserver-xorg-input-void xwatchwin zzuf
=======================================================================
=======================================================================
Main changelog for grml64:
  * Tons of updates, fixes,.. updated Debian packages by 2007-04-15
  * Added several 32bit compability libs, so now working 64<->32bit
    should work really fine.
  * Removed LaTeX, due to space reasons.
=======================================================================
=======================================================================
Main changelog for grml-small:
  * updated to kernel 2.6.20-grml-small (based on 2.6.20.7)
  * updated libc6 (2.5)
  * tons of fixes.... including the issues ones mentioned on
    http://wiki.grml.org/doku.php?id=grml_devel
  * updated Debian packages by 2007-04-15
  * merged all relevant code from big grml[tm]
=======================================================================

```
