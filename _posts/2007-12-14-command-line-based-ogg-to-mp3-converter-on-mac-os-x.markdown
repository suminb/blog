---
layout: post
title: Command Line Based ogg to mp3 Converter on Mac OS X
post_id: '693'
categories:
- Tutorial
tags:
- mac
- MP3
- OGG
- OSX
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '287066210'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/693/
---
First of all, you need to install `vorbis-tools` and `lame`, assuming you have [MacPorts](http://www.macports.org/) installed. If you're using some other package management system, that's fine. Go ahead and install these two packages. If you don't have any, you can always manually install it.

	sudo port install vorbis-tools lame

I'm going to decode an ogg file into a wav file and then convert the wav file to an mp3 file. For example,

	oggdec test.ogg
	lame -h --vbr-new test.ogg

If you want to make an mp3 file with a constant bit rate, use `-b` option. Refer `lame --help` for details. However, it is not a good idea to manually invoke this command for every single file you want to convert. So, I'm gonna make a very simple shell script to do all the works.

	#/bin/bash

	for file in *.ogg; do
		oggdec $file
		file=$(basename $file .ogg)
		lame -h --vbr-new -V 2 "${file}.wav" "${file}.mp3"
		rm "${file}.wav"
	done

I'm giving an option `-V 2` to specify VBR quality of the result. 0 for highest and 9 for lowest quality.

Here's a screenshot:

<a href="http://gallery.sumin.us/v/screenshots/general/ogg_to_mp3.png.html"><img src="http://gallery.sumin.us/d/463-1/ogg_to_mp3.png" alt="" class="aligncenter" /></a>

