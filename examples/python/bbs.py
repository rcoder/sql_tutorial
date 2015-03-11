import sqlite3
from contextlib import closing

from flask import Flask, request, render_template, redirect

app = Flask(__name__)

def get_db():
  return sqlite3.connect("bbs.sqlite3")

# not used currently, but is an alternative method to initialize the DB
def migrate_db():
  with closing(get_db()) as db:
    with app.open_resource('schema.sql', mode='r') as fh:
      db.cursor().executescript(fh.read())
      db.commit()

@app.route("/")
def index():
  with closing(get_db()) as db:
    messages = db.execute(
      "SELECT alias, body, created_at FROM messages ORDER by id DESC LIMIT 25"
    ).fetchall()
    print(messages)
    return render_template("index.html", messages=messages)

@app.route("/post", methods=["POST"])
def post():
  alias = request.form.get('alias', None)
  body = request.form['body']

  with closing(get_db()) as db:
    params = (alias, body)
    stmt = db.execute("INSERT INTO messages(alias, body) VALUES(?, ?)", params)
    db.commit()

  return redirect("/")

if __name__ == "__main__":
  app.debug = True
  app.run()
