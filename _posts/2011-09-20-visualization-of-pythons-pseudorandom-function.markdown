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
  _thumbnail_id: '1529'
  dsq_thread_id: '420841339'
post_id: '1524'
published: true
redirect_from:
- /archives/1524/
- /post/visualization-of-pythons-pseudorandom-function
status: publish
tags:
- NumPy
- PIL
- Python
title: Visualization of Python's Pseudorandom Function
type: post
---
<img src="http://blog.suminb.com/wp-content/uploads/2011/09/random.png" alt="" title="random" width="400" height="400" class="aligncenter size-full wp-image-1529" />

This is a slight modification of a part of my computer vision homework, so you might see some functions that appear to be unnecessarily complicated.

You will need following Python packages.

* [NumPy](http://numpy.scipy.org)
* [Python Imaging Library](http://www.pythonware.com/products/pil)

~~~
from random import randint
from numpy import matrix, empty, uint32
from PIL import Image

def generate_random_spectrum(n):
    """Generates random light spectrum, where n is the number of elements in the row vector."""
    return map(lambda x: randint(0, 0xFFFFFF), xrange(n))

def fill_image_buffer(data, data_shape, m):
    """ data_shape: Conceptual data array size (h, w)
        m: Magnification"""
    array = empty((data_shape[1]*m, data_shape[0]*m), uint32)
    for i in xrange(data_shape[0]):
        for j in xrange(data_shape[1]):
            rgb = data[i*data_shape[1] + j]
            array[i*m:i*m+m, j*m:j*m+m] = 0xFF000000 + rgb

    return array

def save_image(shape, data, filename):
    im = Image.frombuffer('RGBA', shape, data, 'raw', 'RGBA', 0, 1)
    im.save(filename)

spectra = generate_random_spectrum(1600)
buf = fill_image_buffer(spectra, (40, 40), 10)

save_image((400, 400), buf, 'random.png')
~~~

