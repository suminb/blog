---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Computer Science
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287065458'
post_id: '1119'
published: true
redirect_from:
- /archives/1119/
- /post/permutation-generation
status: publish
tags:
- haskell
- math
- Python
- recursion
title: Permutation Generation
type: post
---
Someone asked me how to generate all possible permutations out of a given set and I thought it was kind of interesting to think about it. I was able to come up with a general solution pretty easily (thanks to all the algorithm and math classes I took!) and I would like to share it with everyone.

### Recursive solution

For a given set, *S*,

$$p(S) =
\begin{cases}
  \{\emptyset\},  & \mbox{if } S = \emptyset \\
  \{\{s_1\} + p(S - \{s_1\}), \{s_2\} + p(S - \{s_2\}), ..., \\
    \mbox{  } \{s_n\} + p(S - \{s_n\}) \}, & \mbox{otherwise}
\end{cases}$$

whereas `+` and `-` signs denote set addition and set subtraction respectively.

### Python implementation

~~~
def permutation(set):
        if set == []:
                return [[]]
        else:
                r = []
                for i in xrange(0, len(set)):
                        for p in permutation(set[0:i] + set[i+1:]):
                                r.append([set[i]] + p)
                return r
~~~

### Results

~~~
>>> print permutation([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
~~~

I wouldn't say this particular implementation is *the most efficient* one, but at least we know it works with up to a certain size of set. Sadly, we all have machines with a finite size of memory, our machine will produce stack overflow if your set is too big.

I think languages like Haskell would work very efficiently with this kind of recursive solution due to its beautiful features like lazy evaluation, tail recursion, etc. Please feel free to share your solution or implementation.

