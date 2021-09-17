import os
from database import Database

db = Database()

def open(paths):
    path = " ".join(paths)
    os.system(f'code {path}')
    print(f'opening {path} in VSCode')

def open_workspace(workspace):
    paths = db.get_paths_by_enviroment(workspace)

    workspace = ""

    for path in paths:
        workspace =  " ".join(path)
        os.system(f'code {workspace}')

    print(f'workspace open successfully')
    
def create_workspace(data):
    workspace_name = data[0]
    paths = data[1:]
    
    print(workspace_name)
    print(paths)

    paths = db.add_paths_to_workspace(paths, workspace_name)
    print(f'workspace {workspace_name} created')

def add_subcommand_code(subparsers):
    parser = subparsers.add_parser('code')

    parser.add_argument("-o","--open", type = str, nargs = "+",
        metavar = "", default = None,
        help = "open a VSCode folder")
    
    parser.add_argument("-ow","--open-workspace", type = str, nargs = 1,
        metavar = "", default = None,
        help = "open a VSCode workspace")

    parser.add_argument("-aw","--create-workspace", type = str, nargs = '+',
        metavar = "", default = None,
        help = "open a VSCode workspace")

    parser.add_argument("-lw","--list-workspace", type = str, nargs = None,
        metavar = "", default = None,
        help = "List the VSCode workspaces")

    args = parser.parse_args()
    print(args)
    if args.open != None:
        open(args.open)
    elif args.open_workspace != None:
        open_workspace(args.open_workspace[0])
    elif args.create_workspace != None:
        create_workspace(args.create_workspace)
