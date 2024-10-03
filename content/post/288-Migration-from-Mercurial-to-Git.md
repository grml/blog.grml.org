---
author: Michael Prokop
categories:
- general
date: Wed, 01 Oct 2008 22:00:00 +0000
layout: post
slug: 288-Migration-from-Mercurial-to-Git
title: Migration from Mercurial to Git

---
Over the last few weeks the grml team evaluated the distributed version controll system**Git**. Git is an open source, distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Read the [wikipedia article on Git](http://en.wikipedia.org/wiki/Git_(software)) to get an (not so short) overview.
Grml used to work with the distributed version controll system **Mercurial** and officially announced its use on October 18th, 2006\. The way Mercurial worked was great for us and at that time it definitely was the best solution for our needs. We provided detailed documentation for our setup (see [grml.org/mercurial/](http://grml.org/mercurial/)) and developed our own utils for working with Mercurial and Debian packaging ([grml\-mercurial\-utils](http://hg.grml.org/grml-mercurial-utils)). Special thanks to the Mercurial developers \- we highly appreciate all your help!
But we had to re\-evaluate the situation as time passed:
* in Debian Mercurial is not used for many packages ([http://hg.debian.org](http://hg.debian.org/)), while Git is used a lot ([git.debian.org](http://git.debian.org/)) and there's visible progress on the Git front (for example [git\-buildpackage](http://packages.debian.org/sid/git-buildpackage), [topgit](http://repo.or.cz/w/topgit.git) and [vcs\-pkg.org](http://vcs-pkg.org/))
* situation of Git improved (like better documentation, tools for Debian packaging,...)
* Git provides better branching, rebasing which is great especially when you want to put essential software under your own control without having to fork it from upstream
* Git provides a low\-level interface and all the important features as part of the Git suite. Mercurial provides some important features just as extension (which might not work on upgrades or don't play together with other extensions).
* more and more software we have to deal with is available in Git repositories
So whereas Mercurial used to work just fine for us in most cases Git provides the better approach for us nowadays.
**Current state**
Thanks to our [hg\-to\-git tools](http://git.grml.org/?p=hg-to-git.git;a=summary) the migration itself took less than 1 hour and all repositories have been migrated from [hg.grml.org](http://hg.grml.org/) to [git.grml.org](http://git.grml.org/).
By today (1st of october 2008\) the grml mercurial repositories are deprecated and the official place for grml's sources is **[git.grml.org](http://git.grml.org/)**. The mercurial hosting will be deactivated within the next few weeks.
All the documentation and scripts of grml are being updated to reflect the changes and updated URLs but it has not been finished yet. So if you find something still mentioning hg.grml.org instead of git.grml.org please [let us know](http://grml.org/contact/), thanks!
As usual we provide documentation about our setup and tools:**[grml.org/git/](http://grml.org/git/)**
We highly appreciate any help, corrections and further feedback.
Special thanks to [Michael Gebetsroither](http://grml.org/team/#gebi) for his work and help on migrating.
