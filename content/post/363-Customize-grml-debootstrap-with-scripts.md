---
author: Ulrich Dangel
categories:
- general
date: Mon, 19 Dec 2011 12:00:00 +0000
layout: post
slug: 363-Customize-grml-debootstrap-with-scripts
title: Customize grml-debootstrap with scripts

---
In our latest [blog entry about grml\-debootstrap]({{< relref "362-Deploy-Virtual-Machines-with-Grml-2011.12-or-Debian" >}}) we described how to leverage `grml-debootstrap` for automated installations of Debian into virtualized systems. Unfortunately sometimes this is not enough and you need to run commands after the installation. This post will describe some customization methods of `grml-debootstrap`. For more information on this topic also look at [the manpage of grml\-debootstrap](https://grml.org/grml-debootstrap/)

One quite common task is to execute scripts after the installation like for example gathering the ssh host key or adding your own CA to the host. `grml-debootstrap` supports the execution of scripts after the machine is successfully installed.

To execute scripts after the installation we first need a directory containing all the scripts. This directory will be afterwards specified as a parameter to `grml-debootstrap`. In this example we are using `./scripts` as the directory name.

```
mkdir ./scripts
```

After we create the directory we also need to create a script for our post\-processing task. For this example we'll create a script which will examine the fingerprints of the ssh hosts keys. To be able to access and modify the image all the scripts executed by `grml-debootstrap` will have an environment variable specified called `MNTPOINT` which will point to the directory used for installing the system. Then we have to create a script inside the directory and make it executable:

```
$ cat >./scripts/89_print_sshkeys <<EOF
#!/bin/bash
set -e
if [ -z "$MNTPOINT" ] ; then
  echo "Please run $0 inside grml-debootstrap or export MNTPOINT" >&2
  exit 1
fi

for key in "$MNTPOINT"/etc/ssh/ssh_host_*_key.pub ; do
  chroot "$MNTPOINT" ssh-keygen -l -f ${key##$MNTPOINT}
done
EOF
$ chmod +x ./scripts/89_print_sshkeys
```

This script will iterate over all ssh host keys and print the fingerprint of them.

After we created the directory and the script we can now point `grml-debootstrap` to the directory and it will run all executable files in it. If we extend the command\-line from our last example we have to specify the `--scripts` parameter and point it to the created directory:

```
$ sudo grml-debootstrap --scripts ./scripts/ --password root-pw --vmsize 3G --vmfile --target ./qemu.img
....
Finished chroot installation, exiting.
 * Executing script ./scripts/89_print_sshkeys
1024 9e:d9:18:1d:47:ae:26:9f:53:5e:63:3c:bd:37:ea:2b /etc/ssh/ssh_host_dsa_key.pub (DSA)
2048 c1:5e:27:a3:2f:7d:30:a0:ab:75:a2:86:e7:bb:8a:e2 /etc/ssh/ssh_host_rsa_key.pub (RSA)
....
```


This shows how easy it is to customize and extend `grml-debootstrap` to your own needs. You can easily create customized scripts and run arbitrary commands on the target to do whatever you want. `grml-debootstrap` is of course available within [Grml](https://grml.org/) but also in [Debian](http://debian.org/).
