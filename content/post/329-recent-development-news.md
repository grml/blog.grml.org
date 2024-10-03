---
author: Michael Prokop
categories:
- general
date: Sat, 13 Feb 2010 01:13:00 +0000
layout: post
slug: 329-recent-development-news
title: recent development news

---
On 7th of january we've had a developer meeting on IRC, mainly for updating our roadmap towards our upcoming Grml's releases and infrastructure. That's what development of the last weeks brought up:
* **needsbuild**: we've a new service on our project infrastructure to spot packages that are available for just one architecture (out of i386 and amd64\) but missing for the other one. The service automatically builds the according package and notifies our build admins for inclusion of the package into Grml's Debian repository. Thanks for your work, formorer!
* **grml\-live** features database layer: version 0\.9\.34 introduces an additional package named grml\-live\-db. The grml\-live\-db Debian package provides a simple way to put build information of grml\-live into a database. By default you have to do nothing but install grml\-live\-db and during each invocation of grml\-live you'll get an additional entry in the sqlite3 database /var/log/grml\-live.db. If you want to customize the database logging and for further details check out the grml\-live\-db manpage. Version 0\.9\.35 with changes in FAI's config space layout to further simplify customization has been released as well.
* **grml\-quickconfig**: the simple command line tool that's visible right after booting finished Grml to get fast access to some important and often needed grml\-scripts has been redesigned. The new version is more flexible and supports proper customization. Upload of this new version as part of the new grml\-quickconfig package will happen soon. Thanks for your work, Ulrich!
* We have a new and public accessible [**Grml developer mailinglist**](http://ml.grml.org/mailman/listinfo/grml-devel).
