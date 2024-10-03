---
author: Michael Prokop
categories:
- general
date: Wed, 26 Oct 2005 16:05:00 +0000
layout: post
slug: 117-grml-on-soekris
title: grml on soekris

---
Kevin Krammer just let me know that he is running grml on [his Soekris box](http://www.soekris.com/net4801.htm):

    grml@grml ~ % cat /proc/cpuinfo  
    processor : 0  
    vendor_id : Geode by NSC  
    cpu family : 5  
    model : 9  
    model name : Unknown  
    stepping : 1  
    cpu MHz : 266.695  
    fdiv_bug : no  
    hlt_bug : no  
    f00f_bug : no  
    coma_bug : no  
    fpu : yes  
    fpu_exception : yes  
    cpuid level : 2  
    wp : yes  
    flags : fpu tsc msr cx8 cmov mmx cxmmx  
    bogomips : 534.63  
  
    grml@grml ~ % uname -a  
    Linux grml 2.6.13-grml #1 Sat Oct 22 11:05:29 CEST 2005 i586 GNU/Linux  
    grml@grml ~ % grml-version  
    0.5 Release Codename Tokolytika [2005-10-24]  
    grml@grml ~ %

Rocking :-)
