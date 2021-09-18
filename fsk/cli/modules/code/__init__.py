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
        
    def create_workspace(self, data):
        workspace_name = data[0]
        paths = data[1:]

        paths = db.add_paths_to_workspace(paths, workspace_name)
        print(f'workspace {workspace_name} created')

    def list_workspace(self):
        workspaces = db.get_workspaces()

        print(f'Workspace List:')
        for workspace in workspaces:
            print("=> " + " ".join(workspace))

    def add_subcommand(self, subparsers):
        parser = subparsers.add_parser('code')

        parser.add_argument("-o","--open", type = str, nargs = "+",
            metavar = "", default = None,
            help = "open a VSCode folder")
        
        parser.add_argument("-ow","--open-workspace", type = str, nargs = 1,
            metavar = "", default = None,
            help = "open a VSCode workspace")

        parser.add_argument("-cw","--create-workspace", type = str, nargs = "+",
            metavar = "", default = None,
            help = "open a VSCode workspace")

        parser.add_argument("-lw","--list-workspace", action='store_true',
            help = "List the VSCode workspaces")
        
    def parse_args(self, args):
        if args.open != None:
            self.open(args.open)
        elif args.open_workspace != None:
            self.open_workspace(args.open_workspace)
        elif args.create_workspace != None:
            self.create_workspace(args.create_workspace)
        elif args.list_workspace != None:
            self.list_workspace()
        else: 
            pass
