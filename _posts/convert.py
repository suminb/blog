"""Converts .html posts that have been converted by the jekyll-import tool to
Makrdown format."""

import os
import sys
import re

import yaml


def read_file(file_name):
    return open(file_name).read()


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def load_metadata(text):
    offset_start = text.find('---') + 3
    offset_end = text.find('---', 1)
    return yaml.load(text[offset_start:offset_end])


def insert_redirect_predicate2(text, filename):
    """Redirect post/$pid to posts/$pid"""
    metadata = load_metadata(text)
    metadata.setdefault('redirect_from', [])
    metadata['redirect_from'].append(f'/post/{filename[11:]}')

    metadata = yaml.dump(metadata, allow_unicode=True, default_flow_style=False)
    offset = text.find('---', 1)
    return '---\n{0}{1}'.format(metadata, text[offset:])


def replace_html_tags(text):
    text = re.sub(r'<p>', '', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<br />', '', text)

    return text


def insert_redirect_predicate(text):
    s = re.search(r"post_id: '(\d+)'", text)
    post_id = s.group(1)

    index = text.find('\n---\n', 3)

    prefix = text[:index]
    suffix = text[index:]

    predicate = '''
redirect_from:
  - /archives/{}/'''.format(post_id)

    return prefix + predicate + suffix


def insert_absolute_url(text):
    return text.replace('src="/wp-content', 'src="http://blog.suminb.com/wp-content')


if __name__ == '__main__':
    source_file_name = sys.argv[1]
    source_file_name_noext = os.path.splitext(source_file_name)[0]
    # target_file_name = '{}.markdown'.format(source_file_name_noext)

    content = read_file(source_file_name)
    # content = replace_html_tags(content)
    # content = insert_redirect_predicate(content)
    # content = insert_absolute_url(content)

    content = insert_redirect_predicate2(content, source_file_name_noext)

    write_file(source_file_name, content)
