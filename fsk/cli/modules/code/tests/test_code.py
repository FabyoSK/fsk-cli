from fsk.cli.utils.testing import run_cli
from fsk.cli.scripts.main import cli

def test_entrypoint():
    result = run_cli(cli, ["code"])
    assert "Usage" in result.output

def test_create_workspace():
    args = [
        "code",
        "create",
        "--name",
        "test",
        "--path",
        "/path_1",
        "--path",
        "/path_2",
        "--path",
        "/path_3",
    ]
    result = run_cli(cli, args)
    assert "workspace test created" in result.output

def test_list_workspace_empty():
    args = [
        "code",
        "list",
    ]
    result = run_cli(cli, args)
    assert "No workspaces" in result.output

def test_list_workspace():
    # create some workspaces
    create_args_1 = [
        "code",
        "create",
        "--name",
        "workspace_1",
        "--path",
        "/path_1",
    ]
    run_cli(cli, create_args_1)

    create_args_2 = [
        "code",
        "create",
        "--name",
        "workspace_2",
        "--path",
        "/path_2",
    ]
    run_cli(cli, create_args_2)

    args = [
        "code",
        "list",
    ]
    result = run_cli(cli, args)

    assert "workspace_1" in result.output
    assert "workspace_2" in result.output
