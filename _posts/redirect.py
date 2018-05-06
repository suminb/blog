"""Converts .html posts that have been converted by the jekyll-import tool to
Makrdown format."""

import os
import sys
import re


def read_file(file_name):
    return open(file_name).read()


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def replace_html_tags(text):
    text = re.sub(r'<p>', '', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<br />', '', text)

    return text


def process(text):
    s = re.search(r"  - /archives/(\d+)", text)
    post_id = s.group(1)

    text = re.sub(r"  - /archives/(\d+)", '  - /archives/{}/'.format(post_id), text)

    return text


if __name__ == '__main__':
    source_file_name = sys.argv[1]

    content = read_file(source_file_name)
    content = process(content)

    write_file(source_file_name, content)