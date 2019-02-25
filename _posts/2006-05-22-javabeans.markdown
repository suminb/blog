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
  dsq_thread_id: '287066194'
post_id: '301'
published: true
redirect_from:
- /archives/301/
- /post/javabeans
status: publish
tags:
- Java
title: JavaBeans
type: post
---
# What are JavaBeans? #
JavaBeans are software components written in the Java programming language. Well, this kind of explanation probably would not be helpful.

# How to use JavaBeans? #
Here's a simple example.

###### beans/Bean.java ######

	/**
	 *
	 * @author superwtk
	 */
	public class Bean {

		private String name;

		/** Creates a new instance of Bean */
		public Bean() {
		}

		public String getName() {
			return name;
		}

		public void setName(String name) {
			this.name = name;
		}
	}

###### bean.jsp ######

	<%@page contentType="text/html"%>
	<%@page pageEncoding="UTF-8"%>
	<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
		"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html>
	  <head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>JSP Page</title>
	  </head>
	  <body>
		<jsp:useBean id="bean" class="beans.Bean">
		  <jsp:setProperty name="bean" property="name" value="An example of Bean" />
		</jsp:useBean>


		  With JSTL:
		  <c:out value="Name: ${bean.name}" />
		


		  With scriptlet:
		  <%
			out.println("Name: " + bean.getName());
		  %>
		

	  </body>
	</html>

The following bunch of code

	<jsp:useBean id="bean" class="beans.Bean">
	  <jsp:setProperty name="bean" property="name"
	   value="An example of Bean" />
	</jsp:useBean>

has the same effect with

	beans.Bean bean = new beans.Bean();
	bean.setName("An example of Bean");

For getting more information, refer to:

* [http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPBeans4.html#64054](http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPBeans4.html#64054)
* [http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPBeans5.html#66188](http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPBeans5.html#66188)
* [http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPBeans6.html#62111](http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPBeans6.html#62111)

# References #

* [http://en.wikipedia.org/wiki/Java_Beans](http://en.wikipedia.org/wiki/Java_Beans)
* My brain
</ul>
