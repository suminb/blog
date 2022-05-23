---
categories:
  - General
layout: post
meta:
  disqus_identifier: 29543f83c99531881795377465fc56d45cfcfb6b
date: 2014-05-15
published: true
redirect_from:
  - /post/goodbye-wordpress-hello-jekyll
tags:
  - korean
title: WordPress 에서 Jekyll 로
---

지금으로부터 약 10년전인 2004년부터 설치형 [WordPress][]를 사용해서 개인 블로그를 운영하고 있었는데, 이번에 [Jekyll][]을 사용해서 블로그를 만들어보기로 했다. Jekyll은 HTML이나 Markdown 등의 서식으로 작성된 문서들로 정적 웹사이트를 생성해주는 도구다. WordPress 대신 Jekyll을 선택한 이유는

* 나는 블로그 포스트를 작성할 때 WP에서 제공하는 에디터 대신 텍스트 편집기를 이용해서 Markdown 형식으로 작성한다. 글 작성이 끝나면 WP의 편집기로 복사 & 붙여넣기 하기 때문에 Jekyll을 사용한다면 이 과정을 생략할 수 있다.
* 2011년에 정체 불명의 공격자들이 PHP로 작성된 파일 업로더의 취약점을 이용해서 `.htaccess` 파일을 조작하고 백도어를 심어놓는 등 심각한 수준의 공격을 감행한 적이 있다.
  * 정적 웹사이트의 취약점을 찾아서 공격하는 것은 동적인 웹 애플리케이션을 공격하는 것보다 상대적으로 어려운 일이다.
  * WP의 아이디/패스워드 사용자 인증보다는 [two-factor authentication][]으로 보호 받는 GitHub 계정과 SSH 공개키 기반의 사용자 인증이 더 안전하지 않을까.
* [스포카][]에서 일 하면서 나의 Git 사용 능력이 비약적으로 향상됐다. 따라서 블로그 글을 관리하는데 Git을 사용한다고 해도 부담이 없다.
* [GitHub Pages][]에서 무료로 정적 페이지 호스팅을 제공한다.
* <div><s>WordPress 는 PHP로 작성되었다.</s> (농담)</div>


Jekyll 설치
----------

먼저, Jekyll을 설치하자.

    gem install jekyll

그 다음, Jekyll 디렉토리를 생성하면 된다.

    jekyll new blog

`blog` 디렉토리로 이동하여 다음의 명령어를 실행하면 `http://localhost:4000` 에서 생성된 웹사이트를 볼 수 있다.

    jekyll serve


WordPress 포스트 내보내기
---------------------

WP의 관리자 인터페이스에서 블로그의 내용을 `.xml` 파일로 내보내기 할 수 있다. 자세한 내용은 [이 페이지](http://en.support.wordpress.com/export/)를 참조.


WordPress 포스트 변환하기
---------------------

이제 블로그 포스트를 Jekyll이 이해할 수 있는 형식으로 바꿔야 한다.

Jekyll의 불러오기 도구를 설치하자. WP뿐만 아니라 Tumblr, Joomla, Google Reader, Drupal 을 비롯해서 RSS와 `.csv` 형식도 지원한다. 지원되는 임포터(importer) 목록을 보고 싶으면 [이 페이지](https://github.com/jekyll/jekyll-import/tree/master/lib/jekyll-import/importers)를 보면 된다.

    gem install jekyll-import

사실 일반적인 경우라면 이렇게 설치하는 것으로 끝이지만, 나의 경우에는 잠시 후에 설명할 포스트 리다이렉트(redirect)를 하기 위해서 WP 포스트의 `post_id` 값을 같이 내보내야 했다. 그래서 jekyll-import 프로그램의 소스코드를 약간 수정하기로 했다.

`jekyll-import/importers/wordpressdotcom.rb` 파일을 보면 다음과 같이 포스트의 정보를 얻어오는 부분이 있다.

    date = Time.parse(item.at('wp:post_date').inner_text)
    status = item.at('wp:status').inner_text

밑에 한 줄 추가해줬다.

    post_id = item.at('wp:post_id').inner_text

좀 더 밑으로 내려가면 다음과 같이 [YAML front-matter][] 부분을 채워주기 위한 코드가 있다.

    header = {
      'layout' => type,
      'title'  => title,
      'categories' => categories,
      'tags'   => tags,
      'status'   => status,
      'type'   => type,
      'published' => published,
      'meta'   => metas,
      'author' => authors[author_login]
    }

여기에 `post_id` 를 추가해줬다.

    header = {
      ...
      'post_id' => post_id,
      ...
    }

이제 jekyll-import 프로그램을 실행시킬 차례이다.

[메뉴얼](https://github.com/jekyll/jekyll-import/blob/master/README.markdown)에는 `jekyll import wordpress --source wordpress.xml` 와 같이 해도 된다고 나와있는데, 나는 `Invalid command. Use --help for more information` 이런 에러 메세지가 나왔다. 다행히도 [Jekyll 문서](http://import.jekyllrb.com/docs/wordpressdotcom/)에는 제대로 된 사용법이 소개 되어 있었다.

    ruby -rubygems -e 'require "jekyll-import";
        JekyllImport::Importers::WordpressDotCom.run({
          "source" => "wordpress.xml"
        })'

`_posts` 디렉토리에 `yyyy-mm-dd-title.html` 형식의 파일들이 생성된 것을 볼 수 있을 것이다.


포스트 다듬기
----------

사실 지금 이 상태에서 그대로 올려도 괜찮지만, 나는 깔끔한 블로그를 원하기 때문에 조금 더 공을 들였다. 할 일은 다음과 같다.

* 불필요한 HTML 태그 없애기 (`<p>`, `<br/>` 등)
* 예전 포스트 리다이렉트(redirect)
* 파일 확장자를 `.html` 에서 `.markdown` 으로 변경

300개가 넘는 포스트를 일일이 수작업으로 다듬을 수는 없으니 [간단한 스크립트][convert.py]를 만들어서 해결했다.


예전 포스트 리다이렉트
-----------------

WP에서 쓰던 퍼머링크(permalink)는 `/archieves/${post_id}` 형식이었지만, 새 블로그에서 쓸 퍼머링크는 `/post/${title}` 형식이다. 사실, 퍼머링크 형식을 그대로 유지할 수도 있었지만, [적절한 키워드를 포함하는 퍼머링크가 SEO에 도움이 될 수도 있다](http://code.tutsplus.com/articles/wordpress-permalinks-101-what-how-when-and-why-to-use-them--wp-22652)는 내용을 담은 글을 보고, 대대적인 블로그 데이터 변환 작업을 하는 김에 퍼머링크 형식도 바꾸기로 했다.

예전 퍼머링크 형식으로 접속한 사용자들을 새 링크로 보내줘야 하는데, [jekyll-redirect-form][] 플러그인의 도움을 받으면 비교적 수월하게 해결할 수 있다. 플러그인을 설치하고 `_config.yml` 에 다음과 같은 내용을 추가해줘야 한다.

    gems:
      - jekyll-redirect-from

[포스트 변환 스크립트][convert.py]에 의해서 포스트의 [YAML front-matter][] 부분에 다음과 같이 `redirect_from` 항목이 들어가게 된다. WP 포스트를 변환할 때 `post_id` 값을 저장하도록 한 이유가 바로 이것이다.

    redirect_from:
      - /archives/1234/


Pagination
----------

모든 글이 한 페이지에 나열되어 있으면 너무 길어지니까 여러 페이지에 나누는 작업도 필요하다. [Jekyll의 공식 문서](http://jekyllrb.com/docs/pagination/)를 참고해서 만들었다. 사실 참고했다기보다는 거의 복사 & 붙여넣기 했다. `index.html` 파일에 포스트 보여지는 부분 아래쪽에 다음과 같은 코드를 붙여준다.

    {% raw %}
    <!-- Pagination links -->
    {% if paginator.total_pages > 1 %}
    <div class="pagination">
    {% if paginator.previous_page %}
      <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&laquo; Prev</a>
    {% else %}
      <span>&laquo; Prev</span>
    {% endif %}

    {% for page in (1..paginator.total_pages) %}
      {% if page == paginator.page %}
        <em>{{ page }}</em>
      {% elsif page == 1 %}
        <a href="{{ '/index.html' | prepend: site.baseurl | replace: '//', '/' }}">{{ page }}</a>
      {% else %}
        <a href="{{ site.paginate_path | prepend: site.baseurl | replace: '//', '/' | replace: ':num', page }}">{{ page }}</a>
      {% endif %}
    {% endfor %}

    {% if paginator.next_page %}
      <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Next &raquo;</a>
    {% else %}
      <span>Next &raquo;</span>
    {% endif %}
    </div>
    {% endif %}
    {% endraw %}


MathJax 설치
-----------

수식이 들어간 포스트가 많아서 LaTeX를 랜더링 할 수 있는 MathJax도 필요하다. `_layouts/default.html` 파일의 아래쪽에 다음과 같이 MathJax 자바스크립트 파일을 포함하도록 하는 코드를 넣었다.

    <script type="text/javascript"
       src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

이렇게 하면 `$$ f(x) = x + 1 $$`와 같이 두 개의 달러 사인 (`$$`) 사이에 들어간 LaTeX 표현이 랜더링 된다. MathJax 얘기가 나온 김에 제대로 작동 되는지 테스트 해보자.

$$ f(n) = \begin{cases} n/2 &\text{if } n \equiv 0 \pmod{2}\\ 3n+1 & \text{if } n\equiv 1 \pmod{2} .\end{cases} $$


Google Analytics 설치
--------------------

먼저, `_config.yml` 파일에 다음과 같이 Google Analytics 프로필 아이디를 넣었다.

    google_analytics_id: UA-xxxxxx-x

이렇게 추가된 설정값은 템플릿 언어를 이용하여 `{{ "{{ site.google_analytics_id" }} }}`와 같이 참조할 수 있다. 그 다음, 아래와 같은 내용을 담은 `_includes/analytics.html` 파일을 만들었다.

    {% raw %}
    {% if site.google_analytics_id %}
      <!-- Google Analytics (http://google.com/analytics) -->
      <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', '{{ site.google_analytics_id }}']);
        _gaq.push(['_setDomainName', '{{ site.url }}']); // Multiple sub-domains
        _gaq.push(['_setAllowLinker', true]); // Multiple TLDs
        _gaq.push(['_trackPageview']);
        (function() {
          var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
          ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
      </script>
    {% endif %}
    {% endraw %}

위의 코드 조각은 [jekyll-import의 코드](https://github.com/jekyll/jekyll-import/blob/master/site/_includes/analytics.html)에서 가져온 것이다. 그리고 나서 `_layouts/default.html` 파일의 아래쪽에 `analytics.html` 파일을 포함하도록 만들었다.

    {% raw %}
    {% include analytics.html %}
    {% endraw %}


Disqus 댓글 플러그인 설치
---------------------

포스트 페이지의 레이아웃을 정의하는 `_layouts/post.html` 파일을 수정하면 된다. `disqus_identifier` 값을 지정해주면 페이지의 URL과 관계 없이 예전에 쓰던 댓글 페이지를 그대로 불러올 수 있다고 공식 문서에 나와있지만[^disqus_identifier], 작동이 되지 않는것 같다. 이 문제를 해결할때 까지는 당분간 댓글을 닫아놔야 할 것 같다.

    {% raw %}
    {% if site.disqus %}
    <div id="disqus_thread"></div>
    <script type="text/javascript">
      var disqus_shortname = 'blog-suminb-com';
      {% if page.meta.dsq_thread_id %}
      var disqus_identifier = '{{ page.meta.dsq_thread_id }}';
      {% endif %}

      /* * * DON'T EDIT BELOW THIS LINE * * */
      (function() {
          var dsq = document.createElement('script');
          dsq.type = 'text/javascript'; dsq.async = true;
          dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
          (document.getElementsByTagName('head')[0]
            || document.getElementsByTagName('body')[0]).appendChild(dsq);
      })();
    </script>
    <noscript>Please enable JavaScript to view the
        <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a>
    </noscript>
    <a href="http://disqus.com" class="dsq-brlink">comments powered by
        <span class="logo-disqus">Disqus</span></a>
    {% endif %}
    {% endraw %}

`disqus_identifier` 문제가 해결되지 않는다면 예전 댓글 페이지들을 새 주소로 마이그레이션 해야 되는데[^disqus_migration], 이것도 나름 귀찮은 일이 될 것 같으니 웬만하면 `disqus_identifier`를 이용해서 해결할 계획이다.


검색창 달기
--------

정적 웹사이트인만큼 자체적으로 검색 기능을 제공하는 일이 쉽지 않다. 그래서 검색 기능은 구글에게 위탁하기로 했다. [Google Custom Search Engine][] 서비스를 이용하면 간편하게 특정 사이트 내에서만 검색 되는 검색창을 만들 수 있다.


앞으로 할 일
---------

꽤 많은 작업을 했지만, 아직 할 일이 더 남았다.

1. <div><strike>페이스북 라이브, 트윗 버튼 설치</strike> (완료)</div>
1. 첨부 파일 마이그레이션
1. 스타일시트 수정 (혹은 새로 만들기) - 지금은 일단 Jekyll의 기본 디자인을 쓰고 있지만, 천천히 바꿔 나갈 생각이다.
1. <div><strike>도메인 CNAME 수정 - 지금까지는 내 서버에서 운영했지만, 앞으로는 GitHub Pages에서 운영할 계획이다.</strike> (완료)</div>
1. 포스트 리다이렉션 할 때 `<meta>` 태그 대신 HTTP 302 메세지 내보내기
1. 모바일 페이지 지원


마무리
----

처음에 생각했던 것과는 다르게 굉장히 거창하고 장대한 작업이 되었다. 겉으로 보기엔 간단한 일이라도 실제로 해보면 일의 복잡도가 처음 예상보다 훨씬 높고 숨어있는 문제들이 많다는걸 다시 한 번 깨닫게 됐다.

그리고 구글 애드센스 광고는 더이상 달지 않기로 했다. 어차피 유의미한 수익이 나올만큼 많은 방문자를 보유한 것도 아닌데 블로그의 미관을 해치는 광고를 넣는 일이 부질없다고 생각했다.


[스포카]: http://spoqa.com
[GitHub Pages]: https://pages.github.com
[WordPress]: http://wordpress.org
[Jekyll]: http://jekyllrb.com
[Google Custom Search Engine]: https://www.google.com/cse/
[two-factor authentication]: http://en.wikipedia.org/wiki/Two-step_verification
[jekyll-redirect-form]: https://github.com/jekyll/jekyll-redirect-from
[YAML front-matter]: http://jekyllrb.com/docs/frontmatter/
[convert.py]: https://github.com/suminb/suminb.github.io/blob/master/_posts/convert.py

[^disqus_identifier]: <http://help.disqus.com/customer/portal/articles/472098-javascript-configuration-variables#disqus_identifier>
[^disqus_migration]: <http://help.disqus.com/customer/portal/articles/286778-migration-tools>