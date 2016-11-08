Installation
============

Although most articles are written in Markdown, some are written in
reStructuredText. It requires
[`jekyll-rst`](https://github.com/xdissent/jekyll-rst) plugin in order to
render the articles.

The `jekyll-rst` plugin itself requires `docutils` and `pygments`. To install
them, exeucte the following command in a Python virtual environment.

    pip install docutils pygments

It also requires a Ruby package `rbST`, which can be installed as:

    gem install RbST

The `jekyll-rst` plugin is already included in this project as a Git submodule,
and it can be retrieved by issuing the following command.

    git submodule update --init --recursive

Checklist for writing a post
============================

1. Format file name correctly (`yyyy-mm-dd-title.format`)
1. Put `page.meta.disqus_identifier`
1. Categories and tags
  1. For tags, specify in which language the post is written
1. Author's name
