"""
Copyright <<year>> <<insert publisher name>>

DESCRIPTION:
    <<describe the purpose of the script>>

USAGE EXAMPLE:
    > python template_simple_cli.py example_cmd
"""


# ::IMPORTS ------------------------------------------------------------------------ #

# cli framework - https://pypi.org/project/typer/
import typer

# data types for validation - https://docs.python.org/3/library/typing.html
from typing import Optional

# cross platform path handling - https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# package for reading details about this package
import pkg_resources

# <<OPEN   INCLUDE EXTRA IMPORTS HERE>>
# <<CLOSE  INCLUDE EXTRA IMPORTS HERE>>

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(add_completion=False)

# ::SETUP SUBPARSERS --------------------------------------------------------------- #
# app.add_typer(<<module.app>>, name="subparser")

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "<<python package name>>"

# ::CORE LOGIC --------------------------------------------------------------------- #
# place core script logic here and call functions
# from the cli command functions to separate CLI from business logic

# ::EXAMPLE CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def example_cmd():
    """ example command """
    print("hello typer!")


@app.command()
def example_cmd_args(
    name: str,
    last_name: str = typer.Option(default="<unknown>"),
    age: Optional[str] = typer.Argument(None),
):
    """ example command with arguments """
    print(f"name:{name}  last-name:{last_name}  age:{age}")


# ::DEFAULT CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def version():
    """ get the version of the package """
    version = pkg_resources.get_distribution(PKG_NAME).version
    typer.echo(version)


# ::EXECUTE ------------------------------------------------------------------------ #
def main():
    app()


if __name__ == "__main__":  # ensure importing the script will not execute
    main()
