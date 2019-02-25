---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Mathematics
- 생활 코딩 (Casual Coding)
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287065528'
post_id: '425'
published: true
redirect_from:
- /archives/425/
- /post/delegating-math-homework-to-computer
status: publish
tags: []
title: 수학 숙제는 컴퓨터에게
type: post
---
> Consider the differential equation
>
> dy/dx = sin(xy), with initial condition y(1) = 1
>
> Estimate y(2), using Euler's method with step sizes dx = 0.2, 0.1, 0.05.

이런 문제 나오면 난감한거다. 내 친구 이거 하는데 한시간 걸렸댄다 ㅋㅋㅋ
이럴 때 고성능 계산기-_-를 잘 쓰면 인생이 편해진다.

	double x = 1.0;
	double y = 1.0;
	double dx = 0.05;

	int n = (int) (x / dx);
	for (int i = 0; i <= n; i++) {
	    double slope = Math.sin(x * y);
	    double dy = slope * dx;
	    y += dy;

	    System.out.printf("(%.2f, %.3f) slope=%.3f dy=%.3f y=%.3f\n", x, y
		    - dy, slope, dy, y);

	    x += dx;
	}

살포시 실행시키면 다음과 같은 아름다운 결과를 얻을 수 있다.

	(1.00, 1.000) slope=0.841 dy=0.042 y=1.042
	(1.05, 1.042) slope=0.889 dy=0.044 y=1.087
	(1.10, 1.087) slope=0.930 dy=0.047 y=1.133
	(1.15, 1.133) slope=0.964 dy=0.048 y=1.181
	(1.20, 1.181) slope=0.988 dy=0.049 y=1.231
	(1.25, 1.231) slope=0.999 dy=0.050 y=1.281
	(1.30, 1.281) slope=0.996 dy=0.050 y=1.330
	(1.35, 1.330) slope=0.975 dy=0.049 y=1.379
	(1.40, 1.379) slope=0.936 dy=0.047 y=1.426
	(1.45, 1.426) slope=0.879 dy=0.044 y=1.470
	(1.50, 1.470) slope=0.806 dy=0.040 y=1.510
	(1.55, 1.510) slope=0.718 dy=0.036 y=1.546
	(1.60, 1.546) slope=0.619 dy=0.031 y=1.577
	(1.65, 1.577) slope=0.514 dy=0.026 y=1.603
	(1.70, 1.603) slope=0.405 dy=0.020 y=1.623
	(1.75, 1.623) slope=0.297 dy=0.015 y=1.638
	(1.80, 1.638) slope=0.192 dy=0.010 y=1.647
	(1.85, 1.647) slope=0.094 dy=0.005 y=1.652
	(1.90, 1.652) slope=0.003 dy=0.000 y=1.652
	(1.95, 1.652) slope=-0.080 dy=-0.004 y=1.648
	(2.00, 1.648) slope=-0.154 dy=-0.008 y=1.641

수동으로 하는거에 비해서는 확실히 빠르지만, 이거 받아적는데도 상당한 시간이 요구된다. (약 10분-_-)

