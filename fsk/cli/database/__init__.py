import sqlite3

class Database():
  def __init__(self):
    self.con = sqlite3.connect("fsk.db")
    self.cur = self.con.cursor()
    self.create_table()

  def create_table(self):
  # Create table
    self.cur.execute('''CREATE TABLE IF NOT EXISTS vscode_workspaces
               (path, workspace)''')

  def add_paths_to_workspace(self, paths, workspace):
    for path in paths:
      query = f"INSERT INTO vscode_workspaces VALUES ('{path}', '{workspace}')"
      self.cur.execute(query)
    
    self.con.commit()

  def get_paths_by_enviroment(self, workspace):
    query = f"SELECT path FROM vscode_workspaces WHERE workspace = '{workspace}'"
    result = self.cur.execute(query)
    return result.fetchall()

  def get_workspaces(self):
    query = "SELECT workspace FROM vscode_workspaces GROUP BY workspace"
    result = self.cur.execute(query)
    return result.fetchall()
  

