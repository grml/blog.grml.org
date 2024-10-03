---
author: Ulrich Dangel
categories:
- general
date: Fri, 23 Dec 2011 13:00:00 +0000
layout: post
slug: 367-Create-a-Grml-ISO-image-with-your-own-ssh-keys-for-password-less-login
title: Create a Grml ISO image with your own ssh keys for password less login

---
In this article we will show you how you can leverage [grml\-autoconfig](http://grml.org/config/grml-autoconfig.1.html) to create a Grml ISO which will automatically start an ssh server and use your own ssh keys instead of the traditional password based login. This allows Grml to be used not only for interactive rescue operations but also for remote or automated setups.

Starting with Grml 2009\.05 we streamlined the support of hooking into our boot\-process in [grml\-autoconfig](http://grml.org/config/grml-autoconfig.1.html) thanks to the patches from Marc 'Zugschlus' Haber. Now it is possible to execute arbitrary scripts, unpack archives or install packages at startup not only directly from the Live CD but also from partitions. This allows you to create customized Grml Images with ease without the need to modify the squashfs image (usually known as remastering). In this example we will add the necessary files directly onto the ISO image but you can also use a USB stick instead. Please make sure you read the [grml\-autoconfig manpage](http://grml.org/config/grml-autoconfig.1.html) 

The first step is to create a directory which will contain all the additional files to be copied onto the ISO image. In this example we use */tmp/grml\_overlay/*
> ```
> mkdir /tmp/grml_overlay
> ```


The next step is to create an archive containing the ssh keys. For this step you need either [fakeroot](http://man.cx/fakeroot(1)) or run the commands as root.

> ```
> 
> TMPDIR="/tmp/grml_config"
> cd "$TMPDIR" || mkdir "$TMPDIR" && cd "$TMPDIR"
> fakeroot 
> mkdir --parent root/.ssh home/grml/.ssh
> chmod 0700 root/.ssh home/grml/.ssh
> cp /home/uli/.ssh/id_rsa.pub  root/.ssh/authorized_keys
> cp /home/uli/.ssh/id_rsa.pub  home/grml/.ssh/authorized_keys
> chown -R 1000:1000 home/grml
> tar --numeric-owner -j -c -f /tmp/grml_overlay/config.tbz .
> 
> ```

This will create an archive named /tmp/grml\_overlay/config.tbz containing all the files we created in our directory. Please make sure to replace the cp command with your own ssh keys. As we used fakeroot in this example you can manipulate file permissions without the need to run these commands as root. 

Now we have everything what's needed prepared and can just run [grml2iso](http://grml.org/grml2usb/) and specify the additional boot parameters as well as the overlay directory.
> ```
> 
> grml2iso -b "config ssh" -c /tmp/grml_overlay -o my-grml.iso ./grml64_2011.12.iso
> 
> ```

[![](/images/sshkeys_unpack.png "unpack ssh keys")](/images/sshkeys_unpack.png "unpack ssh keys")
This will create a modified Grml ISO named my\_grml.iso and add the bootparameters *config ssh* to all the existing boot\-entries and copy all files from the /tmp/grml\_overlay directory onto your modified ISO image. With the *config* parameter grml\-autoconfig will automatically unpack config.tbz at bootup which contains our ssh keys. The ssh parameter will automatically start the ssh server and set a random password for the grml user. But as we deployed our ssh keys we don't care about the password anyway. For a list of all boot parameters have a look at the [Grml cheatcodes](http://git.grml.org/?p=grml-live.git;a=blob_plain;f=templates/GRML/grml-cheatcodes.txt;hb=HEAD).  

During startup of Grml you will notice some additional log messages indicating the unpacking of your created archive. This shows that everything works like intended.


Combining different boot parameters in Grml like *config* and *ssh* allows you to create customized and tailored distributions for your own needs without having to dig into the remastering process. With the availability of tools like grml2usb and grml2iso you can easily create customized tools based on Grml without the need to develop everything from scratch. We showed how you can leverage *grml2iso* to create a Rescue CD based on Grml with ssh keys for remote login.
