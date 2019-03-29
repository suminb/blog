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
summary: 파이썬에서 꼬리 재귀 제거(tail recursion elimination)를 구현한 이야기
og_image: /attachments/2019/tail-recursion-in-python/tail-recursion.jpg
og_image_source: https://stackoverflow.com/a/54573509
---

요즘 `LeetCode <https://leetcode.com/>`_ 에서 하루에 하나씩 알고리즘 문제를
풀고 있는데,\ [#leet]_ 재귀 호출을 이용할 때가 많다. 특히 트리나 그래프를 `깊이
우선 탐색(DFS) <https://en.wikipedia.org/wiki/Depth-first_search>`_\ 할 때 직접
`스택 <https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>`_\ 에 값을
넣고 빼지 않아도 되기 때문에 편리하게 구현할 수 있다. 당연한 이야기겠지만, 내
코드에서 관리되는 스택이 아니라 시스템 스택을 사용하기 때문에 가능한 것이다.

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
2. Tail recursion elimination

오늘은 두 번째 해결책에 대한 이야기를 해보고자 한다.


Tail Recursion
--------------
검색을 해보니 한국어로는 '꼬리 재귀'라고 표현하는 것으로 보인다.\
[#tail-recursion-ko]_ 개인적으로는 tail recursion이 더 익숙한 용어이긴 하지만,
글을 쓸 때 한/영 전환을 하는 것은 번거로운 일이기 때문에(?) 이 글에서는 꼬리
재귀로 표기하도록 하겠다.

위키피디아는 꼬리 재귀를 다음과 같이 정의하고 있다.\ [#tail-recursion]_

    In computer science, a tail call is a subroutine call performed as the
    final action of a procedure. If a tail call might lead to the same
    subroutine being called again later in the call chain, the subroutine is
    said to be tail-recursive, which is a special case of recursion. Tail
    recursion (or tail-end recursion) is particularly useful, and often easy to
    handle in implementations.

조금 더 간단히 이야기 하자면, 함수에서 마지막으로 호출하는 함수가 자기
자신이고, 재귀 호출이 끝난 뒤 추가적인 연산이 필요하지 않다면 꼬리 재귀라고 볼
수 있다. 재귀 호출 후 추가적인 연산이 필요하지 않다면 진짜로 함수를 호출하는 것
처럼 시스템 콜 스택에 이것저것 저장하지 않고 선형적으로 구현할 수 있다.

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

조금 더 깊숙히 들여다보기 위해 `파이썬 바이트 코드
<https://opensource.com/article/18/4/introduction-python-bytecode>`_\ 를
해부해보도록 하자. |dis-package|_\ 를 이용하면 손쉽게 바이트 코드를 볼 수 있다.

.. |dis-package| replace:: ``dis`` 패키지
.. _dis-package: https://docs.python.org/3/library/dis.html

.. code::

    >>> dis.dis(factorial)
    2           0 LOAD_FAST                0 (n)
                2 LOAD_CONST               1 (0)
                4 COMPARE_OP               2 (==)
                6 POP_JUMP_IF_FALSE       12

    3           8 LOAD_CONST               2 (1)
                10 RETURN_VALUE

    5     >>   12 LOAD_FAST                0 (n)
                14 LOAD_GLOBAL              0 (factorial)
                16 LOAD_FAST                0 (n)
                18 LOAD_CONST               2 (1)
                20 BINARY_SUBTRACT
                22 CALL_FUNCTION            1
                24 BINARY_MULTIPLY
                26 RETURN_VALUE
                28 LOAD_CONST               0 (None)
                30 RETURN_VALUE

여기서 주의 깊게 봐야 할 부분은 ``factorial()`` 함수를 호출하는 부분이다.

.. code::

                14 LOAD_GLOBAL              0 (factorial)
                16 LOAD_FAST                0 (n)
                18 LOAD_CONST               2 (1)
                20 BINARY_SUBTRACT
                22 CALL_FUNCTION            1

평가 스택(evaluation stack)에 ``n``\ 과 ``1``\ 을 넣은 후 ``BINARY_SUBTRACT``
명령어를 수행하면 평가 스택에서 값 두 개를 꺼내서 빼기 연산을 수행하고, 그
결과를 다시 평가 스택에 넣는다. 그런 다음 ``CALL_FUNCTION`` 명령어의
인자(``1``) 만큼 평가 스택에서 값을 꺼내고, 그 전에 넣어 놓았던 함수
이름(``factorial``)을 꺼내서 함수를 호출한다.

.. code::

                24 BINARY_MULTIPLY
                26 RETURN_VALUE

바이트 코드를 계속 이어서 보자면, ``factorial()`` 함수 호출이 끝나면 함수 실행
결과 값이 평가 스택에 저장되고, 곧이어 ``BINARY_MULTIPLY`` 명령어를 호출한다.
함수 호출 결과값과 ``LOAD_GLOBAL (factorial)`` 명령어 이전에 평가 스택에
넣어놨던 ``n``\ 을 꺼내서 곱한 후 그 결과를 다시 평가 스택에 넣는다.
``RETURN_VALUE`` 명령어는 평가 스택에서 값을 하나 꺼내 현재 함수의
호출자(caller)에게 돌려준다.

.. code::

    return n * factorial(n - 1)

이로써 위와 같은 파이썬 코드가 수행되는 과정을 간략하게 살펴보았는데, 핵심은
현재 함수(``factorial(n)``)에서 결과값을 반환하기 위해서는 현재 함수의 인자
값(``n``)을 평가 스택에 가지고 있다가 그 다음 호출 될 함수(``factorial(n -
1)``)의 결과 값과 함께 연산을 해야 하기 때문에 재귀 호출이 불가피하다는 점이다.

.. raw:: html

    <!-- TODO: Define a set of styles for this -->
    <div style="margin: 1em 0 1.5em 0; padding: 1em; background: #f8ffff; color: rgba(0,0,0,.87); box-shadow: 0 0 0 1px #a9d5de inset,0 0 0 0 transparent; border-radius: 4px; font-size: 0.9em;">
        <h4 style="margin: 0.5em 0;">토막 상식</h4>
        <div>

함수의 최상위 블럭에 ``return`` 구문이 없을 경우 함수의 바이트 코드 맨 뒤쪽에는
항상 ``None``\ 을 반환하는 코드가 붙는다. 예를 들어서, 다음과 같은 코드의 경우
``return`` 구문이 실행되지 않는 경우는 없겠지만, ``return`` 구문이 모두
``if``/``else`` 조건문 안쪽에 있고, 최상위 블럭에는 ``return`` 구문이 존재하지
않는다.

.. code:: python

    def f(x):
        if x == 0:
            return x
        else:
            return x + 1

바이트 코드의 끝 부분을 보면 다음과 같이 ``None``\ 을 반환하는 코드가 붙는다.

.. code::

    >>> dis.dis(f)
    ..(중략)..
             18 RETURN_VALUE
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE

반면, 다음과 같은 코드는 위 코드와 논리적으로 아무런 차이가 없지만, ``return``
구문이 함수의 최상위 블럭에 존재하기 때문에 ``None``\ 을 반환하는 코드가
추가되지 않는다.

.. code:: python

    def g(x):
        if x == 0:
            return x
        return x + 1

따라서 다음과 같이 ``return x + 1`` 구문을 마지막으로 따로 추가되는 명령어는
없다.

.. code::

    >>> dis.dis(g)
    ..(중략)..
    4     >>   12 LOAD_FAST                0 (x)
                14 LOAD_CONST               2 (1)
                16 BINARY_ADD
                18 RETURN_VALUE

다음과 같이 아무것도 하지 않는 함수라고 하더라도 ``None``\ 을 반환하도록
되어있다.

.. code:: python

    def h(x):
        pass

바이트 코드는 다음과 같다.

.. code::

    >>> dis.dis(h)
    1           0 LOAD_CONST               0 (None)
                2 RETURN_VALUE

참고: CPython 이외의 인터프리터에서는 테스트해보지 않았다.

.. raw:: html

        </div>
    </div>

그럼 이 함수를 꼬리 재귀로 바꾸려면 어떻게 해야 할까. 재귀 호출을 하는 부분에서
추가적인 연산이 필요 없도록 만들면 된다. 코드를 살짝 수정하여 아래와 같이
바꾸어 볼 수 있을 것이다.

.. code:: python

    def factorial(n, result=1):
      if n == 0:
          return result
      else:
          return factorial(n - 1, n * result)

바이트 코드도 살펴보도록 하자.

.. code::

    >>> dis.dis(factorial)
    2           0 LOAD_FAST                0 (n)
                2 LOAD_CONST               1 (0)
                4 COMPARE_OP               2 (==)
                6 POP_JUMP_IF_FALSE       12

    3           8 LOAD_FAST                1 (result)
                10 RETURN_VALUE

    5     >>   12 LOAD_GLOBAL              0 (factorial)
                14 LOAD_FAST                0 (n)
                16 LOAD_CONST               2 (1)
                18 BINARY_SUBTRACT
                20 LOAD_FAST                0 (n)
                22 LOAD_FAST                1 (result)
                24 BINARY_MULTIPLY
                26 CALL_FUNCTION            2
                28 RETURN_VALUE
                30 LOAD_CONST               0 (None)
                32 RETURN_VALUE

가장 핵심적인 차이점은 이것이다.

.. code::

            26 CALL_FUNCTION            2
            28 RETURN_VALUE

``factorial()`` 함수를 재귀적으로 호출하긴 하지만, 결과값을 받아서 추가적인
연산을 하지 않고 바로 반환하도록 되어있다. 이로써 꼬리 재귀의 조건을 충족시킬
수 있게 되었다.


Tail Recursion Elimination (TRE)
--------------------------------

위와 같이 꼬리 재귀 조건을 만족한다면 실제로 함수를 호출하지 않는
반복해(iterative solution) 코드로 변경할 수 있다. 이러한 과정을 tail recursion
elimination (TRE) 이라고 한다. 만약, 파이썬 바이트 코드 컴파일러가 TRE를 할 수
있다면 앞서 소개했던 꼬리 재귀 코드는 다음과 같이 변환될 것이다.

.. code:: python

    def factorial(n, result=1):
        while True:
            if n == 0:
                return result
            else:
                result = n * result
                n = n - 1

컴파일러가 충분히 똑똑하다면 조금 더 괜찮은 코드를 작성할 수 있을지도 모른다.

.. code:: python

    def factorial(n, result=1):
        while n != 0:
            result = n * result
            n = n - 1
        return result

Scala와 같은 언어에서는 꼬리 재귀 최적화(tail recursion optimization)를
기본으로 제공하기도 하고,\ [#tail-recursion-in-scala]_ Haskell과 같은
언어에서는 함수 호출이 항상 새로운 콜 스택 프레임을 사용하지 않을 수도 있기
때문에\ [#tail-recursion-in-haskell]_ 마음놓고 재귀 호출을 사용할 수 있지만,
파이썬의 경우 아쉽게도 그런 호사는 누릴 수 없다.


Home-Brewing TRE
----------------

없으면 만들어야지. 이것도 크게 두 가지 해결책이 있을 것 같다.

1. 파이썬 인터프리터를 수정하기\ [#python-switch-statement]_
2. 재귀 호출할 때 함수를 다른걸로 바꿔치기

내 관점에서는 1번이 더 멋진 일이지만, 작업 분량과 난이도를 생각했을 때 2번이
조금 더 현실적인 대안이라고 생각했다.

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

재귀 호출이었다면 다음과 같이 ``factorial()`` 함수 호출의 흔적이 콜 스택에
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

하지만 우리는 재귀 함수의 종료 조건이 만족될 때를 제외하고는 실제로 예외를
캐치하고 있기 때문에 성능상 비싼 값을 치르고 있을 수도 있다. 그래서 얼마나
느린지 직접 테스트를 해보기로 했다. 테스트 코드는 `Gist
<https://gist.github.com/suminb/7118ffb2251b07701b4f8bb9dbd7f899>`_\ 에
올려두었다.

.. code::

    recursive_code
    0.305 ms/pass

    tail_recursive_code
    0.416 ms/pass

    tail_recursion_eliminated_code
    1.916 ms/pass

일반적인 재귀 호출 코드와 꼬리 재귀(tail recursion) 호출 코드는 대동소이한
반면, TRE 코드는 여섯 배 가량 느린 것으로 나타났다(!) 성능을 개선하려면
아무래도 ``try``/``except`` 구문을 사용하지 않고 다른 방법으로 구현해야 할 것
같다.

우리가 ``try``/``except`` 구문을 사용하는 이유는 신호를 전달하기 위함이다.
이번에 재귀 호출을 해야 하는지, 아니면 종료 조건이 만족되어 그냥 결과값을
반환하면 되는지 판단하고, 그 결과를 ``tail_recursion()`` 안쪽의 ``wrapper()``
함수로 전달할 수 있으면 된다. 그래서 다음의 두 가지 방법을 시도해봤다.

Take One: Globals
~~~~~~~~~~~~~~~~~

먼저, 전역 변수를 이용해서 신호를 전달하는 방식으로 코드를 조금 수정해보았다.

.. code:: python

    g = globals()


    def recurse(*args, **kwargs):
        g['@caller_id'] = (True, args, kwargs)


    def tail_recursion(f):
        def wrapper(*args, **kwargs):
            caller_id = f.__name__
            while True:
                g[caller_id] = (False, args, kwargs)
                result = f(*args, **kwargs)
                recursion, args, kwargs = g[caller_id]
                if not recursion:
                    return result
        return wrapper

여기서 ``@caller_id``\ 로 표시된 부분은 ``recurse()`` 함수를 호출하는
호출자(caller) 함수의 이름이 들어갈 자리이다. ``inspect`` 패키지를 이용하여
호출자 이름을 받아오는 방법이 있긴 하지만,\ [#caller-name]_ 사용할 수 없을
정도로 느리다. 시간을 재다가 너무 오래 걸려서 그냥 포기했다. 만약
``recurse()``\ 에서 호출자 이름을 빠르게 알아낼 수 있는 방법이 없다면 이 방법은
범용적으로 사용하기는 어려울 것 같다. LeetCode 문제 풀어서 제출하는 정도의
용도로는 별 지장이 없겠지만.

.. code::

    recursive_code
    0.302 ms/pass

    tail_recursive_code
    0.413 ms/pass

    tail_recursion_eliminated_code
    1.441 ms/pass

``try``/``except`` 구문을 제거함으로써 25% 정도의 성능 향상을 도모할 수
있었지만, 충분히 만족스러운 수준은 아니었다. 재귀 호출 코드와 비교하여 여전히
다섯 배 가량 느리다. 게다가 예외 객체를 이용하는 코드와 비교하여 상당히
비직관적인 코드가 되었다는 것을 고려했을 때, 효용 대비 비용이 너무 큰
방법이라는 생각이 들었다.

Take Two: Coroutines
~~~~~~~~~~~~~~~~~~~~

예외 객체 대신 전역 변수를 사용하는 코드로 기대했던 만큼 성능 향상을 걷두지
못했기 때문에 `코루틴 <https://docs.python.org/3/library/asyncio-task.html>`_\
을 이용하는 방법도 생각해보았다. 단순하게 생각해서 재귀 호출 함수를 코루틴으로
만들면 어떤 식으로든 호출자(caller)와 피호출자(callee)가 신호를 주고받을 수
있지 않을까.

StackOverflow의 어떤 답변은 코루틴을 다음과 같이 정의하고 있다.\ [#coroutine]_

    Coroutines are a general control structure whereby flow control is
    cooperatively passed between two different routines without returning.

코루틴에 대한 학술적 정의와는 완벽하게 들어맞지 않을 수도 있지만, 지금 우리가
하고자 하는 작업의 맥락에서 가장 이해하기 쉬운 설명이라는 생각이 들었다. 우리가
필요한 부분은 두 함수가 신호를 주고 받는 장치이고, 코루틴이 그 부분을 해결해줄
수 있을 것 같아서 코루틴을 이용하여 TRE 코드를 작성해보기로 하였다.

.. code:: python

    import asyncio


    async def done(result):
        return False, result, {}


    async def recurse(*args, **kwargs):
        return True, args, kwargs


    async def handler(f, *args, **kwargs):
        while True:
            task = asyncio.ensure_future(f(*args, **kwargs))
            recursion, args, kwargs = await task

            if not recursion:
                return args


    def tail_recursion(f):
        def wrapper(*args, **kwargs):
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(handler(f, *args, **kwargs))
        return wrapper

코루틴을 이용할 경우 원본 코드를 약간 수정해야 한다.

.. code:: python

    @tail_recursion
    def factorial(n, result=1):
        from trlib import done, recurse as factorial
        if n == 0:
            return done(result)
        else:
            return factorial(n - 1, result * n)

재귀 종료 조건을 만족했을 때 위와 같이 ``done()`` 함수를 이용해서 결과값을
전달해야 한다. ``done()`` 함수를 거치지 않고 결과값을 전달하는 방법을 찾지
못했기 때문이다.

.. code::

    recursive_code
    0.303 ms/pass

    tail_recursive_code
    0.418 ms/pass

    tail_recursion_eliminated_code
    19.460 ms/pass

아쉽게도 성능은 훨씬 더 안 좋아졌다. 어쩌면 더 좋은 구조로 개선할 수 있을지도
모른다. 어쨌든 전역변수를 사용하는 코드에 비해서 13배 이상 느리기 때문에
사용하지 않는 것이 좋겠다.


Conclusion
----------
파이썬으로 알고리즘 문제를 풀다가 느낀 불편함으로 인해 한참동안 야크 털을 깎은
것 같은데,\ [#yak-shaving]_ 나름 즐거운 경험이었다. 덕분에 어렴풋이 알고 있던
개념들을 조금 더 확고하게 익힐 수 있었고, 평소에 들여다 볼만한 계기가 없었던
파이썬 바이트 코드도 구경해 볼 수 있었다.

TRE 코드를 통해 사실상 무제한으로 재귀호출을 할 수 있게 되었지만, 아쉽게도
실제로 사용할만한 성능을 끌어내지는 못했다. Dive Deep 섹션에서 제시한 대안
코드를 작성할 때 충분한 고민을 거치지 않아서 구조적인 결함이 있을 수도 있고,
아니면 그보다 더 근본적인 문제가 있을지도 모른다.

성능 문제 이외에도 파이썬에서의 TRE에 대한 비판 의견도 있다.\
[#critiques-on-tre]_ TRE를 도입할 경우 스택 트레이스가 어려워질 뿐만 아니라
재귀 호출이 모든 프로그래밍의 기초가 되어서는 안 된다는 시각이다. 파이썬은 재귀
호출보다는 반복적(iterative) 해결책이 어울리는 언어이다. 나도 한가지 해결책으로
모든 문제를 해결하려는 태도를 지양하는 편이기 때문에 이런 시각에 대체적으로
동의한다.

모든 문제를 재귀적으로 해결할 필요는 없다. 다만, `동적 프로그래밍(dynamic
programming) <https://en.wikipedia.org/wiki/Dynamic_programming>`_\ 과 같은
방법으로 해결한 문제는 `점화식(recurrence relations)
<https://en.wikipedia.org/wiki/Recurrence_relation>`_\ 으로 표현되기 마련이다.
이런 경우에 재귀 호출을 사용한다면 수학식을 그대로 코드로 옮길 수 있기 때문에
편리하다.

만약 다음에 또 이런 주제로 야크 털을 깎을 일이 있다면 파이썬 인터프리터를
개조해서 TRE를 지원하도록 만들어보는 것도 재밌을 것 같다.


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
.. [#caller-name] https://stackoverflow.com/a/2654130
.. [#coroutine] https://stackoverflow.com/a/553745/1913623
