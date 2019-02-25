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
  dsq_thread_id: '287065524'
post_id: '555'
published: true
redirect_from:
- /archives/555/
- /post/my-first-assembly-program
status: publish
tags:
- mips
title: 나의 첫 어셈블리 프로그램
type: post
---
~~~
.data

numbers: .word  17
         .word  50
         .word   3
         .word  23
         .word  60
         .word  97
         .word  20
         .word  82
         .word  53

numElements:    .word   9

# Your code goes below this line

newline:	.asciiz "\n"
text1:		.asciiz "The modified integers are\n"
text2:		.asciiz "\nThere were "
text3:		.asciiz " changes made.\n"

.text

main:
    # Function prologue -- even main has one
    subu  $sp, $sp, 24    # allocate stack space -- default of 24 here
    sw    $fp, 0($sp)     # save caller's frame pointer
    sw    $ra, 4($sp)     # save return address
    addiu $fp, $sp, 24    # setup main's frame pointer

    la	$a0, text1
    li	$v0, 4
    syscall

    la	$t0, numElements
    lw	$s1, 0($t0)
    li	$t8, 0
    li	$t9, 1

    li	$t7, 4
    la	$s0, numbers

    li	$s4, 0
loopBegin:
    slt	$t2, $t8, $s1
    beq	$t2, $zero, loopEnd

    lw	$s3, 0($s0)

    slt	$t0, $s3, 20
    bne	$t0, $zero, replace20

    li	$t1, 80
    slt	$t0, $t1, $s3
    bne	$t0, $zero, replace80
    j	final

replace20:
    li	$t1, 20
    sw	$t1, 0($s0)
    add	$s3, $zero, $t1
    add	$s4, $s4, 1
    j	final

replace80:
    li	$t1, 80
    sw	$t1, 0($s0)
    add	$s3, $zero, $t1
    add	$s4, $s4, 1

final:
    add	$a0, $zero, $s3
    li	$v0, 1
    syscall

    la	$a0, newline
    li	$v0, 4
    syscall

    add	$t8, $t8, 1
    add	$s0, $s0, $t7
    j	loopBegin

loopEnd:
    la	$a0, text2
    li	$v0, 4
    syscall

    add	$a0, $zero, $s4
    li	$v0, 1
    syscall

    la	$a0, text3
    li	$v0, 4
    syscall

done:   # Epilogue for main -- restore stack & frame pointers and return
    lw    $ra, 4($sp)     # get return address from stack
    lw    $fp, 0($sp)     # restore the caller's frame pointer
    addiu $sp, $sp, 24    # restore the caller's stack pointer
~~~

