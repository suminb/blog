---
author:
  display_name: Sumin
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
  login: admin
categories:
- Tutorial
layout: post
meta:
  _edit_last: '1'
  dsq_thread_id: '287066540'
post_id: '1007'
published: true
redirect_from:
- /archives/1007/
- /post/grocery-store-club-card-imitation
status: publish
tags:
- experiment
- Fry's
- Safeway
title: Grocery Store Club Card Imitation
type: post
---
Introduction
------------

<img src="http://blog.suminb.com/wp-content/uploads/2009/03/dsc_6422.jpg" alt="dsc_6422" title="dsc_6422" width="400" height="266" class="aligncenter size-full wp-image-1009" />

Having club cards for grocery stores that you frequently go is a great way to save money. Well, technically, you don't *save* anything but at least it helps you to spend less.

However, when it comes to multiple cards, it is kind of annoying to carry all of them, especially if you don't have much space in your wallet. So I thought it would be great if I can replace them with a single sheet of paper, which is virtually massless/volumeless compared to those plastic cards.

Procedures
--------------

If you want to make an imitation of something, what would be your first step? I would say the first step you need to take is to figure out how the original one works.

My assumption is that a POS scanner reads the barcode on a club card and then retrieves my membership information from the database. Based on this assumption, we can do the same thing without the club card, if we can generate an identical barcode. Now what we need is a barcode generator. I used this [barcode generator](http://www.barcoding.com/upc). However, there is a bunch of different types of barcodes, so I had to figure out which one the club card uses. It turned out to be UPC-A, which is also used by all the products that grocery stores like Fry's and Safeway have.

For example,

<img src="http://blog.suminb.com/wp-content/uploads/2009/03/barcode.png" alt="barcode" title="barcode" width="184" height="84" class="aligncenter size-full wp-image-1025" />

(TODO: I'll finish up this later)

Result
-------

<img src="http://blog.suminb.com/wp-content/uploads/2009/03/dsc_6427.jpg" alt="dsc_6427" title="dsc_6427" width="400" height="266" class="aligncenter size-full wp-image-1010" />

It works :D

