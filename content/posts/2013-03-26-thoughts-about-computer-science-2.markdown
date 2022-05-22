---
categories:
- Computer Science
- 개똥 철학 (Rubbish Philosophy)
meta:
  _edit_last: '1'
  _thumbnail_id: '1829'
  dsq_thread_id: '1166839551'
post_id: '1811'
date: 2013-03-26
published: true
redirect_from:
- /archives/1811/
- /post/thoughts-about-computer-science-2
title: 컴퓨터 과학(Computer Science)에 대한 고찰 2
---
시작하기 전에 만화를 한 편 보자.

<a href="http://comic.naver.com/webtoon/detail.nhn?titleId=335885&no=476&weekday=wed"><img src="http://blog-old.suminb.com/wp-content/uploads/2013/03/gauss-242x480.jpg" alt="가우스전자 473화" width="242" height="480" class="size-medium wp-image-1812" /></a>

그림 속 인물의 표정을 봤을 때 농담조로 얘기하는것 같기는 하지만, 많은 경우에 "***인데 그것도 몰라?" 와 같은 말은 듣는 사람을 불쾌하게 한다.

> A: 숨겨진 파일 보이게 하려면 어떻게 해야 돼요?
> B: 나 윈도우 안 쓴지 오래 돼서 잘 모르겠는데
> A: 컴퓨터 전공이면서 그런것도 몰라요?
> B: (아니 시발 그럼 니가 찾아보던가)

컴퓨터 과학 전공자라면 이러한 상황에 한번쯤은 처해보았을 것이다. 설마 나만 그런건가? 심지어 어떤 경우에는 컴퓨터 과학 전공도 아니고 '컴퓨터 전공자' 혹은 '컴퓨터 하는 사람'이다. 컴퓨터 과학 전공자들이 4년이라는 긴 시간과 비싼 학비를 투자해가면서 윈도우 7 사용법 따위나 배우려고 대학에 온 것은 아닐것이다. '어떻게 퀵 소트를 할줄 모르느냐'와 같은 핀잔을 들으면 적어도 억울하지는 않을것 같다. [선용](https://www.facebook.com/dicebattle)이의 말대로 이런 경우에는 [lmgtfy 링크](http://lmgtfy.com/?q=how+to+show+hidden+files+in+windows+7)를 던져 주는게 정답인것 같다.

오늘은 [지난번 포스팅](http://blog.suminb.com/archives/1600)에 이어서 컴퓨터 과학에 대한 나의 짧은 생각을 늘어놓아보고자 한다.

비전문가들이 생각하는 컴퓨터의 모습
--------

아마도 대부분의 사람들이 '컴퓨터' 하면 떠올리는 이미지는 이런 것이 아닐까 싶다.

<a href="http://www.dell.com/content/topics/topic.aspx/global/shared/windows7/upgrade/index?c=us&amp;l=en&amp;cs=19"><img src="http://blog-old.suminb.com/wp-content/uploads/2013/03/dell-laptops-480x247.jpg" alt="비전문가들이 생각하는 컴퓨터의 모습" width="480" height="247" class="size-medium wp-image-1813" /></a>

분명히 컴퓨터는 맞지만 컴퓨터 과학에서 말하는 컴퓨터와는 조금 거리가 있다.

조금 더 일반적인 컴퓨터의 정의
--------

컴퓨터와 그 관련 기술에 대해 조금 더 관심이 있는 사람들은 다음과 같은 정의를 생각해볼 수 있을 것이다.

> 입력, 출력, 저장, 연산 장치를 가지는 기계

이 정의에 따르면 우리가 일상적으로 사용하는 데스크탑, 랩탑은 물론이고, 컴퓨터가 아니라고 생각하기 쉬운 스마트폰, 태블릿 뿐만 아니라 음료수 자동판매기, 자동차의 [ECU][ECU], [아이팟 셔플][iPod shuffle]과 같은 것들도 컴퓨터의 범주에 들어간다. 예를 들어서 ECU의 입력 장치는 가속 페달, 엔진으로 유입되는 공기중의 산소 농도를 측정하는 센서 정도가 되겠고, 아이팟 셔플의 출력 장치는 오디오 출력 단자 혹은 그 단자에 연결된 음향 장치(이어폰이나 스피커 등)이다. 외부로부터의 입력에 따라서 기계에 어떤 상태(state)가 기록되고, 그 상태에 따라서 내부적 연산 결과가 달라짐에 따라서 출력값이 결정되는 기계를 컴퓨터라고 정의한다고 보면 되겠다.

그럼 사람들이 컴퓨터를 이렇게 이해하고 있으면 컴퓨터 과학이라는 단어가 낳는 여러가지 오해들을 해결할 수 있을까? 안타깝지만 이정도로는 아직 부족하다. 그럼 컴퓨터 과학에서 말하는 컴퓨터란 도대체 무엇일까.

<a href="/wp-content/uploads/2013/03/win7.jpg"><img src="http://blog-old.suminb.com/wp-content/uploads/2013/03/win7.jpg" alt="비전문가들이 생각하는 컴퓨터 책의 전형적인 예" width="280" height="335" class="size-full wp-image-1823" /></a>

컴퓨터의 수학적 정의
--------

<div class="aligncenter">
$$ M= \left \langle Q, \Gamma, b, \Sigma , \delta , q_{0}, F \right \rangle $$
</div>
아, 벌써부터 웹브라우저 창을 닫는 소리가 들린다. 수학 얘기는 되도록 안 할테니 조금만 인내심을 가지고 읽어보자.

위에 쓴 수식은 다름이 아니라 [튜링 기계(Turing machine)][TM]의 정의이다. 자연어로 풀어쓰자면 (확장 가능한) 유한한 길이[^4]의 저장 공간과 유한한 상태(states), 그리고 유한한 기호(symbols)를 가지는 논리적 기계 쯤으로 정의할 수 있겠다.

컴퓨터 과학의 한 분야인 계산 이론(Theory of Computation)에서는 어떤 문제를 컴퓨터로 풀 수 있는지(computability), 또 얼마나 효율적으로 풀 수 있는지(complexity)를 탐구한다.[^1] [^2] 컴퓨터로 풀 수 있는 문제(computable problems)는 바로 이 튜링 기계에 대응시킬(mapping) 수 있는 함수를 의미한다.

컴퓨터 과학 학부 과정에서 다루는 대부분의 내용들은 컴퓨터로 풀 수 있는 문제의 범주에 속하는 것들이다. 이산 수학(discrete math)이라던가 오토마타(automata) 이론, 컴파일러 이론 등은 모두 컴퓨터로 풀 수 있는 문제에 대한 내용이다. 학부 과정에서는 어떤 문제의 복잡도(complexity)에 대한 고민은 많이 하지만, 컴퓨터로 풀 수 없는 문제들에 대해서는 잘 다루지 않는다. 아마도 셀 수 있는 무한한 집합(countably infinite set)이나 재귀 열거 집합(recursively enumerable set)같은 온갖 해괴한 개념들과, 그 개념들을 표현하는데 사용되는 기호들에 익숙해 지려면 많은 시간이 필요하기 때문일 것이다.

컴퓨터 과학
----------

컴퓨터 과학은 이러한 기초적인 컴퓨터 모델에 기초하여 어떤 문제를 해결할 수 있는 일련의 방법을 제시하는 학문이다. 윈도우 7에서 Nvidia 그래픽 카드 드라이버를 설치하는 법이나 하드디스크를 초기화 하는 방법 따위를 가르치는 학문이 아니다. 

<a href="/wp-content/uploads/2013/03/discrete-math.jpg"><img src="http://blog-old.suminb.com/wp-content/uploads/2013/03/discrete-math-480x290.jpg" alt="초보적인 수준의 컴퓨터 과학 책" width="480" height="290" class="size-medium wp-image-1815" /></a>

[구글 지도](http://maps.google.com)에 출발지와 목적지를 입력하면 어떻게 최단 경로를 계산하는지 의문을 가져본 적이 있는가? 아니면 3차원 물체를 어떻게 평면인 스크린에 입체적으로 보이도록 투영(projection)하는지 알고 있는가? 그것도 아니면 [아마존](http://www.amazon.com)이 어떻게 여러분이 구입 할만한 물건들을 골라서 추천 상품 목록을 보여주는지 궁금한가? 이 모든 것이 컴퓨터 과학을 응용한 기술들이다. 그래프 이론(graph theory), 컴퓨터 그래픽(computer graphics), 머신 러닝(machine learning)은 모두 컴퓨터 과학의 한 분야로서 우리 생활 깊숙히 스며들어있다.

컴퓨터 과학의 하위 범주에 속하는 주제들은 이것보다 훨씬 많지만, 그 내용이 너무 방대하므로 이 글에서는 다루지 않도록 하겠다. 지적 호기심이 발동하는 사람은 위키피디아에서 [컴퓨터 과학](http://en.wikipedia.org/wiki/Computer_science) 주제를 읽어보면 좋을것 같다.[^3]

마무리
-----

사람들은 의외로 굉장히 무지(無知)하다. 세상에는 복잡한 것들 투성이인데 인간의 집중력은 한정되어있으니 어찌 보면 당연한 일인지도 모른다. 나도 이런 무지함에서 자유롭지 못한건 마찬가지다. 물리학적 소양이 부족해서 여러가지 문건을 찾아봐도 힉스(Higgs) 입자가 무엇인지 심도 있게 이해하기에는 역부족이다. 어떤 입자가 힉스 입자로 구성된 공간(fabric)을 통과할 때 힉스 입자와 반응(interact)을 하는 정도가 다른데, 광자(photon)와 같이 힉스 입자와 전혀 반응하지 않는 입자들은 빛의 속도로 그 공간을 통과할 수 있고, 반응을 하는 입자들은 반응 정도에 따라서 그 입자의 질량이 달라진다 -- 정도로 어렴풋이 이해할 수 있을 뿐이다. 대부분의 사람들이 자신의 일이나 관심 분야 이외의 것들에는 무지할 수 밖에 없지 않을까 하는게 내 생각이다.

사람들은 컴퓨터가 무엇인지, 컴퓨터 과학이 무엇인지에 대해서 잘 알지 못하고 알려고 하지도 않는다. 심지어는 운영체제, 웹 브라우저, 인터넷 처럼 서로 다른 개념들을 구분하지 않고 섞어서(interchangeably) 사용하는 사람들도 여럿 봤다. 컴퓨터 과학에 대한 오해는 전공자와 비전공자의 서로 다른 컴퓨터에 대한 이해의 간극이 낳은 결과가 아닐까 한다.

[TM]: http://ko.wikipedia.org/wiki/%ED%8A%9C%EB%A7%81_%EA%B8%B0%EA%B3%84
[ECU]: http://en.wikipedia.org/wiki/Engine_control_unit
[iPod shuffle]: http://www.apple.com/ipod-shuffle/

[^1]: Multiple Authors. "[Theory of Computation](http://en.wikipedia.org/wiki/Theory_of_computation)." *Wikipedia*. Wikimedia Foundation, 25 Mar. 2013. Web. 26 Mar. 2013.
[^2]: 사실 이 수업 때문에 머리가 돌아버릴 지경이다.
[^3]: 한국어판은 내용이 부실해서 부득이하게 영문판을 링크했다.
[^4]: 경계가 없다는 것(unbounded)은 무한하다는 것(infinite)과는 구분되는 개념이다. 참고로 제한이 있는(bounded) 저장 공간을 가지는 튜링 기계를 Linear Bounded Automata (LBA)라고 한다.

