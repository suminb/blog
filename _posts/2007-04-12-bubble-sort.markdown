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
  dsq_thread_id: '287066378'
post_id: '598'
published: true
redirect_from:
- /archives/598/
- /post/bubble-sort
status: publish
tags:
- bubble sort
title: Bubble Sort
type: post
---
### Bubble Sort (Ascending Order)

    bubblesort(A)
        N = the number of elements in A
        for(i=0; i<n; i++)
            for(j=0; j<n-(i+1); j++)
                if(A[j] > A[j+1]) swap(A[j], A[j+1])
            end
        end
    end

기본 원리는 아주 간단하다: 뒤쪽부터 올바른 값으로 채워넣는다. Insertion Sort 와 상반되는 방법이라고도 할 수 있다.

    15, 38, 2, 1, -3, -10, 0, 11, -2, 9

이러한 자료를 담고 있는 배열을 정렬한다고 할 때

    15, 2, 1, -3, -10, 0, 11, -2, 9, 38
    2, 1, -3, -10, 0, 11, -2, 9, 15, 38
    1, -3, -10, 0, 2, -2, 9, 11, 15, 38
    -3, -10, 0, 1, -2, 2, 9, 11, 15, 38
    -10, -3, 0, -2, 1, 2, 9, 11, 15, 38
    -10, -3, -2, 0, 1, 2, 9, 11, 15, 38
    -10, -3, -2, 0, 1, 2, 9, 11, 15, 38
    -10, -3, -2, 0, 1, 2, 9, 11, 15, 38
    -10, -3, -2, 0, 1, 2, 9, 11, 15, 38
    -10, -3, -2, 0, 1, 2, 9, 11, 15, 38

이런식으로 동작한다. 여기서 이야기를 멈추면 중학생 수준의 포스트가 되어버리므로 계속 진행하겠다.

### 문제점

    1, 2, 3, 4, 5, 6, 7, 8, 9, 10

위와 같이 이미 정렬되어있는 배열을 정렬하려고 할 경우 똑똑하지 못한 모습을 보여준다. 더이상 정렬할 필요가 없는데도 불구하고 `sig(i, 1, N-1)` 번 실행된다.

### 발전된 형태의 알고리즘

    bubblesort(A)
        flag = N
        while(flag > 0)
            k = flag - 1
            flag = 0
            for(j=0; j<k; j++)
                if(A[j] > A[j+1])
                    swap(A[j], A[j+1])
                    flag = j + 1
                end
            end
        end
    end

이미 정렬 되어있는 배열의 경우 `O(N)` 의 실행시간을 보여준다 (best case). `flag` 가 하는 역할에 주목할 필요가 있다. 이미 정렬된 부분을 표시함으로써 불필요한 연산을 하지 않도록 만들어준다.

각자 좋아하는 언어로 직접 구현해서 코멘트나 트랙백 다는것도 재밌을것 같다 ;-)

