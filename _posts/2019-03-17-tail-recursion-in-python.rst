---
author:
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
categories:
- Computer Science
draft: true
layout: post
meta: null
published: true
tags:
- python
title: Tail Recursion in Python
---

요즘 `LeetCode <https://leetcode.com/>`_ 에서 하루에 하나씩 알고리즘 문제를
풀고 있는데,\ [#leet]_ 재귀 호출을 이용할 때가 많다. 특히 트리나 그래프를 깊이
우선 탐색(BFS)할 때 직접 `스택
<https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>`_\ 에 값을 넣고 빼지
않아도 되기 때문에 편리하게 구현할 수 있다. 당연한 이야기겠지만, 내 코드에서
관리되는 스택이 아니라 시스템 스택을 사용하기 때문에 가능한 것이다.

재귀 호출은 구현이 편리하긴 하지만 나름의 문제를 가지고 있다. 재귀 호출 스택의
깊이가 얕은 경우에는 어떻게 구현하든 별로 상관이 없는데, 깊이가 깊어지면 문제가
될 수도 있다.

그럼 파이썬에서 가능한 호출 스택의 최대 깊이는 얼마일까?

.. code:: python

    def recurse(n):
        print(n)
        recurse(n + 1)

나와 비슷한 궁금증을 가진 사람의 블로그 포스트를 참고하여\ [#max-depth]_ 현재
시스템에서 가능한 가장 깊은 호출 스택의 깊이를 측정해보았다.

.. code::

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 3, in recurse
      File "<stdin>", line 3, in recurse
      File "<stdin>", line 3, in recurse
      [Previous line repeated 992 more times]
      File "<stdin>", line 2, in recurse
    RecursionError: maximum recursion depth exceeded while calling a Python object
    997

포스트 작성자의 시스템과 마찬가지로 내 시스템에서도 997이 최대로 나온다.

참고로 이 값은 ``sys.setrecursionlimit()`` 함수를 이용해서 오버라이드 할 수
있다.\ [#setrecursionlimit]_ 물론 무한대로 늘릴 수 있는건 아니다. 아주 큰 값을
넣고 실험해본 결과 다음과 같이 segmentation fault가 발생했다.

.. code::

    ...
    34936
    34937
    34938
    [1]    73359 segmentation fault  python

다시 말해서 ``N``\ 의 값이 충분히 크다면 마음 놓고 재귀 호출을 사용할 수 없다는
뜻이다. 해결책은 크게 두 가지다.

1. Iterative solution
2. Tail recursion

오늘은 두 번째 해결책에 대한 이야기를 해보고자 한다.


Tail Recursion
--------------
한국어로는 '꼬리 재귀'라고 표현하기도 하는데,\ [#tail-recursion-ko]_ 널리
쓰이는 용어인지는 잘 모르겠다. 이 글에서는 그냥 원래 용어 그대로 tail recursion
이라고 표기하도록 하겠다.

위키피디아는 tail recursion을 다음과 같이 정의하고 있다.\ [#tail-recursion]_

    In computer science, a tail call is a subroutine call performed as the
    final action of a procedure. If a tail call might lead to the same
    subroutine being called again later in the call chain, the subroutine is
    said to be tail-recursive, which is a special case of recursion. Tail
    recursion (or tail-end recursion) is particularly useful, and often easy to
    handle in implementations.

조금 더 간단히 이야기 하자면, 함수에서 마지막으로 호출하는 함수가 자기
자신이고, 재귀 호출이 끝난 뒤 추가적인 연산이 필요하지 않다면 tail recursion
이라고 볼 수 있다. 재귀 호출 후 추가적인 연산이 필요하지 않다면 진짜로 함수를
호출하는 것 처럼 시스템 콜 스택에 이것저것 저장하지 않고 선형적으로 구현할 수
있다.

팩토리얼을 연산하는 파이썬 코드를 예제로 사용해보자.

.. code:: python

    def factorial(n):
      if n == 0:
          return 1
      else:
          return n * factorial(n - 1)

``factorial(n - 1)`` 호출이 끝난 후 ``n``\ 의 값과 곱해주어야 하기 때문에, 다시
말해서, ``factorial(n)``\ 의 실행이 완료 되지 않은 상태에서 ``factorial(n -
1)``\ 를 호출하기 때문에 리턴 주소를 저장하기 위해서 시스템 콜 스택을 사용할 수
밖에 없다.

Tail Recursion Elimination (TRE)
--------------------------------

위와 같이 tail recursion 조건을 만족한다면 실제로 함수를 호출하지 않는
반복해(iterative solution) 코드로 변경할 수 있다. 이러한 과정을 tail recursion
elimination (TRE) 이라고 한다. 그렇게 하기 위해서는 ``factorial(n - 1)``\ 의
연산이 끝난 후 추가적인 연산이 필요 없도록 만들어야 한다. 위의 코드를 조금
바꾸어 다음과 같이 작성할 수 있다.

.. code:: python

    def factorial(n, result=1):
      if n == 0:
          return result
      else:
          return factorial(n - 1, n * result)

만약, 파이썬 인터프리터가 TRE를 할 수 있다면 위의 코드는 다음과 같이 변환될
것이다.

.. code:: python

    def factorial(n, result=1):
        while n != 0:
            result = n * result
            n = n - 1
        return result

Scala와 같은 언어에서는 tail recursion optimization을 기본으로 제공하기도
하고,\ [#tail-recursion-in-scala]_ Haskell과 같은 언어에서는 함수 호출이 항상
새로운 스택 프레임을 사용하지 않을 수도 있기 때문에\
[#tail-recursion-in-haskell]_ 마음놓고 재귀 호출을 사용할 수 있지만, 파이썬의
경우 아쉽게도 그런 호사는 누릴 수 없다.


Home-Brewing TRE
----------------

없으면 만들어야지. 이것도 크게 두 가지 방법이 있을 것 같다.

1. 파이썬 인터프리터를 수정하기\ [#python-switch-statement]_
2. 재귀 호출할 때 함수를 다른걸로 바꿔치기

1번이 더 멋진 일이지만, 작업 분량과 난이도를 생각했을 때 2번이 조금 더 현실적인
대안이라고 생각했다.

.. code:: python

    return factorial(n - 1, n * result)

파이썬은 런타임에 뭐든지 바꿀 수 있는 언어이기 때문에 위와 같이 재귀 호출이
일어나는 부분에서 ``factorial()`` 함수를 다른 것으로 바꾸어서 재귀 호출이 아닌
다른 일이 일어나도록 만들면 원하는 바를 이룰 수 있다.

하지만 역시 이런 생각은 내가 세계 최초로 한 것이 아니기 때문에 이미 누군가가 잘
만들어놓은 코드가 있었다.\ [#tre]_ 원작자가 만든 코드를 내 입맛에 맞게 아주
조금만 수정해보았다.

먼저, TRE를 하기 위해 필요한 몇가지 구성 요소들이 있다.

.. code:: python

    class Recursion(Exception):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs


    def recurse(*args, **kwargs):
        raise Recursion(*args, **kwargs)


    def tail_recursion(f):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return f(*args, **kwargs)
                except Recursion as r:
                    args = r.args
                    kwargs = r.kwargs
        return wrapper

그리고 ``factorial()`` 함수는 다음과 같이 수정한다.

.. code:: python

    @tail_recursion
    def factorial(n, result=1):
        from trlib import recurse as factorial
        if n == 0:
            return result
        else:
            return factorial(n - 1, result * n)

기본적인 아이디어는 ``factorial()`` 함수를 실제로 재귀적으로 호출하는 대신,
내부적으로 다른 일이 일어나도록 만드는 것이다.

재귀 호출이었다면 다음과 같이 ``factorial()`` 함수 호출의 흔적이 시스템 스택에
차곡차곡 쌓였을텐데,

.. code::

    factorial(n=5, result=1)
      factorial(n=4, result=5)
        factorial(n=3, result=20)
          factorial(n=2, result=60)
            factorial(n=1, result=120)
              factorial(n=0, result=120)

TRE 코드에서는 스택의 깊이가 깊어지지 않는다.

.. code::

    factorial(n=5, result=1)
    factorial(n=4, result=5)
    factorial(n=3, result=20)
    factorial(n=2, result=60)
    factorial(n=1, result=120)
    factorial(n=0, result=120)

실제로 큰 값을 가지고 (e.g., ``n = 2000``) 테스트를 해보면 재귀 호출 코드의
경우 ``RecursionError: maximum recursion depth exceeded in comparison``\ 와
같은 오류 메시지가 발생하는 반면, TRE 코드는 아무 문제 없이 주어진 연산을
수행하는 것을 확인할 수 있다.

Dive Deep
---------

일단 돌아가게 만들어 놓긴 했는데, 성능은 어떨까? 파이썬 3.7 문서에서는 다음과
같이 명시하고 있다.\ [#python-exception-cost]_

    A try/except block is extremely efficient if no exceptions are raised.
    Actually catching an exception is expensive.

하지만 우리는 재귀 함수의 종료 조건이 만족되지 않는 이상 실제로 예외를 캐치하고
있기 때문에 성능상 비싼 값을 치르고 있을 수도 있다. 그래서 얼마나 느린지 직접
테스트를 해보기로 했다. 테스트 코드는 `Gist
<https://gist.github.com/suminb/7118ffb2251b07701b4f8bb9dbd7f899>`_\ 에
올려두었다.

.. code::

    recursive_code
    3.60 usec/pass

    tail_recursive_code
    3.90 usec/pass

    tail_recursion_eliminated_code
    28.68 usec/pass

일반적인 재귀 호출 코드와 꼬리 재귀(tail recursion) 호출 코드는 대동소이한
반면, TRE 코드는 일곱 배 이상 느린 것으로 나타났다(!) 성능을 개선하려면
``try``/``except`` 구문을 사용하지 않고 다른 방법으로 구현해야 할 것 같다.

(TODO: 다른 방법으로 구현해보기)

Conclusion
----------
파이썬으로 알고리즘 문제를 풀다가 느낀 불편함으로 인해 한참동안 야크 털을 깎은
것 같은데,\ [#yak-shaving]_ 나름 즐거운 경험이었다.

파이썬에서의 TRE에 대한 비판 의견도 있다.\ [#critiques-on-tre]_ TRE를 도입할 경우 스택 트레이스가 어려워질 뿐만 아니라 재귀 호출이 프로그래밍의 


Footnotes
---------

.. [#leet] https://github.com/suminb/coding-exercise/tree/master/leetcode
.. [#tail-recursion] https://en.wikipedia.org/wiki/Tail_call
.. [#tail-recursion-ko] https://ko.wikipedia.org/wiki/%EA%BC%AC%EB%A6%AC_%EC%9E%AC%EA%B7%80
.. [#tail-recursion-in-scala] https://www.scala-exercises.org/scala_tutorial/tail_recursion
.. [#tail-recursion-in-haskell] https://wiki.haskell.org/Tail_recursion
.. [#max-depth] https://mattjegan.com/Chasing-Pythons-Recursion-Limit/
.. [#setrecursionlimit] https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
.. [#python-switch-statement] `성우경 <https://www.linkedin.com/in/ukysung/>`_\ 님의 `파이썬에 switch문 넣기: 새 구문을 만들면서 배우는 파이썬 내부 <https://archive.pycon.kr/2018/program/49>`_ 발표를 보고 파이썬 인터프리터를 입맞에 맞게 고쳐서 쓰는 일이 불가능한 일은 아니라는 용기를 얻었다.
.. [#tre] https://chrispenner.ca/posts/python-tail-recursion
.. [#python-exception-cost] https://docs.python.org/3.7/faq/design.html#how-fast-are-exceptions
.. [#yak-shaving] https://www.lesstif.com/pages/viewpage.action?pageId=29590364
.. [#critiques-on-tre] https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
