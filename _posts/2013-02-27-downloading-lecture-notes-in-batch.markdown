---
layout: post
title: Downloading Lecture Notes In Batch
post_id: '1729'
categories:
- Geeky Stuff
- Tutorial
- 생활 코딩 (Casual Coding)
tags:
- curl
- Python
- urllib2
- wget
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '1107926741'
  _thumbnail_id: '1730'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/1729/
---
Imagine you have about 25 lecture notes to download. The files are in a PDF format and the links are available on your class web site. What would you do?

<img src="/wp-content/uploads/2013/02/save-as.png" alt="save-as" width="355" height="306" class="aligncenter size-full wp-image-1730" />

This is probably what most people would do. Right click the link and *save as* a file. You *only* have to click three times for each file. You do a right click on the link, and another click on *save as*, then you confirm the save location. So that's about 75 clicks to download the entire lecture notes. It doesn't sound like a simple task anymore. We all know life is too short for this.

Let me explain how programmers would deal with this problem.

When lecture notes or assignments are properly numbered, it is almost trivial to download all of them at once. Suppose URLs are as following.

* `http://www.cs.arizona.edu/classes/cs433/spring13/hw1.pdf`
* `http://www.cs.arizona.edu/classes/cs433/spring13/hw2.pdf`
* ...
* `http://www.cs.arizona.edu/classes/cs433/spring13/hw5.pdf`

With a minimal amount of shell scripting, we can download all of them effortlessly.

    for i in $(seq 5); do wget http://www.cs.arizona.edu/classes/cs433/spring13/hw$i.pdf; done

However, sometimes the files are not necessarily named sequentially, and that makes the above code obsolete. Let's take a look at an example. [This page](http://www.cs.arizona.edu/classes/cs433/spring13/syl.html) contains well over 15 lecture notes.

We are going to use Python's `urllib2` library[^1],

    import urllib2

To read the content of the web page,

    content = urllib2.urlopen('http://www.cs.arizona.edu/classes/cs433/spring13/syl.html').read()

In order to use a regular expression library,

    import re

Then we will be able to extract all PDF file names with a little bit of regular expressions.

    list = re.findall('[^\s="]+\.pdf', content)

We could write some code to download these files, but there are utilities like `curl` and `wget` to accomplish that. No reason not to take advantage of. I think Mac OS X comes with `curl` by default and most Linux distros come with both. Sorry, Windows users. You might have to look elsewhere.

Now we are going to *synthesize* the command to download all files.

    ';'.join(map(lambda x: 'wget http://www.cs.arizona.edu/classes/cs433/spring13/%s' % x, list))

This should produce something like following.

    wget http://www.cs.arizona.edu/classes/cs433/spring13/slides/Intro.pdf;wget http://www.cs.arizona.edu/classes/cs433/spring13/slides/Transformations2D.pdf;wget http://www.cs.arizona.edu/classes/cs433/spring13/slides/OpenGLs.pdf; ...

Copy and paste it in the terminal. Now you can go get a cup of water and relax.

<a href="/wp-content/uploads/2013/02/download.png"><img src="/wp-content/uploads/2013/02/download-480x323.png" alt="download" width="480" height="323" class="aligncenter size-medium wp-image-1731" /></a>

[^1]: I like [`python-request`](http://docs.python-requests.org/en/latest/) better than `urllib2`, but we will stick with `urllib2` in this tutorial as it is installed by default in most Python distributions.

