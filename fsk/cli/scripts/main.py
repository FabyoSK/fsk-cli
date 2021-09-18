import argparse

def main():
  parser = argparse.ArgumentParser(prog="fsk", description = "A CLI by FSK!")

  subparsers = parser.add_subparsers()

  from ..modules import code
  code.add_subcommand_code(subparsers)

