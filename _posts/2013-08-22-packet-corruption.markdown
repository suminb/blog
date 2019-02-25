---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Troubleshooting
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '1627458270'
post_id: '1883'
published: true
redirect_from:
- /archives/1883/
- /post/packet-corruption
status: publish
tags: []
title: Packet Corruption
type: post
---
I encountered a very strange error message that I have never come across before. I was transferring a large file (a few gigabytes) from a computer to another using `rsync`.

    Received disconnect from xx.xxx.xx.xx: 2: Packet corrupt

I initially suspected `rsync` was being silly, so I tried it with `scp`. Same result.

Sometimes I see slightly different error messages:

    Corrupted MAC on input.
    Disconnecting: Packet corrupt

So I Googled around and found a number of related pages:

* <https://bugs.launchpad.net/ubuntu/+source/linux-source-2.6.17/+bug/60764>
* <http://serverfault.com/questions/338439/ssh-sessions-terminate-abruptly-with-message-corrupted-mac-on-input-disconnect>
* <http://blog.e-shell.org/270>
* <http://verahill.blogspot.com/2012/09/briefly-packet-corrupt-during-ssh.html>

This is enough to lead me to believe that the on-board network interface card has some issues. Maybe I'm filling the buffer faster than it can flush out. Or it could be a nasty bug in the Linux kernel. Either way, it's not something that I can fix very easily.

What if I slow down a bit? Would it make any difference?

As `rsync` manual explains:

    --bwlimit=KBPS          limit I/O bandwidth; KBytes per second

I've tried this:

    rsync -aP -e ssh --bwlimit=500 archive.tgz some.remote.host:path/

It would take it to a little bit further, but it still failed.

As a temporary solution, I wrote a simple shell script:

    while [ 1 ]; do
      rsync -aP -e ssh --bwlimit=500 archive.tgz some.remote.host:path/
      if [ $? -eq 0 ]; then exit; fi;
    done

This will keep trying the file transfer until `rsync` exits with a status code `0` which indicates a normal exit.

The only way to test my hypothesis (that it is a hardware problem) is to try the same file transfer with a different network interface card. 

