import click
# from fsk.cli.modules.code import Code,  list_workspace

# create the instances of the classes
# code = Code() 

# http://click.pocoo.org/5/documentation/#help-parameter-customization
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

# https://click.palletsprojects.com/en/5.x/python3/#unicode-literals
click.disable_unicode_literals_warning = True

# @click.group()
# def main():
#   parser = argparse.ArgumentParser(prog="fsk", description = '''
#     
#   ''')
  
#   subparsers = parser.add_subparsers()

#   # add subparsers
#   code.add_subcommand(subparsers)

#   # parse_args
#   args = parser.parse_args()

#   code.parse_args(args)


@click.group("fsk", context_settings=CONTEXT_SETTINGS)
def cli():
    """ 
    A CLI to by FSK! To automate tasks
    """
    pass

@cli.group("code")
def cli_code():
    """ A helper to automate some VSCode tasks 

    \b
    Examples
    --------
    \b
    $ fsk code --list-workspaces
    $ fsk code --create-workspace
    """


def add_subcommands():
  from .code import open, create, list
  cli_code.add_command(open)
  cli_code.add_command(create)
  cli_code.add_command(list)


add_subcommands()