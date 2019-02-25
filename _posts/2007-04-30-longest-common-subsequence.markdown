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
  dsq_thread_id: '287066168'
post_id: '614'
published: true
redirect_from:
- /archives/614/
- /post/longest-common-subsequence
status: publish
tags: []
title: LCS(Longest Common Subsequence) 찾기
type: post
---
오... 완전 신기>_ <

	LCS(X, Y)
		for(i=1; i<=m; i++) L[i, 0] = 0
		for(j=0; j<=n; j++) L[0, j] = 0
		for(i=1; i<=m; i++)
			for(j=1; j<=n; j++)
				if(x[i] == y[j])
					L[i, j] = 1 + L[i-1, j-1]
				else if(L[i-1, j] >= L[i, j-1])
					L[i, j] = L[i-1, j]
				else
					L[i, j] = L[i, j-1]

