---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Geeky Stuff
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287065694'
post_id: '300'
published: true
redirect_from:
- /archives/300/
- /post/convert-from-javautildate-to-javasqldate
status: publish
tags:
- Java
- sql
title: Convert from java.util.Date to java.sql.Date
type: post
---
# Content #

If you try to do like:

    Calendar cal = Calendar.getInstance();
    java.util.Date uDate = cal.getTime();
    java.sql.Date sDate = (java.sql.Date) uDate;

You will obtain a cast exception. Instead, you can do like:

    Calendar cal = Calendar.getInstance();
    java.util.Date uDate = cal.getTime();
    java.sql.Date sDate = new java.sql.Date(uDate.getTime());

# References #

* [http://www.dbforums.com/t1100948.html](http://www.dbforums.com/t1100948.html)
* [http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Date.html](http://java.sun.com/j2se/1.5.0/docs/api/java/sql/Date.html)
* [http://java.sun.com/j2se/1.5.0/docs/api/java/util/Date.html](http://java.sun.com/j2se/1.5.0/docs/api/java/util/Date.html)

