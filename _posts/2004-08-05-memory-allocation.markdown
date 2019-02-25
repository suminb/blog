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
  dsq_thread_id: '287066009'
  keywords: c,cpp,cpp,memory,메모리
post_id: '57'
published: true
redirect_from:
- /archives/57/
- /post/memory-allocation
status: publish
tags: []
title: 메모리 할당
type: post
---
응용프로그램이 사용하는 메모리 영역은 크게 스택(stack)과 힙(heap)으로 나눌 수 있다.

자동변수는 스택 영역에, 그 이외의 변수(global, static, new, malloc, GlobalAlloc)는 힙 영역에 할당된다.

힙은 또다시 두가지로 나뉘는데, 윈도우 힙과 CRT(C Run-Time)힙이다.

윈도우 힙은 모든 윈도우 응용프로그램이 공유하는 큰 메모리 공간으로, 주로 큰 메모리 블록을 할당받고자 할 때 사용한다. 윈도우 힙을 할당받으려면 GlobalAlloc 함수를 사용한다.

CRT 힙은 윈도우 힙과는 별도로 프로그램마다 별도로 존재하는 힙이다. malloc함수나 new연산자를 이용하여 메모리를 할당받으면 이 영역에 메모리가 할당된다.
CRT 힙은 초기에 64KB의 공간을 갖게 되며, 이 공간을 다 쓰면 메모리 공간을 두배씩 늘려나간다. 일반적으로 CRT 힙을 사용하는것이 윈도우 힙을 사용하는 것 보다 속도가 빠르지만, CRT 힙 영역에 큰 공간을 할당받으려면 메모리 영역을 넓혀나가는 작업을 여러번 해야 하므로 큰 메모리 공간이 필요할 때는 윈도우 힙을 사용하는 것이 바람직하다.

(참고로, malloc 함수보다 new 연산자가 더 빠르게 동작한다고 한다. 실험을 한번 해봐야겠네)

[윈도우 힙 할당받기]

<blockquote>The GlobalAlloc function allocates the specified number of bytes from the heap. Windows memory management does not provide a separate local heap and global heap.
Note  The global functions are slower than other memory management functions and do not provide as many features. Therefore, new applications should use the heap functions. However, the global functions are still used with DDE, the clipboard functions, and OLE data objects.
HGLOBAL GlobalAlloc( UINT uFlags,  SIZE_T dwBytes );
</blockquote>
MSDN에는 이렇게 나와 있다.
> GlobalAlloc 함수는 힙 영역에 특정 크기(바이트 단위)의 메모리를 할당해준다. 윈도우 메모리 관리자는 로컬 힙 영역과 글로벌 힙 영역을 나누는것을 지원하지 않는다.

GlobalAlloc 함수는 다음과 같이 사용할 수 있다.

	LPSTR lpMem = (LPSTR)GlobalAlloc(GMEM_FIXED|GMEM_ZEROINIT, 1024*1024);
	// ....
	GlobalFree(lpMem);

GMEM_MOVEABLE를 설정하면 메모리 블럭이 이동 가능하도록 할당되고, `GMEM_FIXED`를 설정하면 고정된 메모리 블럭이 할당된다. 여기에 `GMEM_ZEROINIT`를 조합하면 할당된 메모리가 0으로 초기화된다.

이동 가능한 메모리 블럭은 메모리가 부족할 경우 언제든지 다른 곳으로 이동될 수 있다. 메모리 블럭이 다른곳으로 이동되고 나면, 메모리 블럭을 가리키고 있던 포인터도 바뀌게 된다. 따라서, GlobalAlloc 함수는 메모리의 포인터를 넘겨주지 않고, 글로벌 핸들을 넘겨준다. 이동 가능한 메모리 블럭을 사용할 때에는 GlobalLock 함수를 이용하여 잠시 고정시켜 사용해야 한다.

이동 가능한 메모리 블럭은 다음과 같이 할당한다.

	HGLOBAL hMem = GlobalAlloc(GMEM_MOVEABLE, 1024*1024);
	LPSTR lpMem = (LPSTR)GlobalLock(hMem);
	// ....
	GlobalUnlock(hMem);
	GlobalFree(hMem);

Visual C++ 완벽가이드 2nd Edition 을 읽고 나름대로의 언어로 정리해봤다.

