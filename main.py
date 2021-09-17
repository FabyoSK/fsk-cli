import argparse

def main():
  parser = argparse.ArgumentParser(prog="fsk", description = "A CLI by FSK!")

  subparsers = parser.add_subparsers()

  from code import add_subcommand_code
  add_subcommand_code(subparsers)

if __name__ == "__main__":
    # calling the main function
    main()
