---
author: Michael Prokop
categories:
- packages
date: Fri, 17 Jun 2005 15:39:00 +0000
layout: post
slug: 74-grml-autoconfig-revisited
title: grml-autoconfig revisited

---
I just worked on grml\-autoconfig which is a seperate package since 5th of June. I split grml\-autoconfig into a shellscript\-library, an init\-file and a configuration file. Now it's possible to de\-/activate the modules of grml\-autoconfig without touching the source itself. As an example:

```
% cat /etc/grml/autoconfig.config
[...]
CONFIG_DISCOVER=no
CONFIG_HWINFO=yes
CONFIG_HOTPLUG_AGENT=yes
CONFIG_HOTPLUG_BLACKLIST=yes
CONFIG_HOTPLUG=yes
```

I'll add the functionality to grml2hd so you will be able to decide on your own what parts you would like to use on a harddisk installation of grml.
I'll do some more testing and will upload the new grml\-autoconfig\-system to the pool then.
