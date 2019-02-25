---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Geeky Stuff
- 생활 코딩 (Casual Coding)
layout: post
meta:
  _edit_last: '1'
  _wp_old_slug: ''
  dsq_thread_id: '287065018'
post_id: '1327'
published: true
redirect_from:
- /archives/1327/
- /post/programmers-way-to-vote-on-doodle
status: publish
tags:
- doodle
- Google
- jquery
- safari
title: Programmers' Way To Vote On Doodle
type: post
---
[Doodle](http://doodle.com) is a great tool for organizing meetings and scheduling events, especially when attendees have largely different schedules.

<img src="/wp-content/uploads/2010/10/doodle-400x347.png" alt="" title="doodle" width="400" height="347" class="aligncenter size-medium wp-image-1331" />

A few days ago, my boss made a Doodle poll to organize our development meeting with nearly hundred time slots. Since I'm a full-time staff, I decided to check every single checkbox on the poll, which is *very* annoying. I was complaining about it, and my roommate[^Cody], who was playing Halo in his room, came to my room to make a great suggestion: to use [jQuery][jQuery]! So, here's how a programmer would solve the problem.

First, you need to be able to dynamically edit the content of a webpage. Since I'm a Safari user, I used the developers tool that comes with Safari. Google Chrome offers a similar feature. There's a great tool called [FireBug](http://getfirebug.com) for Firefox. If you're an Internet Explorer user, well, good luck.

<img src="/wp-content/uploads/2010/10/safari-devtool-400x79.png" alt="" title="safari-devtool" width="400" height="79" class="aligncenter size-medium wp-image-1335" />

Second, you'll need [jQuery][jQuery]. Google hosts a jQuery file for your convenience. It can be accessed at <http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js>. Of course, you don't have to use jQuery if you have other preferable libraries or you'd rather not use any. Other tools such as Dojo or Prototype can be also found at [Google Libraries API - Developer's Guide](http://code.google.com/apis/libraries/devguide.html).

Under `<head>`, insert the following line to use jQuery.

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>

Third, check all the checkboxes on the page.

    $('[type=checkbox]').each(function(i, e) { e.checked = 'checked' });

That's it.

<img src="/wp-content/uploads/2010/10/doodle-checkboxes.png" alt="" title="doodle-checkboxes" width="440" height="51" class="aligncenter size-full wp-image-1342" />

Now, enjoy your day instead of spending your invaluable time clicking the mouse over hundred times.

[jQuery]: http://jquery.com
[^Cody]: [Cody Jorgensen](http://www.facebook.com/Comster)

