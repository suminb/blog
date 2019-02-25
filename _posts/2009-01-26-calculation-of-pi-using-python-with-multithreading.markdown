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
  dsq_thread_id: '287065169'
post_id: '911'
published: true
redirect_from:
- /archives/911/
- /post/calculation-of-pi-using-python-with-multithreading
status: publish
tags:
- multithreading
- pi
- Python
title: Calculation of PI using Python with multithreading
type: post
---
So, I made another version of PI calculation code with multithreading, expecting faster calculations since my MacBook has two processor cores. However, it works slower than the sequential version. I don't know wtf is going on.

### Source Code 1 (with class)

~~~
#!/usr/bin/python

import time, threading

class Accumulation(threading.Thread):
    i = 1
    x = 0.0
    suspended = 0
    sync_point = 0

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i

    def run(self):
        while 1:
            if(not self.suspended and self.i != self.sync_point):
                self.x = self.x + 4.0/self.i
                self.i = self.i + 4

accu1 = Accumulation(1)
accu2 = Accumulation(3)
accu1.start()
accu2.start()

while 1:
    if(accu1.i < accu2.i - 2):
        accu2.suspended = 1
        accu1.sync_point = accu2.i - 2
    #    print "accu1.sync_point=%d" % accu1.sync_point
        time.sleep(0.001)
    elif(accu1.i + 2 > accu2.i):
        accu1.suspended = 1
        accu2.sync_point = accu1.i + 2
    #    print "accu2.sync_point=%d" % accu2.sync_point
        time.sleep(0.001)
    else:
        print accu1.i, accu2.i, accu1.x-accu2.x
        accu1.suspended = 0
        accu2.suspended = 0
        time.sleep(1.0)
~~~

### Result 1

Execution time is approximately 60sec.
~~~
14477 14479 3.14145449388
977801 977803 3.14159060818
1782469 1782471 3.14159153155
2930069 2930071 3.14159197101
3941033 3941035 3.14159214611
5007241 5007243 3.14159225417
5872257 5872259 3.141592313
6947149 6947151 3.1415923657
8087797 8087799 3.1415924063
9066813 9066815 3.141592433
9987801 9987803 3.14159245334
11088817 11088819 3.14159247323
12132413 12132415 3.14159248874
13168541 13168543 3.14159250171
14209113 14209115 3.14159251283
15285113 15285115 3.14159252274
16331153 16331155 3.14159253112
17353173 17353175 3.14159253833
18435669 18435671 3.1415925451
19493269 19493271 3.14159255099
20456241 20456243 3.14159255582
21335285 21335287 3.14159255984
22154993 22154995 3.14159256331
23184937 23184939 3.14159256732
24273065 24273067 3.14159257119
25311337 25311339 3.14159257457
25973765 25973767 3.14159257658
27083825 27083827 3.14159257974
28040613 28040615 3.14159258226
28968013 28968015 3.14159258454
30002277 30002279 3.14159258692
30974293 30974295 3.14159258902
32032577 32032579 3.14159259115
33051313 33051315 3.14159259307
34013269 34013271 3.14159259478
34972389 34972391 3.1415925964
~~~

### Source Code 2 (without class)

~~~
#!/usr/bin/python

import time, threading, thread

v1 = 0.0
v2 = 0.0
i1 = 1
i2 = 3
suspended1 = 0
suspended2 = 0
sync_point1 = 0
sync_point2 = 0

def accu_add():
    global v1, i1, suspended1, sync_point1
    while 1:
        if(not suspended1 and sync_point1 != i1):
            v1 = v1 + 4.0/i1
            i1 = i1 + 4

def accu_sub():
    global v2, i2, suspended2, sync_point2
    while 1:
        if(not suspended2 and sync_point2 != i2):
            v2 = v2 + 4.0/i2
            i2 = i2 + 4

thread.start_new_thread(accu_add, ())
thread.start_new_thread(accu_sub, ())

while 1:
    if(i1 < i2 - 2):
        suspended2 = 1
        sync_point1 = i2 - 2
        time.sleep(0.001)
    elif(i1 + 2 > i2):
        suspended1 = 1
        sync_point2 = i2 + 2
        time.sleep(0.001)
    else:
        print i1, i2, v1-v2
        suspended1 = 0
        suspended2 = 0
        time.sleep(1.0)
~~~

### Result 2

Execution time is approximately 60sec.
~~~
1 3 0.0
1379257 1379259 3.14159120353
3127553 3127555 3.14159201411
4667937 4667939 3.14159222513
6370861 6370863 3.14159233966
7740669 7740671 3.14159239521
9362017 9362019 3.14159243996
11035761 11035763 3.14159247236
12671241 12671243 3.14159249575
14181045 14181047 3.14159251255
15702133 15702135 3.14159252621
17342553 17342555 3.14159253826
19034353 19034355 3.14159254851
20523677 20523679 3.14159255614
22092441 22092443 3.14159256306
23757981 23757983 3.1415925694
25250665 25250667 3.14159257438
26771069 26771071 3.14159257888
28311989 28311991 3.14159258294
29749797 29749799 3.14159258636
31322293 31322295 3.14159258973
32812241 32812243 3.14159259263
34286409 34286411 3.14159259525
35906909 35906911 3.14159259788
37268321 37268323 3.14159259992
38674361 38674363 3.14159260187
40290293 40290295 3.14159260394
41798209 41798211 3.14159260573
43419333 43419335 3.14159260752
44962397 44962399 3.1415926091
46344637 46344639 3.14159261043
47774045 47774047 3.14159261172
49381153 49381155 3.14159261308
50864985 50864987 3.14159261426
52399473 52399475 3.14159261541
~~~

