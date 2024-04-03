<p align="center">
    <img src="./typer_cli_gpt_banner.jpg" />
    <br />
    <i>
    Create Typer CLI's with an OpenAI GPT
    </i>
    <br />
    <br />
    <a href="https://robbyboney.notion.site/">
        <img
            src="https://img.shields.io/badge/GPT-black?color=black&style=for-the-badge&logo=OpenAI"
            alt="GPT Link"
        />
    </a>
    <a href="https://medium.com/@robbyb_77782">
        <img
            src="https://img.shields.io/badge/Blog Post-black?color=black&style=for-the-badge&logo=Medium"
            alt="Blog Post"
        />
    </a>
    <a href="https://medium.com/@robbyb_77782">
        <img
            src="https://img.shields.io/badge/v1.0.0-black?color=white&style=for-the-badge"
            alt="Version"
        />
    </a>
</p>



All the code, scripts and docs for a Typer CLI python script used for a ChatGPT GPT assistant

<br>
<br>


# Starters

- create a cli script to list all files in a folder with their file size
- create a cli script to find a recursively find matching files 
- create a cli script to show the contents of a file
- create a cli script to move files with a .png extension to a folder
- create a cli script to generate a boid flocking algorithm simulation with pygame

<br>
<br>

# The Template Script
```python
"""
Copyright <<year>> <<insert publisher name>>

DESCRIPTION:
    <<describe the purpose of the script>>

INSTALL:
    pip install <<list packages to pip install>>

USAGE EXAMPLE:
    > python template_simple_cli.py example_cmd

LICENSE:
    << insert license text >>
"""


# ::IMPORTS ------------------------------------------------------------------------ #

# cli framework - https://pypi.org/project/typer/
import typer

# data types for validation - https://docs.python.org/3/library/typing.html
from typing import Optional

# cross platform path handling - https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# Standard library import for package version retrieval - https://docs.python.org/3/library/importlib.metadata.html
from importlib.metadata import version

# NOTE: only include if needed
# Rich print for better formatting - https://rich.readthed.com/
# from rich import print


# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

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
    """ example basic command """
    print("hello typer!")


@app.command()
def example_cmd_args(
    name: str,
    last_name: str = typer.Option(default="<unknown>"),
    age: Optional[str] = typer.Argument(None),
):
    """ example command with arguments """
    print(f"name:{name}  last-name:{last_name}  age:{age}")

@app.command()
def example_empty_cmd():
    """ example command leave blank for dev to fill out """
    
    # --- YOUR CODE HERE --- #

    raise NotImplementedError

@app.command()
def example_loading_spinner_cmd():
    """ example command with rich package spinner for cli loading indicator """
    # NOTE: 'import rich' must be added to imports for this command
    
    with rich.console.Console() as console:
        # do some action
        pass

@app.command()
def example_user_input_cmd():
    """ example command to get user input """
    person_name = typer.prompt("What's your name?")
    print(f"Hello {person_name}")



# ::DEFAULT CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def version():
    """ get the version of the package """
    package_version = version(PKG_NAME)
    typer.echo(package_version)


# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":  # ensure importing the script will not execute
    app()
```