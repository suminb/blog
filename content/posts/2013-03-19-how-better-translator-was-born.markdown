---
categories:
- Geeky Stuff
meta:
  _edit_last: '1'
  _thumbnail_id: '1793'
  dsq_thread_id: '1149052872'
post_id: '1792'
date: 2013-03-19
published: true
redirect_from:
- /archives/1792/
- /post/how-better-translator-was-born
tags:
- Google
- Google Translate
- Naver
- Reddit
title: 더 나은 번역기 탄생 비화(祕話)
---
2013년 2월 어느 평화로운 토요일 오후. 하라는 숙제는 안 하고 방구석에서 빈둥빈둥 하던 대학원생 B군은 페이스북에서 재미있는 스크린샷을 발견하게 된다. 구글 번역기를 이용해서 한국어를 영어로 번역할 때, 직접 번역하는것 보다는 일본어를 거쳐서 번역하면 더 좋은 결과물이 나온다는 내용이었다.

예를 들면,

> 여러분이 몰랐던 구글 번역기

와 같은 문장을 영어로 바로 번역 하면

> You did not know Google translator

와 같은 다소 엉뚱한 결과가 나오는 반면, 일본어로 먼저 번역을 하고

> 皆さんが知らなかったGoogle翻訳

이것을 다시 영어로 번역하면

> Google translation that you did not know

처럼 조금 더 정확한 번역이 된다는 것이다. B군은 '오 이런게 있었군' 하면서 신기해 했지만 그때까지만 해도 별 생각이 없었다.

며칠 후 B군은 또 페이스북 뉴스피드를 뒤적거리다가 유능한 넥슨 게임 개발자인 [이흥섭](http://subl.ee)군의 친구분께서 내놓으신 흥미로운 제안을 발견했다.

<a href="http://blog-old.suminb.com/wp-content/uploads/2013/03/sublees-friend.png"><img src="http://blog-old.suminb.com/wp-content/uploads/2013/03/sublees-friend-480x149.png" alt="흥섭이 친구분의 솔깃한 제안" width="480" height="149" class="size-medium wp-image-1795" /></a>

한국어-일본어-영어 번역 과정을 자동화 할 수 있지 않겠느냐는 친구의 말에 이흥섭은 짧고 간결한 답변을 남겼다.

> 할 수 있겠지 ㅋㅋ

기술적으로 크게 어려울 것도 없을것 같고, 나름 흥미로운 주말 프로젝트가 될 수 있을것 같다고 B군은 생각했다.

그로부터 며칠이 지난 시점, 컴퓨터 그래픽 수업에서 다루는 OpenGL과 선형대수 때문에 고통받던 B군은 고통에서 잠시 벗어나기 위해서 딴짓거리를 하게 된다. 며칠 전에 생각했던 아이디어의 프로토타입을 만들어보기로 한 것이다. 당연히 구글에서 제공하는 구글 번역기 [API](http://ko.wikipedia.org/wiki/API)가 있겠거니 하고 안일하게 생각했던 B군은 잠시 후 충격적인 사실을 깨달았다. 대부분의 구글 서비스들은 일정 한도 내에서 무료로 쓸 수 있는 API를 제공하지만, 구글 번역기 API는 무료 할당량이 아예 없고 번역 100만 문자당 $20을 지불해야 한다는 것이었다.[^1]

B군은 그 비용을 감당할 자신이 없었다. 그렇다고 이렇게 쉽게 포기하기엔 뭔가 아쉬웠다. B군은 일단 구글 번역기 웹사이트가 어떻게 동작하는지 하나하나 분석해 나가기 시작했다. 소스코드가 공개되어있지 않고, 공개적으로 문서화되지 않은 서비스라 통찰력과 경험에서 우러난 추측에 전적으로 의존하는 방법 밖에는 없었다. 서비스의 오용(abuse)을 방지하기 위한 여러가지 장치도 있었다. 하지만 데이터를 훔치는게 주 특기인 B군에게는 큰 문제가 되지 않았다. 이 글에서는 기술적인 내용을 자세히 다루지 않겠지만, 기회가 된다면 다음에 따로 시간을 내어서 다뤄보는 것도 괜찮을것 같다.

구글 번역기 서비스가 어떻게 동작하는지 대략적으로 파악한 B군은 그 과정에서 알아낸 사실들을 문서로 남겨놓았다. 그 관성을 이어받아 프로토타입 구현까지 할 수도 있었지만 B군은 프로토타입을 만드는 일은 잠시 미루기로 했다. 저녁 시간이 다 되었기 때문이었다.

또 며칠이 지난 일요일 밤. B군은 침대에 누워서 잠을 청했지만 베개에 머리를 대는 순간 잠들던 평소 모습과는 다르게 꽤 오랜 시간동안 잠들지 않고 누워있었다. 일어난지 열두시간도 안 됐는데 다시 잠을 청하려니 쉽게 잠들지 못하는 것은 어찌 보면 당연한 일인지도 모르겠다. 그러다가 문득 며칠 전에 만들어 놓았던 구글 번역기 해킹 문서가 뇌리를 스쳤다. "아, 그거나 만들어볼까" 하면서 B군은 침대에서 일어나 책상에 앉았다. [깃헙 커밋 로그](https://github.com/suminb/translator/commits/master)에서도 볼 수 있듯이 B군은 그날 새벽 동이 트기 직전까지 [더 나은 번역기][Translator][^2]의 기본적인 기능들을 구현하고 나서 비로소 잠자리에 들었다.

해가 중천에 뜬 시간에 다시 일어난 B군은 놀라운 사실을 발견하게 된다. 페이스북에 링크만 하나 달랑 던져놨을 뿐인데 예상보다 훨씬 반응이 좋았던 것이다. 결국 서비스를 공개한지 열일곱시간 만에 600회가 넘는 페이지뷰와 106개의 페이스북 '좋아요'를 받게 됐다.

사람들로부터의 뜻밖의 관심에 흥이 난 B군은 여러가지 기능을 추가하기 시작했다. [홍민희](http://dahlia.kr)군과 같은 유명 인사들의 이름을 예문에 넣는가 하면, [정유진](http://flyingyujin.x-y.net)양의 도움을 받아 프랑스어 서비스도 준비했다. 스페인어 서비스 준비는 B군의 오랜 친구인 Leon Garcia군이 도와주었다.

B군의 취미이고 특기이자 3대 삶의 낙 중의 하나가 바로 자랑질이다. 3월 17일, 4개국어로 서비스를 시작했다고 페이스북에 - 그것도 전체 공개 설정으로 - 자랑해놨는데, 그걸 발견하신 [박신조](https://github.com/peremen)님께서 [러시아어 번역][GitHub-Russian]을 해주셨다. 정말 고마운 일이다. B군은 도움을 주신 모든 분들의 노고를 세상에 알리고자 [만든 사람들](http://translator.suminb.com/credits) 페이지도 만들었다.

그 후 [더 나은 번역기][Translator]는 트위터, [블로그 글][blog], [카라 팬 페이지][Karaboard], [레딧(Reddit)][Reddit], [네이버 카페][Naver-cafe] 등 여러곳에 언급되면서 전 세계로 뻗어나가기 시작했다.

<a href="http://blog-old.suminb.com/wp-content/uploads/2013/03/worldwide-impact.png"><img src="http://blog-old.suminb.com/wp-content/uploads/2013/03/worldwide-impact-480x271.png" alt="전 세계로 뻗어 나가는 더 나은 번역기" width="480" height="271" class="size-medium wp-image-1793" /></a>

B군은 당분간 새로운 기능 추가 대신 여러가지 [알려진 문제점들](https://github.com/suminb/translator/issues)을 해결하고 서비스의 질을 개선하는데 주력할 계획이다.

또한 B군의 방돌이[^3]들 중 한명인 김성중군이 더 나은 번역기의 안드로이드 버전을 준비중이다. 모양새를 갖추는대로 안드로이드 마켓에 공개할 계획이다.

하지만 [더 나은 번역기][Translator]는 근본적인 문제점을 가지고 있다. 구글에서 정식으로 허가하지 않은 방법으로 구글 번역기를 이용하는 서비스인만큼 구글에서 어떤 형식으로든 제재를 하게 되면 서비스를 중단해야 할 수도 있다.

[^1]: 자세한 정보는 [구글 번역기 API 가격 정책 페이지](https://developers.google.com/translate/v2/pricing)를 참고.
[^2]: 처음에 사용한 이름은 '더 나은 한영 번역기'였다. 처음에는 한국어-영어 번역 기능밖에 없었기 때문이다.
[^3]: 룸메이트

[blog]: http://fischer.egloos.com/4786122
[Karaboard]: http://karaboard.com/bbs/board.php?bo_table=community&wr_id=715518
[Reddit]: http://www.reddit.com/r/Korean/comments/1akf04/tip_if_youre_using_google_translation_for_engkor/
[Naver-cafe]: http://cafe.naver.com/malltail.cafe?iframe_url=/ArticleRead.nhn%3Fclubid=21820768%26page=1%26menuid=68%26boardtype=L%26articleid=1145359%26referrerAllArticles=false
[GitHub-Russian]: https://github.com/suminb/translator/commit/c4c0f0633b174eb608d94fdb7dfc75925d3726e2
[Translator]: http://better-translator.com

