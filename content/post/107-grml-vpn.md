---
author: Michael Prokop
categories:
- general
date: Thu, 22 Sep 2005 15:44:00 +0000
layout: post
slug: 107-grml-vpn
title: grml-vpn

---
We just have a developer meeting in Graz and Gebi wrote a script
namend grml\-vpn. grml\-vpn is a program to establish encrypted
communication channels in a network. We just tested it and it really
rocks. :\-) It's very easy to use, take a look at the usage example:
Gebi (root@gebi) starts grml\-vpn on his laptop with key/passphrase 'test' and uses his and my ip for the encrypted communication channel:

```
root@gebi # grml-vpn -k test add 1000 192.168.1.104 192.168.1.101
```
I (root@mika) am using the same command line on my laptop:

```
root@mika # grml-vpn -k test add 1000 192.168.1.104 192.168.1.101
```

To demonstrate that it's working let's use IPsec's setkey command:

```
root@mika # setkey -D
192.168.1.101 192.168.1.104  
        esp mode=transport spi=1000(0x000003e8) reqid=0(0x00000000)  
        E: aes-cbc  d8e8fca2 dc0f896f d7cb4cb0 031ba249  
        seq=0x00000000 replay=0 flags=0x00000000 state=mature  
        created: Sep 22 15:15:02 2005   current: Sep 22 15:19:40 2005  
        diff: 278(s)    hard: 0(s)      soft: 0(s)  
        last: Sep 22 15:15:14 2005      hard: 0(s)      soft: 0(s)  
        current: 1488(bytes)    hard: 0(bytes)  soft: 0(bytes)  
        allocated: 12   hard: 0 soft: 0  
        sadb_seq=1 pid=20148 refcnt=0  
192.168.1.104 192.168.1.101  
        esp mode=transport spi=1001(0x000003e9) reqid=0(0x00000000)  
        E: aes-cbc  d8e8fca2 dc0f896f d7cb4cb0 031ba249  
        seq=0x00000000 replay=0 flags=0x00000000 state=mature  
        created: Sep 22 15:15:02 2005   current: Sep 22 15:19:40 2005  
        diff: 278(s)    hard: 0(s)      soft: 0(s)  
        last: Sep 22 15:15:14 2005      hard: 0(s)      soft: 0(s)  
        current: 768(bytes)     hard: 0(bytes)  soft: 0(bytes)  
        allocated: 12   hard: 0 soft: 0  
        sadb_seq=0 pid=20148 refcnt=0
```


Now let's check whether it's really encrypted:

```
root@mika # ping 192.168.1.104  
[...]  
root@gebi # tcpdump  
15:16:26.066885 IP 192.168.1.101 > 192.168.1.104: ESP(spi=0x000003e8, seq=0xa)  
15:16:26.067040 IP 192.168.1.104 > 192.168.1.101: ESP(spi=0x000003e9, seq=0xa)
```

Bingo! :\-)
