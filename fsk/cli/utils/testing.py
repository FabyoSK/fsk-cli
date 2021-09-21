import sys

def run_cli(cli, args, exit_code=0):
    """Run Click command line tool.
    Thin wrapper around `click.testing.CliRunner`
    that prints info to stderr if the command fails.
    Parameters
    ----------
    cli : click.Command
        Click command
    args : list of str
        Argument list
    exit_code : int
        Expected exit code of the command
    Returns
    -------
    result : `click.testing.Result`
        Result
    """
    from click.testing import CliRunner

    result = CliRunner().invoke(cli, args, catch_exceptions=False)

    if result.exit_code != exit_code:
        sys.stderr.write("Exit code mismatch!\n")
        sys.stderr.write("Ouput:\n")
        sys.stderr.write(result.output)

    return result