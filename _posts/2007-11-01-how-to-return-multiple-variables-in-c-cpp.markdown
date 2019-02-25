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
  dsq_thread_id: '287065082'
post_id: '683'
published: true
redirect_from:
- /archives/683/
- /post/how-to-return-multiple-variables-in-c-cpp
status: publish
tags:
- C
title: How To Return Multiple Variables in C/C++
type: post
---
There are several ways to get multiple variables from a function in C/C++. Remember C is a pass-by-value language and there is no exception.

### 1. Pointers

Using pointers is a common way to get multiple variables back.

	void add(int* tiger, int* leopard) {
		*tiger++;
		*leopard++;
	}

### 2. Arrays

We can do the same job by passing an array as an argument of a function which is expect to be modified, but I wouldn't recommend this as a general solution because every single element of the array has to be the same data type.

	int* add(int arg[]) {
		arg[0]++;
		arg[1]++;

		return arg;
	}

### 3. Struct

Structure is one of beautiful features in C even though there is no way to explicitly involve functions with it. It just works like a default data type such as `int`.

	typedef struct _zoo {
		int tiger;
		int leopard;
	} zoo;

	zoo add(zoo arg) {
		arg.tiger++;
		arg.leopard++;

		return arg;
	}

### 4. More?

How about this? Would it work?

	zoo* add(int tiger, int leopard) {
		zoo v = {tiger+1, leopard+1};

		return &v;
	}

The answer is *no*. It does not work because the stack of the function `add` is going to be cleaned up when the function is done. That means all the local variable of the function will be gone! Also, you will see a warning message like `function returns address of local variable` when you try to compile it.

