import argparse
from fsk.cli.modules.code import Code

# create the instances of the classes
code = Code() 

def main():
  parser = argparse.ArgumentParser(prog="fsk", description = '''
    A CLI to by FSK!
    to automate tasks
  ''')
  
  subparsers = parser.add_subparsers()

  # add subparsers
  code.add_subcommand(subparsers)

  # parse_args
  args = parser.parse_args()

  code.parse_args(args)

