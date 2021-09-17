import argparse
import os


def main(args=None):
  parser = argparse.ArgumentParser(prog="FSK CLI", description = "A CLI by FSK!")

  # parser.add_argument("-co","--code", type = str, nargs = 1,
  #                       metavar = "", default = None,
  #                       help = "Control VSCode using the CLI.")

  parser.add_argument("-o","--open", type = str, nargs = 1,
        metavar = "", default = ".",
        help = "Open a VSCode folder")

  # subparsers = parser.add_subparsers()/

  # from code import add_subcommand_code
  # add_subcommand_code(subparsers)

  # parse the arguments from standard input
  args = parser.parse_args(args)
  # print("S" , args)
    
  # calling functions depending on type of argument
  if args.open != None:
    open(args)

def open(args):
    path = args.open[0]
    os.system(f'code {path}')


if __name__ == "__main__":
    # calling the main function
    main()

