import sqlite3

class Database:
  def __init__(self, db):
    self.conn = sqlite3.connect(db)
    self.cur = self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS pocket (id INTEGER PRIMARY KEY, account text, password text)")
    self.conn.commit()

  def fetch(self):
    self.cur.execute("SELECT * FROM pocket")
    rows = self.cur.fetchall()
    return rows


  def insert(self, account, password):
    self.cur.execute("INSERT INTO pocket VALUES (NULL, ?, ?)", (account, password))
    self.conn.commit()

  def remove(self, id):
    self.cur.execute("DELETE FROM pocket WHERE id=?", (id,))
    self.conn.commit()

  def update(self, id, account, password):
    self.cur.execute("UPDATE pocket SET account = ?, password = ? WHERE id = ?", (account, password, id))
    self.conn.commit()

  def __del__(self):
    self.conn.close()

db = Database("pw.db")
# db.insert("facebook", "asdasd")
# db.insert("twitter", "qweqwe")
# db.insert("email", "asdasd")
