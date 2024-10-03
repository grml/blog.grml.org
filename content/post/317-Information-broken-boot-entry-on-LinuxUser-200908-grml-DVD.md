---
author: Michael Prokop
categories:
- general
date: Wed, 12 Aug 2009 09:24:00 +0000
layout: post
slug: 317-Information-broken-boot-entry-on-LinuxUser-200908-grml-DVD
title: 'Information: broken boot entry on LinuxUser 2009/08 grml-DVD'

---
### English Version
(Eine deutsche Version dieses Textes ist am Ende diese Blogeintrags verfügbar. A german version of this text is available at the bottom of this blogentry.)
The [Grml 2009\.05 LinuxUser\-Edition DVD shipped with LinuxUser 2009/08](http://blog.grml.org/archives/323-Grml-2009.05-LinuxUser-Edition.html) sadly includes two errors. Neither data loss nor security risks, but broken boot entries instead. The grml team wants to inform users of the LinuxUser grml\-DVD about this issue.
* The grml64 flavour has two kernel entries (one being a leftover from the bootloader templates used for remastering) and due to murphy the wrong one is used. If you press the tab key with grml64 flavour being selected on the bootprompt you'll see:
> /boot/suse/linux ...

instead of:

> /boot/release/grml64/linux26

To work around this issue replace '/boot/suse/linux' with '/boot/release/grml64/linux26' at the grml64 entry on the bootprompt. Note: the failsafe64 entry does NOT have this problem and booting it works without problems when selecting the failsafe64 bootoption.
* The 'forensic64' bootoption uses 'live\-media\-path\=/live/grml/' instead of 'live\-media\-path\=/live/grml64/'. The system will boot with the wrong entry as well but instead of 64bit userland you'll get the 32bit userspace from flavour grml instead. To workaround this issue just edit the forensic64 bootoption at the bootprompt (press the tab key) and replace 'live\-media\-path\=/live/grml/' with 'live\-media\-path\=/live/grml64/'.
The grml team is very sorry about this fsckup. This was the first official remastering of a multi\-ISO grml\-DVD including a new bootlayout (isolinux with vesamenu) and sadly the configuration error wasn't caught during our tests. Please note that this error happened to the grml team and is NOT the fault of LinuxUser.
### German / Deutsche Version
Die [Grml 2009\.05 LinuxUser\-DVD die der LinuxUser\-Ausgabe 2009/08](http://blog.grml.org/archives/323-Grml-2009.05-LinuxUser-Edition.html) beiliegt hat leider zwei Fehler. Kein Datenverlust, keine Security\-Probleme, sondern kaputte Bootloader\-Einträge. Das Grml\-Team möchte mit diesem Blogeintrag Anwender der LinuxUser\-grml\-DVD über dieses Problem informieren.
* Der grml64\-Flavour besitzt zwei Kernel\-Einträge (einer ist ein Überbleibsel der Bootloader\-Vorlagen die für das Remastern verwendet wurden) und gemäß Murphy wird der falsche Eintrag verwendet. Wenn man bei ausgewähltem grml64\-Eintrag am Bootprompt die Tabulator\-Taste drückt, sieht man:

> /boot/suse/linux ...

statt dem korrekten Eintrag:

> /boot/release/grml64/linux26

Um dieses Problem zu umgehen, am Bootprompt bei den grml64\-Einträge das '/boot/suse/linux' einfach durch '/boot/release/grml64/linux26' ersetzen, dann bootet das System korrekt. Anmerkung: der Booteintrag 'failsafe64' hat dieses Problem NICHT und bootet defaultmäßig wie gewünscht!
* Die Bootoption 'forensic64' bootoption nutzt fälschlicherweise 'live\-media\-path\=/live/grml/' statt dem korrektem 'live\-media\-path\=/live/grml64/'. Das System bootet auch mit dem falschen Eintrag anstandslos, allerdings wird dann statt dem 64bit\-Userspace der 32bit\-Userspace vom Grml\-Flavour verwendet. Um dieses Problem zu korrigieren bitte am Bootprompt die forensic64\-Bootoption mit der Tabulator\-Taste editieren und 'live\-media\-path\=/live/grml/' durch 'live\-media\-path\=/live/grml64/' ersetzen.
Dem Grml\-Team tut dieser Fehler sehr leid und es bittet um Entschuldigung bei den Anwendern. Die grml\-DVD war das erste offizielle multi\-ISO in dieser Größe mit einem neuen Bootlayout (isolinux mit vesamenu). Leider wurde das Konfigurationsproblem in den Testläufen nicht entdeckt. Das Grml\-Team möchte explizit darauf hinweisen, dass dieser Fehler NICHT die Schuld von LinuxUser ist.
