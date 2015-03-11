# An Introduction to Relational Databases and SQL #

This repo contains several samples and scripts you can use to get started
working with structured data and queries in a modern relational database.

We'll be using the SQLite database (specifically SQLite3), which is a free,
open source, embedded database. "Embedded" in this context means SQLite is
packaged as a reusable library of code which can be included in a larger 
project. Many software vendors embed SQLite, including Apple, Adobe, Dropbox,
and Google. It also comes preinstalled on OS X, most Linux distributions, and
every along with the Python programming language standard library.

## Basic Terms and Concepts ##

A _relational database_ collects structured data (that is, data which has a
well-defined internal format that a computer can work with) into _tables_.
Entries in those tables are called _rows_, and each tables structure is 
encoded as a set of named 'columns' with defined datatypes.

The term relational comes from _relational algebra_, which is a set of simple
operators that allows the combination and transformation of collections of 
structured data. Those operators are _selection_, _projection_, _product_ 
or _join_, _union_, and _intersection_. (If you've studied set theory then
many of these will be familar but it's not necessary to understand and use 
databases.)

Database _engines_ like SQLite provide tools to map between high-level, 
human-readable representations of structured data and bytes on disk (possibly
more than one disk or even more than one computer). They range widely in
complexity, cost, and sophistication.

We use the term _schema_ when describing the structure all of the tables in
a particular database instance. The process of defining that structure is 
_modelling_ or _schema design_.

You can get data in and out of your databases via _queries_. Most people write
queries using a semi-standardized language called _Structured Query Language_
(_SQL_). Even when you're using a tool that provides an alternate front-end 
view of your queries, odds are it's converting them to SQL behind the scenes.

## Getting Started ##

As we previously mentioned, the SQLite database tool is already installed on
OS X and most Linux systems. If you are running Windows you can download a 
copy from the [download page](http://sqlite.org/download.html) or use a 
[web-based demo console](http://kripken.github.io/sql.js/GUI/).

Some of the examples in this tutorial will also use the 
[Python](http://python.org/) standard library modules for SQLite. If you don't
have Python installed (again, it's pre-loaded on OS X and Linux, so this 
basically means Windows folk) you can 
[download it](https://www.python.org/downloads/) for free as well.

To check that you have everything installed, type the following into a 
terminal (or Windows command shell) window:

    sqlite3

You should see a prompt like the following:

    bitty:sql_tutorial lennon$ sqlite3
    SQLite version 3.8.5 2014-08-15 22:37:57
    Enter ".help" for usage hints.
    Connected to a transient in-memory database.
    Use ".open FILENAME" to reopen on a persistent database.

Then do the same for the 'python' command.

If you get a listing of version info and a prompt with three right carats
(<tt>&gt;&gt;&gt;</tt>) you're all set! Open up the file 
[README.md](examples/first_steps/README.md) in the <tt>examples/first_steps</tt>
directory and follow along!
