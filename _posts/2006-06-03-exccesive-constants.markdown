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
  dsq_thread_id: '287065542'
post_id: '310'
published: true
redirect_from:
- /archives/310/
- /post/exccesive-constants
status: publish
tags:
- Java
title: Exccesive Constants
type: post
---
서론
----

Java 에서는 final 키워드가 붙은 변수가 어떻게 처리될까요. 이것에 관련된 간단한 실험을 한가지 해보겠습니다.

# Justin 의 identification

Justin 의 나이, 신원, 지역을 저장해놓은 클래스입니다.

	import java.util.Locale;

	public class Justin {
		public final static int age = 18;
		public final static String identification = "I'm Justin";
		public final static Locale locale = new Locale("en-US");
	}

Justin 클래스의 각 상수들을 출력하는 클래스입니다.

	public class Test {
		public static void main(String[] args) {
			System.out.println(Justin.age);
			System.out.println(Justin.identification);
			System.out.println(Justin.locale);
		}
	}

실행 결과는 당연히

	18
	I'm Justin
	en-us

입니다. 자, 그럼 이제 Justin 클래스를 약간 수정해보겠습니다.

	public class Justin {
		public final static int age = 21;
		public final static String identification = "I'm not Justin";
		public final static Locale locale = new Locale("ko-KR");
	}

Justin 클래스는 컴파일 하고, Test 클래스는 다시 컴파일하지 않고 그대로 실행합니다. 실행 결과는

	18
	I'm Justin
	ko-kr

입니다. locale 의 값은 의도한대로 바뀌었지만, 나머지 값들은 그대로입니다. 어찌된 일일까요.

결론
----

위 실험 결과를 토대로 다음과 같은 결론을 도출해낼 수 있습니다. __"final 키워드가 붙은 primitive 와 String 형식의 변수는 컴파일타임에 해당 클래스에서 <acronym title="hard coding 된">상수</acronym>로 치환된다"__ 다른 말로 해서,

	public class Test {
		public static void main(String[] args) {
			System.out.println(Justin.age);
			System.out.println(Justin.identification);
			System.out.println(Justin.locale);
		}
	}

이 코드는

	public class Test {
		public static void main(String[] args) {
			System.out.println(18);
			System.out.println("I'm Justin");
			System.out.println(Justin.locale);
		}
	}

와 똑같은 효과를 가집니다. Justin 클래스의 변경사항을 Test 클래스에 반영시키려면 Test 클래스를 다시 컴파일해야 합니다.

