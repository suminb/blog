---
layout: post
title: 이상한 호주 여행기 - 비용 정산
categories:
- Travel
- Mathematics
tags:
- australia
- dynamic programming
- python
published: true
draft: false
meta:
author:
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
---

사건의 개요
---
NOTE: 여행중 남긴 기록들을 토대로 열심히 여행기를 작성하고 있는데, 사실 이 글이 여행기의 마지막편이다. 마지막편을 가장 먼저 공개하게 되어서 유감이지만 완성도가 낮은 글을 공개하기는 곤란하다고 판단했다. 지금 나의 친구들과 동료들이 열심히 리뷰해주고 있으니, 리뷰 코멘트를 반영해서 완성되는대로 한편씩 차례대로 공개할 생각이다.

회사의 든든한 지원을 등에 업고 즐거운 여행을 다녀온것 까지는 좋았으나, 복잡한 비용 정산 문제가 남아있었다.

부연 설명을 하나 덧붙이자면, 1인당 주어진 GEP 예산은 300만원이었다. 이것으로 항공권, 현지 교통비, 숙박, 식사 등 여행에 필요한 전반적인 비용들을 해결할 수 있다. 주어진 예산만 가지고도 여행을 하는데 부족함이 없었겠지만, 개인 돈을 조금 보태서 쓴 덕분에 훨씬 풍요로운 생활을 누릴 수 있었다.

GEP 예산 지원을 받기 위해서는 여행중에 사용한 비용을 법인카드로 결제 하고 그 내역을 상신하면 된다. 비용은 한달 단위로 정산한다. 9월 말에 사용한 비용은 여행중에 회사 인트라넷에 접속해서 직접 상신했고, 호주팀 사람들과 공동으로 사용한 비용은 공용 법인카드로 처리하고 담당자분께서 대신 결재를 올려주셨다. 이제 10월 초에 사용한 비용만 정산하면 된다.

9월에 사용한 비용과 호주팀 사람들과 공동으로 사용한 비용을 제외하고 나에게 남은 예산은 약 90만원 정도였다. 이 글에서는 자세히 설명하지 않을 여러가지 복잡한 사정에 의해 그 예산의 일부는 우리 팀원이 사용한 결제 내역을 처리하는데 사용하고, 그분이 그 비용을 나한테 현금으로 보내주셨다. 아직 결재를 올리지 못한 법인카드 사용 내역은 29건, 총 1,324,996원이었다. 이중에 GEP 예산으로 처리할 수 있는 비용이 903,910원, 내 개인 돈으로 해결해야 할 돈이 421,086원이었다. 우리 팀원이 나한테 보내준 돈이 590,943원이었으니 내가 결재를 올릴 수 있는 금액은 정확히 312,967원이었다. 다시 말해서 그 29건의 거래 내역 중 적당한 내역들을 골라서 최대한 312,967원에 가깝게, 하지만 그 금액을 넘기지는 않게 조합해서 결재를 올리면 되는 아주 간단한(?) 문제였다.

### 아직 결재를 올리지 못한 내역들

전체 거래 내역을 일일이 들여다보지 않아도 포스트의 내용을 이해하는데 전혀 지장이 없긴 하지만, 궁금증이 많은 독자들을 위해서 전체 내역을 기록해두었다.

|  사용 내역  |  금액(KRW)  |
|-----------|-----------:|
| AYR TRAVEL CENTRE AYR AUS |  16,199 |
| HJ MACKAY MACKAY AUS    |  10,906 |
| HJ ROSS RIVER TOWNSVILLE AUS    |  3,382 |
| TRAVEL RESERVATION AU SYDNEY AUS    |  84,725 |
| TRAVEL RESERVATION KOR PARIS FRA    |  71,294 |
| JIMMYS BURGER & CO CAIRNS AUS   |  36,372 |
| AROI BANGKOK THAI RE HERMIT PARK AUS    |  21,256 |
| WW PETROL 2268 HERMIT PAR AUS   |  18,555 |
| MATILDA MARYBOROUGH SINNAMON PARK AUS   |  21,636 |
| COLES EXPRESS 1764 MACKAY AUS   |  19,425 |
| CALTEX BOYNE RIVER BENARABY AUS |  18,688 |
| SUBWAY MACKAY - NEBO WEST MACKAY AUS    |  10,482 |
| Lillys Bistro 5277108 GIN GIN AUS   |  7,613 |
| COLES 4564 BRISBANE AUS |  74,453 |
| AIRBNB * AIRBNB.COM GBR |  58,176 |
| Sydney Opera House Tru Sydney AUS   |  50,942 |
| SECURE PARKING ASTOR T SPRING HILL AUS  |  26,950 |
| 7-ELEVEN 4174 GAVEN AUS |  26,582 |
| HAKATAYA RAMEN BR SBANE AUS |  9,589 |
| KFC NO 2 PORT MACQRIE PORT MACQUARI AUS |  9,520 |
| AIRBNB * AIRBNB.COM GBR |  210,198 |
| JAMIES ITALIAN BY JA SYDNEY AUS |  50,818 |
| 7-ELEVEN 2240 LAMBTON AUS   |  36,992 |
| FRIENDLY GROCER PYRM PYRMONT AUS    |  17,732 |
| NOMONIE PTY LTD WICKHAM AUS |  16,953 |
| UBER AU OCT05 CRMVT HELP.UBER.C AUS |  9,971 |
| COLES EXPRESS 1698 ULTIMO AUS   |  8,031 |
| TRANSPORT FOR NSW SYDNEY AUS    |  5,247 |
| HERTZ AUSTRALIA P/L |  372,309 |

렌터카(372,309원)는 이미 최대치를 넘겼으니 올리지 말고, 그 다음으로 큰 금액인 에어비앤비(210,198원) 내역을 올리면 10만원 정도가 남으니까 10만원 이하 결제 내역 중에서 다음으로 큰게 뭐였더라... 아니지, [그리디 알고리즘(greedy algorithm)](https://en.wikipedia.org/wiki/Greedy_algorithm)으로는 전역적 최적해(global optimum)를 찾지 못할 가능성이 높다. 생각이 여기까지 미치자 프로그래머의 고질병인 [야크 털 깎기](https://www.lesstif.com/pages/viewpage.action?pageId=29590364)가 발현되었다.

문제 해결
---
가만있자, 이거 어디선가 많이 본 문제인데? 컴퓨터공학을 전공한 사람이라면 내가 무슨 얘기를 할 것인지 벌써 눈치 챘을 것이라고 생각한다. 그렇다. 최적화 문제의 일종인 배낭 문제와 매우 흡사하다.

### 배낭 문제 (Knapsack Problem)

배낭 문제란, 일정 가치와 무게가 있는 짐들을 배낭에 넣을 때, 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제이다.[^1] 예를 들어서, 다음과 같은 물건들이 있을 때 최대 5kg 한도 내에서 배낭 안에 들어가는 물건들의 가치가 최대가 되는 조합을 찾는 상황을 가정해보자.

| 가격($) | 무게(kg) |
|-------:|--------:|
|  4 | 12 |
|  2 |  2 |
|  2 |  1 |
|  1 |  1 |
| 10 |  4 |

`(가격, 무게)` 순서쌍으로 표현했을 때 답은 $$\{(2, 1), (10, 4)\}$$가 될 것이다. 두 물건의 무게의 합은 5kg이고, 가격의 합은 \$12이다. 이것보다 더 높은 가격의 합을 만들기 위해서는 5kg을 초과할 수 밖에 없기 때문에 이 조합이 최적해이다. 문제를 수학식으로 표현하자면 다음과 같다.

$$
\text{maximize } \sum_{i=1}^n v_i x_i \\
\text{subject to } \sum_{i=1}^n w_i x_i \leq W \text{ and } x_i \in \{0,1\}
$$

여기서 $v$는 가격을 의미하고, $w$는 무게를, $x$는 해당 물건의 포함 유무를, 마지막으로 $W$는 최대 무게를 의미한다.

### 변형된 배낭 문제

전통적인 배낭 문제에서는 물건들의 무게의 합을 일정 값 이하로 유지하면서 가격의 합을 최대화 하는 것이 목표였다면, 내가 해결하고자 하는 문제에서는 무게라는 개념은 빠져있고 정해진 최대치 내에서 가격의 합을 최대화 하는 문제이다.

수학식으로는 다음과 같이 표현할 수 있다.

$$
\underset{v \in X}{\operatorname{arg\,max}}
\sum v \text{ subject to } \sum v \leq W
$$

우리의 배낭 $X$는 다음과 같이 정의할 수 있다.

$$
X = \{v_1, v_2, \cdots, v_n\}
$$

물론 배낭은 비유적인 표현일 뿐이다. $X$는 아직까지 결재를 올리지 않은 법인카드 사용 내역들의 집합이고, $v_i$는 각각의 거래당 결제 금액이다.

그리고, $m[i, v]$를 $i$번째까지의 결제 내역의 일부 또는 전부를 합쳐서 만들 수 있는 $v$ 이하의 최대 금액으로 정의하자. 조금 더 격식을 차려 표현하자면 다음과 같다.

$$
m[i, v] = \left\{
  \begin{array}{ll}
    0 & \text{ if } i = 0 \text{ (empty) } \\
    m[i-1, v] & \text{ if } v_i > v \\
    \max \left\{
      \begin{array}{l}
        m[i-1, v] \\
        m[i-1, v - v_i] + v_i
      \end{array}
    \right. & \text{otherwise}
  \end{array}
\right.
$$

### 파이썬 코드로 최적의 해 구하기

식까지 세웠으니 코드로 옮기는 것은 그다지 어려운 일이 아니다. 재귀호출을 이용하여 다음과 같이 아주 간단하게 구현할 수 있다. 함수 호출에 필요한 시스템 스택은 크기가 제한되어있기 때문에 $n$이 클 경우 이 방법은 적합하지 않을 수도 있지만, 29개의 거래 내역을 가지고 문제를 푸는데 딱히 걱정해야 할만한 사항은 아니라서 그냥 편한 방법으로 구현하기로 했다.
  
    def m(i, limit, values):
        if i < 0:
            return 0
        else:
            curr = values[i]
            if curr > limit:
                return m(i - 1, limit, values)
            else:
                left = m(i - 1, limit, values)
                right = m(i - 1, limit - curr, values) + curr
        
                return right if right > left else left

수학식에서는 $v_1$이 첫번째 거래 내역의 금액을 의미하는 표기였지만, 파이썬 코드에서는 `v[0]`이 리스트의 첫번째 원소가 된다. 따라서 물건을 하나도 사용하지 않고 만들 수 있는 최대 금액인 $m[0, v]$는 `m[-1, V]`로 표현된다.

다음과 같이 거래 금액을 리스트로 만들고

    values = [
        16199, 10906, 3382, 84725, 71294, 36372, 21256, 18555, 21636, 19425, 18688,
        10482, 7613, 74453, 58176, 50942, 26950, 26582, 9589, 9520, 210198, 50818,
        36992, 17732, 16953, 9971, 8031, 5247, 372309]

조금 전에 정의했던 `m()` 함수를 이용해서 최적해를 구할 수 있다.
  
    v = m(len(values) - 1, 312967, values)

하지만 `m()`은 각 거래 금액의 합산으로 예산 범위 내에서 만들 수 있는 최대값만 구할 뿐, 어떤 내역을 취했고, 어떤 내역을 버렸는지는 알 수 없다.

### 어떤 거래 내역을 취했는지 알아내기

조금 전에 세웠던 식을 다시 리뷰해보자.

$$
\max \left\{
  \begin{array}{l}
    m[i-1, v] & \text{(1)} \\
    m[i-1, v - v_i] + v_i & \text{(2)}
  \end{array}
\right.
$$

`(1)`은 현재 내역을 버리는 것, `(2)`는 현재 내역을 취하는 경우이다. `(2)`를 선택할 경우에 이것을 기록해두는 작업이 필요하다. 아까 작성했던 `m()` 함수를 조금 고쳐봤다. 차이점이 있다면 `(2)`의 경우가 나올때마다 `(i, limit)`을 기록해놓는다는 것이고, 이것을 위해 `taken`이라는 인자가 추가됐다는 점이다.

    def m(i, limit, values, taken):
        if i < 0:
            return 0
        else:
            curr = values[i]
            if curr > limit:
                return m(i - 1, limit, values, taken)
            else:
                left = m(i - 1, limit, values, taken)
                right = m(i - 1, limit - curr, values) + curr
        
                if right > left:
                    taken[(i, limit)] = 1
                    return right
                else:
                    return left

코드에서 볼 수 있듯이 `m()` 함수는 여전히 `values`의 원소들을 조합하여 `limit` 안에서 만들 수 있는 최대값을 반환한다. 어떤 원소들을 택했는지 알아내려면 `taken`을 역추적해봐야 한다.

    def track_solutions(n, limit, values, taken):
        k = limit
        for i in range(n, -1, -1):
            if (i, k) in taken:
                yield i
                k -= values[i]

이렇게 최종 결과로부터 하나씩 거슬러 올라가면서 추적할 수 있다.

### 중간 계산 결과 저장하기

처음 코드를 작성할 때에는 원소 여섯개짜리 샘플 데이터 셋을 가지고 테스트 하면서 작업했었는데, 29개의 레코드를 다 넣으니 CPU 사용량이 100%로 올라간 상태가 꽤 오래 지속되었다. 그럴만도 한 것이, 위의 배낭 문제에서 하위 문제(subproblem)의 계산 결과값을 처음부터 다시 계산할 경우 알고리즘의 시간복잡도는 지수 함수(exponential function)인 $O(2^n)$가 된다.[^2] 여기서 $n$은 리스트 원소의 개수인데, 원소의 수가 적을 때는 다항 함수(polynomial function)의 시간복잡도를 가지는 알고리즘과 비교하여 실제 수행 시간상의 의미 있는 차이를 발견하기 어렵지만, 원소의 개수가 많아질수록 급격하게 헬게이트가 펼쳐진다.

그렇지만 우리가 배낭 문제를 푸는데 사용한 [동적 계획법(dynamic programming)](https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EA%B3%84%ED%9A%8D%EB%B2%95)이라는 기법의 아름다움은 이미 풀었던 하위 문제를 다시 풀 필요가 없다는 것이다. 하위 문제를 풀때마다 그 결과를 저장해놓고 그 다음 문제에서 그걸 이용하면 계산 시간을 획기적으로 줄일 수 있다.

    def m(i, limit, values, taken, cache):
        if i < 0:
            return 0
        else:
            curr = values[i]
            key = (i, limit)

            try:
                return cache[key]
            except KeyError:
                pass

            if curr > limit:
                value = m(i - 1, limit, values, taken, cache)
            else:
                left = m(i - 1, limit, values, taken, cache)
                right = m(i - 1, limit - curr, values, taken, cache) + curr

                if right > left:
                    taken[key] = 1
                    value = right
                else:
                    value = left

            cache[key] = value
            return value

이렇게 해서 1분 27초쯤 걸리던 작업이

    ➜  time python knapsack.py 
    ...
    python knapsack.py  87.26s user 1.86s system 96% cpu 1:32.39 total

18초 미만으로 줄어들었다.

    ➜  time python knapsack.py 
    ...
    python knapsack.py  17.56s user 0.65s system 96% cpu 18.898 total

이것보다 더 빠르게 만들 수도 있겠지만, 파이썬의 생산성 덕분에 아낄 수 있었던 내 시간을 고려해서 너그럽게 봐주도록 하자.

전체 소스코드는 [Gist에 공개](https://gist.github.com/suminb/e9b255dc1afdf3b586a43ce2a28e960a)해놓았다.

마무리
---

나의 프로그램은 아래와 같이 아름다운 결과를 도출해냈고,

    ➜  python knapsack.py 
    Sum of taken values = 312967
    Taken records = [9520, 58176, 74453, 7613, 18688, 19425, 21636, 21256, 71294, 10906]

프로그램에 찾아준 최적해에 따라 1원 단위까지 딱 맞춰서 비용정산을 마칠 수 있었다.


[^1]: 이 부분은 [위키피디아의 '배낭 문제' 항목 한국어판](https://ko.wikipedia.org/wiki/%EB%B0%B0%EB%82%AD_%EB%AC%B8%EC%A0%9C)을 인용했다.
[^2]: 그런 일이 일어날 가능성은 희박하지만, 시간적 여유가 된다면 어떤 과정을 통해 이런 결론을 도출했는지 간략하게 설명해봐도 좋을 것 같다.
