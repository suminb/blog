---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Geeky Stuff
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287065953'
post_id: '600'
published: true
redirect_from:
- /archives/600//
- /post/dynamic-class-loading-in-java
status: publish
tags:
- Java
title: Java 동적 클래스 로드
type: post
---
PHP 에선 다음과 같은 다소 황당한 문법도 통한다.

	$class_name = 'post';
	new $class_name($parameters);

Java 에도 동적으로 클래스를 로드하는 방법이 있다. 역시 뭔가 조금 딱딱한 느낌이다.

	abstract class Person {
		public abstract String toString();
	}

	class Woody extends Person{
		@Override
		public String toString() {
			return "What's up, man.";
		}
	}

	class Haruhi extends Person {
		@Override
		public String toString() {
			return "Sumin-san, ohayougozaimasu!";
		}
	}

	public class ClassTest {
		public static void main(String[] args) throws Exception {
			Class c = Class.forName("Woody");
			Person p = (Person)c.newInstance();
			System.out.println(p);

			System.out.println(Class.forName("Haruhi").newInstance());
		}
	}

결과는

	What's up, man.
	Sumin-san, ohayougozaimasu!

참고로 <a href="http://java.sun.com/javase/6/docs/api/java/lang/Class.html#forName(java.lang.String)">Class.forName(String className)</a> 가 되돌려주는것은 인스턴스가 아니다. 클래스이다. 실제 인스턴스를 얻기 위해서는 <a href="http://java.sun.com/javase/6/docs/api/java/lang/Class.html#newInstance()">newInstance()</a> 메소드를 호출해야 한다.

