---
author: Michael Prokop
categories:
- general
date: Wed, 12 Aug 2009 13:41:00 +0000
layout: post
slug: 318-forensic-mode-readonly-blockdevices-on-hotplug
title: 'forensic mode: readonly blockdevices on hotplug'

---
[grml release 2009\.05](http://grml.org/changelogs/README-grml-2009.05/) supports a bootoption 'readonly' which marks all /dev/\[hs]\*dX devices as readonly. This is important for data rescue and forensic investigations and is automatically activated when booting via 'forensic'. I just implemented readonly support for hotplugging. This means you can safely add new block devices to your system when booted via forensic and the blockdevices will be set to readonly mode automatically. You'll notice something like that in your syslog:
> Aug 12 16:21:49 grml kernel: \[ 259\.426656] usb 2\-3: new high speed USB device using ehci\_hcd and address 4  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551346] usb 2\-3: configuration \#1 chosen from 1 choice  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551582] scsi8 : SCSI emulation for USB Mass Storage devices  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551701] usb\-storage: device found at 4  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551704] usb\-storage: waiting for device to settle before scanning  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551816] usb 2\-3: New USB device found, idVendor\=1e3d, idProduct\=2092  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551819] usb 2\-3: New USB device strings: Mfr\=1, Product\=2, SerialNumber\=3  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551821] usb 2\-3: Product: Flash Disk  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551823] usb 2\-3: Manufacturer: CBM  
> 
> Aug 12 16:21:49 grml kernel: \[ 259\.551824] usb 2\-3: SerialNumber: 301958004BD98A00  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.550509] scsi 8:0:0:0: Direct\-Access CBM Flash Disk 5\.00 PQ: 0 ANSI: 2  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.551366] sd 8:0:0:0: \[sdc] 2041856 512\-byte hardware sectors: (1\.04 GB/997 MiB)  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.551860] sd 8:0:0:0: \[sdc] Write Protect is off  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.551864] sd 8:0:0:0: \[sdc] Mode Sense: 0b 00 00 08  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.551866] sd 8:0:0:0: \[sdc] Assuming drive cache: write through  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.552982] sd 8:0:0:0: \[sdc] 2041856 512\-byte hardware sectors: (1\.04 GB/997 MiB)  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.553480] sd 8:0:0:0: \[sdc] Write Protect is off  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.553482] sd 8:0:0:0: \[sdc] Mode Sense: 0b 00 00 08  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.553484] sd 8:0:0:0: \[sdc] Assuming drive cache: write through  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.553487] sdc: sdc1  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.554282] sd 8:0:0:0: \[sdc] Attached SCSI removable disk  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.554346] sd 8:0:0:0: Attached scsi generic sg3 type 0  
> 
> Aug 12 16:21:54 grml kernel: \[ 264\.554528] usb\-storage: device scan complete  
> **Aug 12 16:21:54 grml logger: forensic mode: setting /dev/sdc \[CBM\_Flash\_Disk\_301958004BD98A00\-0:0] to readonly  
> 
> Aug 12 16:21:54 grml logger: \|\-\> done; execute 'blockdev \-\-setrw /dev/sdc' to unlock**Aug 12 16:21:54 grml rebuildfstab\[13521]: re\-generating /etc/fstab \- see 'man rebuildfstab'  
> 
> Aug 12 16:21:54 grml rebuildfstab\[13522]: bootoption nofstab found, ignoring request to re\-generate /etc/fstab without force option  
> **Aug 12 16:21:55 grml logger: forensic mode: setting /dev/sdc1 \[CBM\_Flash\_Disk\_301958004BD98A00\-0:0] to readonly  
> 
> Aug 12 16:21:55 grml logger: \|\-\> done; execute 'blockdev \-\-setrw /dev/sdc1' to unlock**Aug 12 16:21:55 grml rebuildfstab\[13551]: re\-generating /etc/fstab \- see 'man rebuildfstab'  
> 
> Aug 12 16:21:55 grml rebuildfstab\[13552]: bootoption nofstab found, ignoring request to re\-generate /etc/fstab without force option
