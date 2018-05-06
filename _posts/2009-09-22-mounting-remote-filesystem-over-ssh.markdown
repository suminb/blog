---
layout: post
title: Mounting Remote Filesystem over SSH
post_id: '1179'
categories:
- Geeky Stuff
- Tutorial
tags:
- linux
- SSH
- sshfs
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '287066260'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/1179/
---
I've been using this shell script for a long time and it works pretty well unless I have really slow network connection. When I upgraded to Snow Leopard from Leopard, the installer got rid of all files under `/Volumes` directory where this script was located. I probably should've put the file under `/usr/bin`. So I'm posting this as a backup just in case I lose the file again, but please feel free to use it if you have `sshfs` installed on your system.

~~~
#!/bin/sh
# @author Sumin Byeon

URI=user@dev.sumin.us
MOUNTPOINT=/Volumes/dev.sumin.us
OPTIONS="reconnect,follow_symlinks"

if [ ! -d $MOUNTPOINT ]; then
	mkdir $MOUNTPOINT
fi

sshfs -o $OPTIONS $URI: $MOUNTPOINT
~~~

