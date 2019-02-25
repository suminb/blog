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
  dsq_thread_id: '287064900'
post_id: '1230'
published: true
redirect_from:
- /archives/1230/
- /post/hanja-hanguel-translator
status: publish
tags:
- Python
- 한글
- 한자
title: 한자-한글 변환
type: post
---
[한자-한글 변환기][link] (<http://hanja.suminb.com>)

오랜만의 한국어 포스팅이다.

나는 어렸을 때 한자 공부를 열심히 하지 않아서 그런지, [이런](http://www.hanja-edu.com/bbs/view.php?id=magazine_article&no=368) 글을 보면 무언가 거부감이 든다. 한자와 한글의 병용을 주장하는 글을 한자 혼용으로 작성해놓은 이유는 무엇인가.

본문에 따르자면 한자를 배워야 하는 이유를 다음의 몇가지로 요약할 수 있다.

1. 성명의 한자 표기를 통해 자기의 근본을 알고 자기 정체성을 확립한다.
2. 어휘력을 풍부하게 한다.
3. 단어의 뜻을 명확하게 알 수 있다.

먼저, 자기의 성과 이름을 한자로 쓸 줄 알고 자기의 근본을 알고 자기정체성을 확립하는 것과 일상 생활에서 한자를 병용하는것은 별 관계가 없어보인다. 또, 흔한 경우는 아니지만, 한글 전용으로 인해 특정 단어의 의미가 명확하지 않은 경우가 있을수도 있는데, 이런 경우에 한해서만 괄호 안에 대응되는 한자를 넣어주는 한자 병용으로 문제를 해결할 수 있다. 대부분의 경우에 한글 전용으로도 의미가 확실히 전달되는데에도 불구하고 굳이 한자를 쓰는것은 대단한 자원의 낭비라고 생각된다.

본문 중에 다음과 같은 내용이 있다.

> 例를 들어 여기 흔히 쓰이는 정신 나간 사람이라고 할 때 ‘井神, 定身, 廷臣, 精神, 挺身, 正信, 貞臣, 淨神, 正身, 情神, 鼎臣’ 등이 있는데 이 중 어느 정신인지 漢字를 모르면 구분이 잘 안 된다.

주장하고자 하는 바가 무엇인지 대략 짐작이 가지만, 예를 조금 잘못 선택한것 같다. 위의 문맥에서 쓰인 '정신'이 어떤 뜻의 정신인지 모르면 정말로 정신 나간 사람이 아닐까 한다.

이것 이외에도 적절하지 않은 뒷받침 내용이나, 출처나 사실 여부를 알 수 없는 서술문, 논리적 오류가 보이지만, 이 글을 쓰는 목적이 위의 글을 비판하기 위함이 아니므로 본론으로 넘어가도록 하겠다.

오늘 이 글을 쓰는 목적은 [한자-한글 변환기][link]를 공개하는 것이다. 이것 덕분에 위의 한자 혼용 글도 읽고 이해할 수 있었다.

일단, 약 3만개의 한자-한글 매핑 데이터를 [여기](http://kore.wikia.com/wiki/사용자:Masoris/hani_converter.js)서 얻어왔다. 이것을 파이썬의 사전(dictionary) 형식으로 표현하고, 변환할 문자열에서 한 글자씩 한자에서 한글로 변환하는 방식이다. 핵심 기능을 하는 코드는 다음의 한 줄이 전부이고, 나머지는 사용자의 입력을 받고 결과물을 보여주기 위한 코드이다.

~~~
map(lambda x: x in dict and dict[x] or x, post['query'])
~~~

`map` 함수가 어떤 기능을 하는 것인지 모르겠으면 [이 문서](http://docs.python.org/library/functions.html#map)를 읽어보길 바란다. `map`, `reduce`, `filter` 과 같은 [higher-order function](http://en.wikipedia.org/wiki/Higher-order_function) 들을 잘 쓰면 프로그램을 간결하면서도 효과적으로 작성할 수 있다.

[link]: http://hanja.suminb.com

