import sqlite3


# def connect():

class Database():
  def __init__(self):
    self.con = sqlite3.connect('fsk.db')
    self.cur = self.con.cursor()

  def create_table(self):
  # Create table
    self.cur.execute('''CREATE TABLE vscode
               (name, path, environment)''')

  def add_path(self, name, path, environment):
    self.query = f"INSERT INTO vscode VALUES ('{name}', '{path}', '{environment}')"
    self.cur.execute(query)
    self.con.commit()

  def get_path_by_enviroment(self, environment):
    query = f"SELECT path FROM vscode WHERE environment = '{environment}'"
    result = self.cur.execute(query)
    print(result.fetchall())
    return result.fetchall()


# create_table()
# create_table()
# add_path("samba", "~/chuvaio/samba_web", "samba")

