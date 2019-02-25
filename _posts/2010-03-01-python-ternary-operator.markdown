---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Software Engineering
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287066565'
post_id: '1236'
published: true
redirect_from:
- /archives/1236/
- /post/python-ternary-operator
status: publish
tags:
- Python
title: Python Ternary Operator
type: post
---
I've been using a tuple as a substitution of a ternary operator in Python. Even though it is not exactly a ternary operator and has some drawbacks, but it works fine in most cases.

~~~
w = (u, v)[x < y]
~~~

When `x < y` is true, the whole expression of the tuple, `(u, v)[x < y]`, will be evaluated as `v` because true means 1 here. Likewise, false will cause the tuple expression to be evaluated as `u`.

I had another trick to use with lambda functions.

~~~
lambda w: x < y and v or u
~~~

This might be a little less obvious to see what's going on. When `x < y` is false, the following part, `and v`, will not be evaluated due to [short-circuit evaluation](http://en.wikipedia.org/wiki/Short-circuit_evaluation), and it will jump to the next part, `or u`. Thus, this whole expression is to be evaluated as `u`. Similarly, when `x < y` is true, `and v` part has to be evaluated so it the whole expression will be evaluated as `v`. 

However, as acute readers might already noticed, this trick has a major drawback. When `v` is a *falsy* value such as `0`, `False` or `None`, the whole expression will be evaluated as `u` regardless of the result of `x < y`. So, one should refrain from using this trick unless it is impossible for `v` to be a falsy value.

Last Saturday, Cody told me that there is a ternary operator equivalent in Python.

~~~
w = v if x < y else u
~~~

Strictly speaking, it is not a ternary *operator*, rather an expression. But, in my opinion, it is more intuitive thus it makes it easier to maintain the code.

