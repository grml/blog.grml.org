---
author: Michael Prokop
categories:
- general
date: Thu, 03 Oct 2024 14:18:00 +0000
layout: post
slug: "415-Infrastructure-overhaul-web-paste-blog"
title: "Infrastructure overhaul: web, paste + blog"

---
We're reworking, updating and migrating our infrastructure. We try to not break too much of it, but if you should notice any problems [please let us know](https://grml.org/contact/).

We no longer host our own paste service (which used to be available at paste.grml.org). This [paste.pl](https://github.com/formorer/paste.pl) service was written and thankfully maintained for a long time by alumni Grml developer Alexander 'formorer' Wirt, and served us well for many years (seems to have be >14 years!). We no longer want to maintain the service ourself though and therefore decided to retire it. If you're looking for a similar web service, paste.debian.net provides the same paste.pl service and API, and is also run by Alexander.

We also migrated our mirror infrastructure, as well as our download and [main web presence](https://grml.org/). All those changes should not really affect nor be visible to anyone in the public though.

Finally, we also migrated our blog system, which is serving what you're reading here. :) Back in 2011 we switched from the hosted supersized.org service to our self hosted [Serendipity](https://www.s9y.org/). Also serendipity (AKA s9y) served us well for the last 13 years, but we don't want to host yet another PHP/MySQL service any longer. We decided to migrate to [hugo](https://gohugo.io/), being a static blog engine.

**IMPORTANT:** The RSS feed at https://blog.grml.org/feeds/index.rss2 should work as it used to work. But comments are gone, so also the previous comments feeds (formerly known as blog.grml.org/feeds/comments.rss2) is gone as well. We had troubles with getting the Atom feed working with hugo, but decided to not put further work into that, as most users seem to be using the RSS2 feed anyways. So at least for now our Atom feed is gone! If you are subscribed to our atom feed at blog.grml.org/feeds/atom.xml, please switch to https://blog.grml.org/feeds/index.rss2 instead, to be able to receive further updates from our Grml blog. This also will be the last blog entry that's shipped via Atom feed.

