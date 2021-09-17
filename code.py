import os

def add_subcommand_code(subparsers):
    parser = subparsers.add_parser('code')
    # parser.set_defaults(func=hello)

    parser.add_argument("-o","--open", type = str, nargs = 1,
        metavar = "", default = ".",
        help = "Open a VSCode folder")
    # parser.add_argument("-o","--open", type = str)

    args = parser.parse_args()


def open(args):
    path = args.open[0]
    os.system(f'code {path}')
