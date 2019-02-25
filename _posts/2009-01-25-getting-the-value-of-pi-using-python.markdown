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
  dsq_thread_id: '287065226'
post_id: '894'
published: true
redirect_from:
- /archives/894/
- /post/getting-the-value-of-pi-using-python
status: publish
tags:
- pi
- Python
title: Calculation of PI using Python
type: post
---
I barely started using Python today. I made a piece of code that calculates the value of PI for practice. You're welcome to criticize, but *politely*, my first ever Python code.

### Source Code

I apology if this makes you unhappy because it doesn't look like python code. Trust me. It will be a lot better if I keep using Python.
~~~
#!/usr/bin/python

import time, threading

class PrintValue(threading.Thread):
    def run(self):
        while 1:
            print x
            time.sleep(1.0)

i = 1
x = 0.0

printvalue = PrintValue()
printvalue.start()

while 1:
    if(i%2):
        x += 4.0/(i*2-1)
    else:
        x -= 4.0/(i*2-1)
    i = i + 1
~~~
As you can see, this code will never stop. It will print out the value of PI every second. If you want to stop, give it a substitute character (Ctrl + Z).

Also, I believe this is not thread-safe. However, it probably won't cause any problem because `PrintValue` does not change the value of `x`. The only possible problem here, as far as I can tell, is the inaccuracy of the value of `x` printed on the screen at the moment when the statement `print x` (under `PrintValue.run()`) is executed. Well, the value of `x` is an approximation of the value of PI anyway ;-)

### Result
<a href="http://gallery.sumin.us/v/screenshots/general/6c7e32ea743c770a.png.html"><img src="http://gallery.sumin.us/d/1437-1/6c7e32ea743c770a.png" alt="" /></a>

### TODO
* Fully utilizing two processor cores on my MacBook
* Measurement of time to calculate up to a certain number of digits

### References
* <http://en.wikipedia.org/wiki/Pi>

