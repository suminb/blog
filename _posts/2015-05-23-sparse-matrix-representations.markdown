---
author:
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
categories:
- Computer Science
layout: post
meta: null
published: true
redirect_from:
- /post/sparse-matrix-representations
tags:
- math
- sparse matrix
title: Sparse Matrix Representations
---

[올해 NDC 에서 OpenCL 과 행렬 연산의 응용을 주제로 발표](http://www.slideshare.net/suminb/durango-opencl)를 했는데, 발표 후 질문 답변 시간에 나왔던 질문중 하나가

> Compressed sparse row (CSR) 이외에 sparse matrix 를 효율적으로 표현할 수 있는 자료구조가 있나요?

였다. 답변을 잘 하고 싶은 좋은 질문이었다. 분명히 발표자료 만들면서 찾아봤던 것은 기억이 나는데, 마이크를 잡고 있어서 그런지 그 자료구조들의 이름조차 기억이 나지 않아서 "지금은 기억이 나지 않는다"는 답변밖에 할 수 없었다. 현장에서 답변을 할 수 있었으면 좋았겠지만, 그렇게 하지 못했으니 아쉬운대로 이 자리를 빌어 제대로 된 답변을 내놓고자 한다.

일단 이 글에서 공통적으로 사용되는 행렬은 다음과 같다.

$$
\mathbf{A} = \begin{bmatrix}
    0 & 0 & 4 & 0 & 0  \\
    0 & 8 & 2 & 0 & 0  \\
    0 & 7 & 4 & 0 & 3  \\
    0 & 0 & 0 & 0 & 0  \\
    0 & 0 & 0 & 0 & 5  \\
\end{bmatrix}
$$

Dictionary of Keys (DOK)
---
말 그대로 행렬을 사전(dictionary)에 저장한다. 이때 0이 아닌 원소의 좌표가 키(key)가 되고, 그 원소가 값(value)이 된다. 파이썬 오브젝트로 표현하면 다음과 같다.

    {
        (0, 2): 4,
        (1, 1): 8,
        (1, 2): 2,
        (2, 1): 7,
        (2, 2): 4,
        (2, 4): 3,
        (4, 4): 5
    }

### 장점
* 이해하기 쉬움<sup>[나의 주관적 견해]</sup>
* 원소의 추가와 삭제, 색인이 빠르다. $O(1)$

### 단점
* 다른 자료구조로 변환하는 것 이외에는 딱히 유용하지 않다.

Coordinate List (COO)
---
DOK와 비슷하지만, 사전이 아닌 `(행, 열, 값)` 튜플(tuple)로 행렬을 표현한다.

파이썬 오브젝트로 표현하면 대략 이런 모습이다.

    [
        [0, 2, 4],
        [1, 1, 8],
        [1, 2, 2],
        [2, 1, 7],
        [2, 2, 4],
        [2, 4, 3],
        [4, 4, 5]
    ]

### 장점
* 원소의 추가가 빠르다. $O(1)$

### 단점
* 색인은 그다지 빠르지 않을 수 있다. $O(n)$
* DOK 와 마찬가지로 다른 자료구조로 변환하는 것 이외에는 딱히 유용하지 않다.

List of Lists (LIL)
---

[위키피디아의 표현](https://en.wikipedia.org/wiki/Sparse_matrix)을 빌리자면,

> LIL stores one list per row, with each entry containing the column index and the value. Typically, these entries are kept sorted by column index for faster lookup. This is another format good for incremental matrix construction.

이 설명을 토대로 구성을 해보면 대략 이런 모습이 될 것 같다.

    [
        [2, 4],
        [1, 8, 2, 2],
        [1, 7, 2, 4, 4, 3],
        [],
        [4, 5]
    ]

반면, [Lund University 의 자료](http://www.maths.lth.se/na/courses/FMNN25/media/material/sparse_lecture.pdf)에 의하면,

> Store two lists: one containing lists of column indices for each row and one containing lists of corresponding values

이와 같이 약간 다른 설명이 나온다. 이 설명에 따르면 다음과 같은 모습이 나오지 않을까 한다.

    [
        [[2], [1, 2], [1, 2, 4], [], [4]],
        [[4], [8, 2], [7, 4, 3], [], [5]]
    ]

### 장점
* 원소 하나를 수정하는 것은 COO 방식만큼 효율적이다.
* 행렬을 자르는 것이 쉽다. 특히 행별로 자르는 것.
* COO, DOK 방식과 비교하여 빠른 행렬-벡터 곱셈이 가능하다.

### 단점
* 더 나은 방식과 비교했을 때에는 행렬-벡터 곱셈이 더 느릴 수 있다.
* 느린 연산(arithmetic operations).
* 데이터가 메모리상에 연속적으로 존재하지 않아서 캐시 적중률이 낮아질 수 있다.

Compressed Sparse Row
---

이 방식이 바로 발표 자료에서 다루었던 방식이다.

<iframe src="//www.slideshare.net/slideshow/embed_code/key/wIG0hCSCROKQBb?startSlide=128" width="630" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> 

파이썬 오브젝트로 나타내면,

    row_offsets =    [0, 1, 3, 6, 7]
    column_indices = [2, 1, 2, 1, 2, 4, 4]
    values =         [4, 8, 2, 7, 4, 3, 5]

### 장점
* 빠른 행렬-벡터 곱셈.
* 빠른 연산.
* 행 기준으로 자르기 쉽다.

### 단점

* 열 기준으로 자르기 어렵다.
* 원소의 추가와 삭제가 어렵다.

Compressed Sparse Column
---

CSR 과 똑같은 방식이다. 단지 행(row)을 기준으로 자르는 것이 아니라 열(column)을 기준으로 잘라서 표현하는 것일 뿐. 행렬의 전치행렬(transpose)을 구해서 CSR 형식으로 표현하면 원래 행렬의 CSC 형식이 될 것이다.<sup>[정말 그렇게 되는지 직접 확인해보지는 않았음]</sup>

    column_offsets = [0, 2, 5, 7]
    row_indices =    [1, 2, 0, 1, 2, 2, 4]
    values =         [8, 7, 4, 2, 4, 3, 5]

### 장점

* 빠른 행렬-벡터 곱셈.
* 빠른 연산.
* 열 기준으로 자르기 쉽다.

### 단점

* 행 기준으로 자르기 어렵다.
* 원소의 추가와 삭제가 어렵다.

그 이외의 자료구조들
---
이 글에서 언급한 자료구조 이외에도 [Yale Sparse Matrix Package](http://cpsc.yale.edu/sites/default/files/files/tr112.pdf) 등 몇가지 자료구조들이 더 있는것 같지만 이 글에서는 다루지 않을 것이다.