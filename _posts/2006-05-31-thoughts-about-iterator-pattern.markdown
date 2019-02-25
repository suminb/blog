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
  dsq_thread_id: '287065725'
post_id: '306'
published: true
redirect_from:
- /archives/306/
- /post/thoughts-about-iterator-pattern
status: publish
tags:
- design pattern
- iterator
- Java
title: Iterator 패턴에 관한 고찰
type: post
---
# 서론

![weather.png](/wp-content/uploads/2006/05/weather.png)

정말 뜨겁습니다. 그리고 건조합니다.
(사실 글 내용과 전혀 상관 없습니다-_-a)

# LinkedList 탐색

Java 로 프로그래밍을 처음 해보는 초보자에게 [이 문서](http://java.sun.com/j2se/1.5.0/docs/api/java/util/LinkedList.html)를 주면서 LinkedList 의 모든 원소를 출력하는 프로그램을 작성하라는 숙제를 내주면 아마도 다음과 같이 작성할 것입니다.

	LinkedList<integer> list = new LinkedList<integer>();
	list.add(34);
	list.add(72);
	list.add(59);

	for(int i=0; i
<list.size(); i++) {
		System.out.println(list.get(i));
	}

위의 코드는 당장 어떤 문제가 있는 코드는 아닙니다. 문법적 오류도 없으며, 의도한 결과가 나옵니다. 하지만 소프트웨어의 유지보수 측면에서 보면 그다지 깔끔한 구현 방법은 아닙니다. 만약 LinkedList 대신 [Hashtable](http://java.sun.com/j2se/1.5.0/docs/api/java/util/Hashtable.html) 을 사용하라는 요구사항이 생긴다면 어떻게 될까요. 데이터를 삽입하는 부분은 그렇다 치더라도, 데이터를 출력하는 부분의 코드도 모두 바꿔야 합니다. 물론 여기서 예로 든 상황은 약간 억지스러워보일 수도 있고, 심각한 수준의 문제도 아닙니다. 하지만, 소프트웨어를 개발하다보면 이렇게 요구사항에 유연하게 대처하기 힘든 상황이 빈번히 발생합니다.

# Iterator 패턴

[원문](http://www.allapplabs.com/java_design_patterns/iterator_pattern.htm)에 따르면, Iterator 패턴은 내부 구현에 대한 이해 없이 자료의 집합체(List, Stack 등)를 탐색할 수 있도록 해주는 것이라고 합니다.

> The Iterator pattern is one, which allows you to navigate through a collection of data using a common interface without knowing about the underlying implementation.

# Java 에서의 Iterator 패턴

java.util.Collection 인터페이스에는 iterator 메소드가 있습니다.

> `Iterator<e> iterator()`
> Returns an iterator over the elements in this collection. There are no guarantees concerning the order in which the elements are returned (unless this collection is an instance of some class that provides a guarantee).

각 Collection 에서 적당한 Iterator 의 인스턴스를 반환하도록 되어있습니다. 예를 들면, Vector 클래스의 iterator() 메소드는 Vector 를 순차적으로 탐색할 수 있는 Iterator 의 인스턴스를 반환합니다. 그렇게 함으로써

	Iterator i = list.iterator();
	while(i.hasNext()) {
		System.out.println(i.next());
	}

와 같은 코드 작성이 가능한 것입니다. Vector 클래스를 사용하는 개발자는 Vector 클래스의 내부 구현이 어떻게 되어있는지, 어떻게 탐색해야 되는지에 대해서 전혀 알 필요가 없습니다. 오직 Iterator 의 hasNext 와 next 메소드의 사용법만 알면 Vector 클래스 탐색이 가능합니다.

iterator 메소드는 Collection 작성자에 의해서 구현됩니다. 바꿔 말하면, Collection 을 만드는 개발자 마음대로 탐색 방법을 결정할 수 있다는 뜻입니다. 만약 여러분이 [java.util.AbstractList](http://java.sun.com/j2se/1.5.0/docs/api/java/util/AbstractList.html)를 상속받아서 MyVector 라는 클래스를 구현한다고 가정한다면, iterator 메소드를 어떻게 작성하느냐에 따라서 탐색 방법이 달라질 수 있습니다. 역순으로 탐색하는것도 가능하고, Collection 의 <acronym title="element">요소</acronym>를 한칸씩 건너서 탐색하는것도 가능합니다. 다시 한 번 간단히 정리하자면, iterator 의 구현은 구현하는 사람 마음대로입니다.

Iterator 는 실제적 구현체를 갖지 않는 인터페이스이므로, 다음과 같이 Iterator 의 인스턴스를 생성하는것은 불가능합니다.

	Iterator i = new Iterator(); // impossible

각 Collection 에서 적절한 Iterator 를 얻어와야 사용이 가능합니다.

	Vector v = new Vector();
	Iterator i = v.iterator();

이렇게 말입니다.

# Iterator 이용

먼저, 리스트의 내용을 출력하는 간단한 프로그램을 작성해보겠습니다.

	List<string> list = new LinkedList<string>();
	list.add("Windows XP");
	list.add("Gentoo Linux");
	list.add("Solaris 10");

	Iterator<string> i = list.iterator();
	while(i.hasNext()) {
		System.out.println(i.next());
	}

첫번째 예제와 다른점은 for 이 아닌 while loop 과 Iterator 을 사용한다는 것입니다.

	List<string> list = new Vector<string>();
	list.add("Windows XP");
	list.add("Gentoo Linux");
	list.add("Solaris 10");

	Iterator<string> i = list.iterator();
	while(i.hasNext()) {
		System.out.println(i.next());
	}

이번엔 LinkedList 가 아닌 Vector 를 사용했습니다. 하지만 데이터를 출력하는 부분은 똑같습니다.

	HashMap<integer, String> map = new HashMap<integer, String>();
	map.put(1, "Windows XP");
	map.put(2, "Gentoo Linux");
	map.put(3, "Solaris 10");

	Iterator<string> i = map.values().iterator();
	while(i.hasNext()) {
		System.out.println(i.next());
	}

이번엔 HashMap 을 사용했습니다. HashMap 은 위에서 사용했던 LinkedList 나 Vector 과는 다른 종류의 Collection 입니다. HashMap 은 크게 Map 으로 분류되고, LinkedList 와 Vector 는 List 로 분류됩니다. 하지만 위에서 볼 수 있듯이 각 Collection 이 가지고 있는 자료를 출력하는 코드의 모양엔 차이가 없습니다.

# 맺음말

문서가 아직 미완성인듯 합니다-_-a

# 참고 자료

* <http://www.allapplabs.com/java_design_patterns/iterator_pattern.htm>
* <http://java.sun.com/j2se/1.5.0/docs/api/index.html>

