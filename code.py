import os

def open(args):
    path = args.open[0]
    os.system(f'code {path}')

def add_subcommand_code(subparsers):
    parser = subparsers.add_parser('code')

    parser.add_argument("-o","--open", type = str, nargs = 1,
        metavar = "", default = ".",
        help = "Open a VSCode folder")

    args = parser.parse_args()
    print(args)
    if args.open != None:
        open(args)
