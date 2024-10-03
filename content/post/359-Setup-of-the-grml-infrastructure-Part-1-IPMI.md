---
author: Andreas Gredler
categories: []
date: Wed, 21 Dec 2011 16:41:00 +0000
layout: post
slug: 359-Setup-of-the-grml-infrastructure-Part-1-IPMI
title: 'Setup of the grml infrastructure: Part 1 - IPMI'

---
Back in August 2011 the Grml Team received a new Server \& Hosting furnished by [Hostway](http://www.hostway.de/). The Server is hosted in their [DataCenter in Hannover](http://www.hostway.de/infrastruktur/rechenzentren/index.php). As the new Server is dedicated for the Grml Infrastructure we chose to create a new system from scratch. The new infrastructure contains many pieces like puppet, libvirt, ldap and many more. In the next few weeks we will provide some insights into our current Server Setup. So expect some interesting posts about system administration.


We start off with IPMI (Intelligent Platform Management Interface). IPMI is the interface to the BMC (Baseboard management controller), which let's you read sensor data or just shutdown or reboot you server. IPMI may be used over lan or directly (in\-band) with the help of a kernel module (ipmi\_si) that implements the ipmi driver. In newer servers you may find a virtual usb to eth interface (e.g. IBM IMM in contrast to IBM RSA). First of all we need to setup a new user/admin account instead of the default one. To list all users run:  

```
ipmitool user list 1
```
The digit 1 indicates channel 1\.  
Create user jimmy:
```
ipmitool user set name 2 jimmy
ipmitool user set password 2 mysecret
```
2 is for userid 2 which was the first free id in my case.
Next we need to setup networking:
```
ipmitool lan set 1 ipaddr 192.168.2.6
ipmitool lan set 1 defgw ipaddr 192.168.2.1
ipmitool lan print 1
```
Digit 1 is again for channel 1\.  
Now you can test your ipmi setup over the network:
```
ipmitool -I lan -H 192.168.1.6 -U jimmy bmc info
```
You'll be prompted for the password and receive some infos of the bmc controller.  
Here are some more examples:
```
ipmitool -I lan -H 192.168.1.6 -U jimmy chassis power status
ipmitool -I lan -H 192.168.1.6 -U jimmy chassis power off
ipmitool sensor get "BB Ambient Temp"
ipmitool sensor get "CPU Fan"
```
The first one checks the power status of the server, e.g. on or off and the second one powers the server off. The last two read some sensor data. Read the man page of ipmitool to find out more ;\-)
There's a lot more about IPMI but this should help you to get started.