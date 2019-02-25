---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Mathematics
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287065411'
post_id: '1196'
published: true
redirect_from:
- /archives/1196/
- /post/finding-gram-matrix
status: publish
tags:
- linear algebra
- Python
title: Finding Gram Matrix
type: post
---
Matrix manipulation by hand is often times pain in the neck when it comes to anything bigger than 2 by 2 matrices as it involves a quite amount of arithmetic operations. Well, I've got an Intel Core 2 Duo processor and Python. No reason not to take advantage of them ;-)

### Source Code
~~~
__author__ = 'Sumin Byeon <sumin@cs.arizona.edu>'

from Numeric import *

# u and v are lists of same lengths
def inner_product(u, v):
    return reduce(int.__add__, map(lambda x: x[0]*x[1], zip(u, v)))

# vs: a list of vectors
def gram_matrix(*vs):
    n = len(vs)
    mx = zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            mx[i,j] = inner_product(vs[i], vs[j])
    return mx
~~~

### Result
~~~
>>> gram_matrix([1,0,0,1], [-2,1,0,0], [-1,0,-1,0], [0,2,-3,0])
[[ 2 -2 -1  0]
 [-2  5  2  2]
 [-1  2  2  3]
 [ 0  2  3 13]]
~~~

