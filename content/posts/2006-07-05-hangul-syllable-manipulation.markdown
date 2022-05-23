---
categories:
- Software Engineering
meta:
  _edit_last: '1'
  dsq_thread_id: '287065203'
post_id: '375'
date: 2006-07-05
published: true
redirect_from:
  - /archives/375/
  - /post/hangul-syllable-manipulation
status: publish
tags:
  - Java
  - 한글
title: 한글 음절(syllable) 다루기
---
# 서론

음절은 하나 또는 그 이상의 말소리로 이루어져 독자적으로 발음되는 가장 작은 단위이다. 또 다른 말로는 '소리마디', 영어로는 syllable 이라고 한다. 한글의 음절은 초성, 중성, 종성으로 이루어진다. 초성과 중성은 반드시 있어야 하지만 종성은 없어도 음절을 구성하는데 지장이 없다. 더 자세히 들어가면 나의 국문학적 무지가 탄로날지도 모르니 서론은 여기서 그만 하도록 하겠다.

# 본론

간단하게 음절을 다루는 클래스, Syllable 을 작성하기로 했다. 내부적으로 초성, 중성, 종성을 분리하여 저장하고 있으며, 몇 가지 편리한 메소드를 제공한다.

Syllable 클래스를 작성하기 시작한지 얼마 지나지 않아서 문제에 봉착하게 되었다. 키보드에서 'ㄱ' 을 눌러서 타이핑된 글자의 코드는 `0x3131` 이지만, unicode specifications 에 나와있는 초성의 'ㄱ'은 `0x1100`, 종성의 'ㄱ'은 `0x11A8` 이다. 이 문제를 해결하기 위해 외부적으로는 `0x3131` 과 `0x1100` 이 모두 허용되도록 하고, 내부적으로는 specifications 에 나와있는 코드를 쓰기로 결정했다.

음절을 만드는 방법은 다음의 3가지가 있다.

#### 방법 1

빈 음절 인스턴스를 만든 후, 초성, 중성, 종성을 따로 집어넣는다.

	Syllable s1 = new Syllable();
	s1.setChoSeong('ㅂ');
	s1.setJungSeong('ㅡ');
	s1.setJongSeong('ㄹ');

#### 방법 2

방법 1과 비슷하다. 단지 생성자가 그 일을 대신할 뿐이다.

	Syllable s2 = new Syllable('ㄹ', 'ㅗ');

#### 방법 3

마지막으로, 생성자에 완전한 음절을 집어넣는 방법이 있다.

	Syllable s3 = new Syllable('그');

#### 예제

	System.out.print(s1);
	System.out.print(s2);
	System.out.print(s3);

실행 결과는

	블로그

전체 코드를 공개하면 좋겠지만, 안타깝게도 Syllable 클래스의 소스코드는 당분간 공개하지 않기로 결정했다. 대신, 프로토타입 정도는 공개한다.

	public class Syllable {

		private char choSeong;
		private char jungSeong;
		private char jongSeong;

		public Syllable();
		public Syllable(char syllable);
		public Syllable(char choSeong, char jungSeong);
		public Syllable(char choSeong, char jungSeong, char jongSeong);

		public void setChoSeong(char choSeong);
		public char getChoSeong();
		public void setJungSeong(char jungSeong);
		public char getJungSeong();
		public void setJongSeong(char jongSeong);
		public char getJongSeong();

		public String toString();

		public static boolean isSyllable(char character);
		public static char[] split(char syllable);
		public static char build(char choSeong, char jungSeong, char jongSeong);
	}

# 참고 자료

* [유니코드 (구원의 여신 등장?)](http://web.edunet4u.net/~han0416/%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4%20%EA%B0%95%EC%A2%8C/chapter2/uni_code2_iso.htm)
* <http://en.wikipedia.org/wiki/Hangul>
* <http://www.unicode.org/charts/PDF/U1100.pdf>
* <http://www.unicode.org/charts/PDF/UAC00.pdf>

