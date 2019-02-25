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
  dsq_thread_id: '1699003503'
post_id: '1889'
published: true
redirect_from:
- /archives/1889/
- /post/translation-sample-search
status: publish
tags: []
title: Translation Sample Search
type: post
---
One of the goals of [Better Translator][better-translator] is to build a large database of natural language translation samples, which may ultimately lead us to develop our own translation engine rather than relying on Google Translate.

In spite of the possibility of the ambitious long-term goal of building our own translation engine, one of our short-term goals is to design and implement a *translation sample search engine*. It allows users to discover similar translation examples when they request a machine translation.

The first prototype of this search system has been implemented using the default [full-text search feature][search] provided by PostgreSQL. It works well in some cases where a query string consists of a small number of words (as opposed to a long sentence or a cluase with a large number of words), but our overall assessment was that it may not be the optimal solution to search for similar strings.

Today, we came across with a [research paper][paper] that might provide us some insights to make a significant improvement on the search quality. The main idea of the paper evolves around the goal to find similar files in a large file system.

The basic idea introduced in the paper is to use fingerprints (i.e., hashes) on several small parts of a string[^1], then *synchronize* the equal parts in two different strings.

Although it is a computationally intensive task to find similar entities that are similar to a given query, the *Sif* program introduced in the paper shows decent performance with a reasonably large data sets.

If we can adopt this to the translation sample search engine, we may be able to remarkably improve its search quality.

[better-translator]: http://better-translator.com
[paper]: http://dl.acm.org/citation.cfm?id=1267074.1267076
[search]: http://www.postgresql.org/docs/8.3/static/textsearch.html

[^1]: Not necessarily a string of characters; it may be an arbitrary binary sequence.

