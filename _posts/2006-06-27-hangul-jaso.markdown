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
  _wp_old_slug: '%ed%95%9c%ea%b8%80-%ec%9e%90%ec%86%8c-%eb%b6%84%eb%a6%ac-%eb%98%a0%eb%b0%a9%ea%b0%81%ed%95%98%eb%a5%bc-%e3%84%b8%e3%85%97%e3%85%81%e3%85%82%e3%85%8f%e3%85%87%e3%84%b1%e3%85%8f%e3%84%b1%e3%85%8e%e3%85'
  dsq_thread_id: '287066518'
post_id: '353'
published: true
redirect_from:
- /archives/353/
- /post/hangul-jaso
status: publish
tags:
- Java
- 한글
title: 한글 자소 분리
type: post
---
[link1]: http://mwultong.blogspot.com/2006/03/perl.html "[Perl/펄] 한글 자소 분리: '똠방각하'를 'ㄸㅗㅁㅂㅏㅇㄱㅏㄱㅎㅏ'로 자동 변환"

[레몬향기혜성](http://mwultong.blogspot.com)님이 쓴 [포스트][link1]를 보고 Java 로 conversion 해봤다.

학교 도서관 컴퓨터로 프로그래밍 하는 일은 그다지 유쾌한 일이 아니다. 개발도구가 설치되어있지 않음은 물론이고 Administrator Privilege 도 없어서 소프트웨어를 마음대로 설치할 수 없다. 그래도 다행인것은 Eclipse는 설치하지 않고 실행이 가능하다는 점과, Mac 에서는 Netbeans 도 설치하지 않고 실행할 수 있다는 점이다.

아무튼, 이 클래스는 도서관에 있는 Power Mac 으로 힘들게;; 작성했다. 인코딩은 UTF-8 으로 설정해야 된다.

    /*
     * Jaso.java
     *
     * Created on June 27, 2006, 3:12 PM
     *
     * To change this template, choose Tools | Template Manager
     * and open the template in the editor.
     */

    import java.util.Vector;

    /**
     *
     */
    public class Jaso {

        public static char[] ChoSeong = { 0x3131, 0x3132, 0x3134, 0x3137, 0x3138,
                0x3139, 0x3141, 0x3142, 0x3143, 0x3145, 0x3146, 0x3147, 0x3148,
                0x3149, 0x314a, 0x314b, 0x314c, 0x314d, 0x314e };
        public static char[] JungSeong = { 0x314f, 0x3150, 0x3151, 0x3152, 0x3153,
                0x3154, 0x3155, 0x3156, 0x3157, 0x3158, 0x3159, 0x315a, 0x315b,
                0x315c, 0x315d, 0x315e, 0x315f, 0x3160, 0x3161, 0x3162, 0x3163 };
        public static char[] JongSeong = { 0x0000, 0x3131, 0x3132, 0x3133, 0x3134,
                0x3135, 0x3136, 0x3137, 0x3139, 0x313a, 0x313b, 0x313c, 0x313d,
                0x313e, 0x313f, 0x3140, 0x3141, 0x3142, 0x3144, 0x3145, 0x3146,
                0x3147, 0x3148, 0x314a, 0x314b, 0x314c, 0x314d, 0x314e };

        /**
         * @param args the command line arguments
         */
        public static void main(String[] args) {
            try {
                char[] chars = "대한민주주의공화국".toCharArray();
                Vector<character> v = new Vector<character>();

                for (int i = 0; i < chars.length; i++) {
                    if (chars[i] >= 0xAC00 && chars[i] <= 0xD7A3) {
                        int i1, i2, i3;

                        i3 = chars[i] - 0xAC00;
                        i1 = i3 / (21 * 28);
                        i3 = i3 % (21 * 28);
                        i2 = i3 / 28;
                        i3 = i3 % 28;

                        v.add(ChoSeong[i1]);
                        v.add(JungSeong[i2]);
                        if (i3 != 0x0000)
                            v.add(JongSeong[i3]);
                    }
                    else {
                        v.add(chars[i]);
                    }
                }

                System.out.println(v);
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }

    }

결과는 다음과 같다.

    [ㄷ, ㅐ, ㅎ, ㅏ, ㄴ, ㅁ, ㅣ, ㄴ, ㅈ, ㅜ, ㅈ, ㅜ, ㅇ, ㅢ, ㄱ, ㅗ, ㅇ, ㅎ, ㅘ, ㄱ, ㅜ, ㄱ]

