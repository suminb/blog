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
  dsq_thread_id: '287065567'
post_id: '552'
published: true
redirect_from:
- /archives/552/
- /post/changing-order-of-operators
status: publish
tags: []
title: Binary Tree 탐색을 이용한 연산자 표기 순서 변경
type: post
---
오랜만에 블로그 제목에 어울리는 포스트를 하나 올리겠다.

## Tree

<img id="image551" src="http://blog.suminb.com/wp-content/uploads/2007/02/tree.png" alt="tree.png" />

여기 잘 만들어진 나무가 있다. Visio 를 이용해서 그렸다-_-v 중위 표기법으로 표현된 수식을 이러한 형식으로 변환하는 과정은 생략하겠다 :P

왜냐고 물으면 딱히 할 말이 없다. 그냥 귀찮아서? 이게 정답인것 같다. 괄호로 완벽하게 묶인(fully-parenthesized) 식이라면 몰라도 실세계에서 흔히 접하는 수식은 경우에 따라서 해석하기 난해할 수도 있다. 예를 들면 `-8 / -1/2(2 + 4)(-3 + 1)` 이런거...

## 연산자 후위 표기 (Postfix)

	postfix(tree)
		if(tree is null) return

		postfix(tree.left)
		postfix(tree.right)
		print(tree.value)

의사 코드(pseudo code)이다. 이걸 보고 어떤 프로그래밍 언어냐고 묻는 사람은 없을거라고 믿는다.

	1 2 + 3 4 - * 5 6 + *

연산자 후위 표기와 전위 표기의 주된 장점중 하나는 괄호 없이 연산자 우선순위를 명시할 수 있다는 것이다. 예를 들어서, `a + b * c` 와 같은 식의 연산자 우선순위를 바꾸려면 `(a + b) * c` 와 같이 괄호를 써줘야 한다. 하지만 후위 표기법으로 나타내면 전자는 `a b c * +`, 후자는 `a b + c *` 와 같이 나타낼 수 있다.

고등학생때 간단한 사칙연산 해석기(parser)를 만들었었는데, 그때도 후위 표기법을 사용했던걸로 기억한다. 중위 표기법으로 표현된 수식을 해석해서 후위 표기법으로 바꿔 스택에 넣으면 아주 간단하게 수식의 결과를 얻을 수 있다.

## 연산자 전위 표기 (Prefix)

	prefix(tree)
		if(tree is null) return

		print(tree.value)
		postfix(tree.left)
		postfix(tree.right)

<strike>전위 표기법은 실제로 사용해본적이 없는것 같다.</strike>

	* * + 1 2 - 3 4 + 5 6

## 연산자 중위 표기 (Infix)

대부분의 사람들한테 친숙한 표기법이다. 정규 교과 과정에 수학 과목이 포함되어있고, 정규 교과 과정에서 다루는 수학에서는 중위 표기법을 쓰니까.

	infix(tree)
		if(tree is null) return

		infix(tree.left)
		print(tree.value)
		infix(tree.right)

이렇게 하면 될까?

	1 + 2 * 3 - 4 * 5 + 6

대충 모양이 나오는것 같지만, 연산자 우선순위가 엉망이 되어버렸다. 연산자 중위 표기를 위해서는 약간의 추가적인 작업을 해줘야 한다.

	infix(tree)
		if(tree is null) return
		if(tree.value is an operator) print("(")

		infix(tree.left)
		print(tree.value)
		infix(tree.right)

		if(tree.value is an operator) print(")")

결과는?

	(((1 + 2) * (3 - 4)) * (5 + 6))

괄호 덕분에 연산자 우선순위가 바로잡혔다.

## 마무리

고등학생때(아마 2학년때였을 거다) 이러한 내용들을 알게 되었을때 뭔가 커다란 깨달음을 얻은것 같은 느낌이었다. 중3때 C언어 처음 만져봤을때처럼. 그때부터 이쪽으로 계속 연구했었다면 지금쯤 컴파일러 하나쯤 개발했을지도 모르겠다. 아하하...

1. 괄호 없이 연산자 우선순위 평가
1. 생략된 연산자 인식 (`5(b + c) = 5 * (b + c)`)
1. 단일 연산자 구분 (`a + -b`)
1. 할당 연산자 (`=`)

이정도만 구현해도 꽤 괜찮은 수식 해석기를 만들 수 있을거라고 생각한다. 관심 있는 사람은 한번 도전해보길 바란다.

