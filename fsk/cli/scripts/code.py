import os
import click
from fsk.cli.modules.code import Code

code = Code()



@click.command()
@click.argument('name')
def open(name):
    """Open a workspace"""
    code.open_workspace(name)

@click.command()
def list():
    """List all workspaces"""
    code.list_workspace()

@click.command()
@click.option("-n", "--name", help="Name of the workspace")
@click.option("-p", "--path",  multiple=True, help="The path of the folders")
def create(name, path):
    """Create a workspace"""
    code.create_workspace(name, path)
