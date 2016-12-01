<h1>Web Application Project 2016 by Vaida Abelkyte</h1>

This repository contains code and information for a third-year undergraduate project for the module Data Representation and Querying. The module is taught to undergraduate students at GMIT in the Department of Computer Science and Applied Physics. The lecturer is
<a href="/newpost">Ian McLoughlin.</a>

<h2>Overview</h2>

I have created Single-Page Web Application (SPA) which is a small model of blog-website.
It has a home page with a list of posts, the LogIn page and the 'add post' page.


The SPA is build using the in class examples aswell lecturer examples on his Github page and documentation of <a href="http://flask.pocoo.org/docs/0.11/">Flask</a>
and <a href="https://docs.python.org/2/library/sqlite3.html">Sqlite3.</a>
It is written in  <a href="https://www.python.org/">Python3.</a> using <a href="http://flask.pocoo.org/docs/0.11/">Flask</a> web micro-framework. They both must be installed 
to run the application.
<a href="https://docs.python.org/2/library/sqlite3.html">Sqlite3.</a> also required to run the SPA as it it used as database.


<h2>Instructions to run the application</h2>
The database file added in repository.
The app can be run locally :
$ python app.py

Without .db file user must first run: <br>
$ python sql.py   ---->   to create a file and then :<br>
$ python app.py   -----> to star the app.


The log in name in "login.html" is <strong>   user   </strong>  and the password is  <strong>   user   </strong> 

The new post is created in "newpost.html" page and saved into <strong>   posts.db   </strong> file.


