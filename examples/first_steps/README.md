# Example #1: First Steps #

The file [schema.sql](schema.sql) in this directory has the SQL commands
needed to define a new database with one table. Open it in your favorite text
editor and read along as we break it down.

## Basic Syntax ##

There are a few rules for writing SQL you should understand. First, SQL
supports comments; any line beginning with two dashes (<tt>--</tt>) will
be ignored by the computer.

Second, most statements in SQL have to be ended with a semicolon. This 
allows you to break up longer statements into multiple lines of text.

SQL allows some built-in types (mainly numbers and booleans) to be typed
directly. Strings are enclosed in single-quote characters, and most other
types are entered as strings and then converted to the appropriate type by
the database engine.

## Defining Tables ##

Since all of our data has to go into one or more tables, our first task is
to define one. Open up [schema.sql](schema.sql) and look at lines 3-8.
