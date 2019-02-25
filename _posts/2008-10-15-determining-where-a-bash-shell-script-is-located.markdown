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
  dsq_thread_id: '287065557'
post_id: '701'
published: true
redirect_from:
- /archives/701/
- /post/determining-where-a-bash-shell-script-is-located
status: publish
tags: []
title: Determining Where a Bash Shell Script Is Located
type: post
---
I just figured this out today.

    #!/bin/bash
    echo $(dirname $PWD/$0)
