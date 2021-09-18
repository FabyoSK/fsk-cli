import os
from fsk.cli.database import Database

db = Database()

class Code: 
    def open(self, paths):
        path = " ".join(paths)
        os.system(f'code {path}')
        print(f'opening {path} in VSCode')

    def open_workspace(self, data):
        workspace = data[0]
        paths = db.get_paths_by_enviroment(workspace)

        workspace = ""

        for path in paths:
            workspace =  " ".join(path)
            os.system(f'code {workspace}')

        print(f'workspace open successfully')
        
    def create_workspace(self, name, paths):
        db.add_paths_to_workspace(paths, name)
        print(f'workspace {name} created')

    def list_workspace(self):
        workspaces = db.get_workspaces()

        if workspaces:
            print(f'Workspace List:')
            for workspace in workspaces:
                print("=> " + " ".join(workspace))
        else:
            print("No workspaces")
