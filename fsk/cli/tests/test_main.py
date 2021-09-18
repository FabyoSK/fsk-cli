import os
from fsk.cli.utils.testing import run_cli
from fsk.cli.scripts.main import cli

os.environ['DB_URL'] = "sqlite:///:memory:"

def test_entrypoint():
    result = run_cli(cli, [])
    assert "Usage" in result.output
