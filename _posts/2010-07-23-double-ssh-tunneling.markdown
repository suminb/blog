---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Tutorial
layout: post
meta:
  _edit_last: '1'
  _wp_old_slug: ''
  dsq_thread_id: '287066124'
post_id: '1318'
published: true
redirect_from:
- /post/double-ssh-tunneling
status: publish
tags:
- SSH
title: Double SSH Tunneling
type: post
---
This is just a self-reminder.

    ssh -t -L 8000:localhost:8000 lec.cs.arizona.edu 'ssh -L 8000:sebeos:80 robotlab@sebeos'

`lec.cs.arizona.edu` is in the DMZ, and `sebeos.cs.arizona.edu` is one of the machines in the robot lab, which is behind the firewall. So, I'm basically *double* tunneling to `sebeos` via `lec` to access to `sebeos` from outside the firewall.
