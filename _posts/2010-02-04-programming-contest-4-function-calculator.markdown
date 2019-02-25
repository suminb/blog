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
  dsq_thread_id: '287065034'
post_id: '1222'
published: true
redirect_from:
- /archives/1222/
- /post/programming-contest-4-function-calculator
status: publish
tags:
- Google
- pymt
- Python
title: 'Programming Contest: 4-function Calculator'
type: post
---
Today's programming contest, sponsored by Jude Nelson, was to make a 4-function calculator using PyMT. There were some extra credits for additional features such as support for trigonometric functions, parenthesis for changing orders of operations, and so on.

Even though I was the winner (thanks to Google), I admit I wrote an embarrasingly low quality code, but I think I have legitimate excuses; I've never dealt with PyMT until few hours ago, and we had a very tight time constraint.

So, here I'm posting the full source code at the request of Charles and a couple more people.

~~~
import urllib, urllib2, re
from pymt import *

# Google search would give me a 403 error so I had to "pretend" to be a real web browser.
useragent = 'Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic) Firefox/3.5.6'

# This is how you get things done.
url = 'http://www.google.com/search?'

m = MTWidget()

button0 = MTButton(label='0', pos=(0, 0), size=(90, 90))
buttonpr = MTButton(label='.', pos=(100,0), size=(90, 90))
buttonok = MTButton(label='=', pos=(200,0), size=(90, 90))

button1 = MTButton(label='1', pos=(0,100), size=(90, 90))
button2 = MTButton(label='2', pos=(100,100), size=(90, 90))
button3 = MTButton(label='3', pos=(200,100), size=(90, 90))

button4 = MTButton(label='4', pos=(0,200), size=(90, 90))
button5 = MTButton(label='5', pos=(100,200), size=(90, 90))
button6 = MTButton(label='6', pos=(200,200), size=(90, 90))

button7 = MTButton(label='7', pos=(0,300), size=(90, 90))
button8 = MTButton(label='8', pos=(100,300), size=(90, 90))
button9 = MTButton(label='9', pos=(200,300), size=(90, 90))

m.add_widget(button0)
m.add_widget(buttonpr)
m.add_widget(buttonok)
m.add_widget(button1)
m.add_widget(button2)
m.add_widget(button3)
m.add_widget(button4)
m.add_widget(button5)
m.add_widget(button6)
m.add_widget(button7)
m.add_widget(button8)
m.add_widget(button9)

buttonlp = MTButton(label='(', pos=(400,0), size=(90, 90))
buttonrp = MTButton(label=')', pos=(500,0), size=(90, 90))

m.add_widget(buttonlp)
m.add_widget(buttonrp)

buttonp = MTButton(label='+', pos=(300,300), size=(90, 90))
buttons = MTButton(label='-', pos=(300,200), size=(90, 90))
buttonm = MTButton(label='*', pos=(300,100), size=(90, 90))
buttond = MTButton(label='/', pos=(300,0), size=(90, 90))

m.add_widget(buttonp)
m.add_widget(buttons)
m.add_widget(buttonm)
m.add_widget(buttond)

buttonbs = MTButton(label='<-', pos=(400,100), size=(90, 90))
buttoncl = MTButton(label='CL', pos=(400,200), size=(90, 90))

m.add_widget(buttonbs)
m.add_widget(buttoncl)

buttonsin = MTButton(label='sin', pos=(500,300), size=(90, 90))
buttoncos = MTButton(label='cos', pos=(500,200), size=(90, 90))
buttontan = MTButton(label='tan', pos=(500,100), size=(90, 90))

m.add_widget(buttonsin)
m.add_widget(buttoncos)
m.add_widget(buttontan)

buttonhex = MTButton(label='0x', pos=(600,0), size=(90, 90))
buttonbin = MTButton(label='0b', pos=(600,100), size=(90, 90))

m.add_widget(buttonhex)
m.add_widget(buttonbin)

inputl = MTLabel(label='', pos=(0, 400), size=(90, 300))
m.add_widget(inputl)

#@button0.event
#def on_press(*largs):
#	print 'on_press()', button0.state, largs

@button0.event
def on_release(*largs):
	inputl.label += '0'

@button1.event
def on_release(*largs):
	inputl.label += '1'

@button2.event
def on_release(*largs):
	inputl.label += '2'

@button3.event
def on_release(*largs):
	inputl.label += '3'

@button4.event
def on_release(*largs):
	inputl.label += '4'

@button5.event
def on_release(*largs):
	inputl.label += '5'

@button6.event
def on_release(*largs):
	inputl.label += '6'

@button7.event
def on_release(*largs):
	inputl.label += '7'

@button8.event
def on_release(*largs):
	inputl.label += '8'

@button9.event
def on_release(*largs):
	inputl.label += '9'

@buttonlp.event
def on_release(*largs):
	inputl.label += '('

@buttonrp.event
def on_release(*largs):
	inputl.label += ')'

@buttonp.event
def on_release(*largs):
	inputl.label += '+'

@buttons.event
def on_release(*largs):
	inputl.label += '-'

@buttonm.event
def on_release(*largs):
	inputl.label += '*'

@buttond.event
def on_release(*largs):
	inputl.label += '/'

@buttonpr.event
def on_release(*largs):
	inputl.label += '.'

@buttonbs.event
def on_release(*largs):
	inputl.label = inputl.label[:-1]

@buttoncl.event
def on_release(*largs):
	inputl.label = ''

@buttonsin.event
def on_release(*largs):
	inputl.label += 'sin('

@buttoncos.event
def on_release(*largs):
	inputl.label += 'cos('

@buttontan.event
def on_release(*largs):
	inputl.label += 'tan('

@buttonhex.event
def on_release(*largs):
	inputl.label += '0x'

@buttonbin.event
def on_release(*largs):
	inputl.label += '0b'

@buttonok.event
def on_release(*largs):
	inputl.label = get_result(inputl.label)

def get_result(query):
	headers = {'User-Agent':useragent}
	req = urllib2.Request(url + urllib.urlencode({'q':query}), None, headers)
	r = urllib2.urlopen(req)
	result = r.read()

	m1 = re.search('
<td nowrap >
<h2 class=r style="font-size:138%"><b>', result)
	if m1 is None:
		return 'Invalid expression'

	m2 = re.search('</b>', result[m1.end():])

	return result[m1.end():(m1.end()+m2.start())]

runTouchApp(m)
~~~

