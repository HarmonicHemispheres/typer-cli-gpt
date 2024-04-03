"""
Copyright 2024 Robby

DESCRIPTION:
    A CLI tool to list all files in a folder along with their file sizes

INSTALL:
    pip install typer rich pandas

USAGE EXAMPLE:
    > python list_files.py ls /path/to/directory

LICENSE:
    MIT License
"""


# ::IMPORTS ------------------------------------------------------------------------ #

# CLI framework - https://pypi.org/project/typer/
import typer

# Data types for validation - https://docs.python.org/3/library/typing.html
from typing import Optional

# Cross platform path handling - https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# Standard library import for package version retrieval - https://docs.python.org/3/library/importlib.metadata.html
from importlib.metadata import version

# Rich print for better formatting - https://rich.readthedocs.io/
from rich import print

# Data manipulation and analysis - https://pandas.pydata.org/
import pandas as pd

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "list_files"

# ::CORE LOGIC --------------------------------------------------------------------- #
def get_file_sizes(path: Path):
    # Logic to get file sizes and convert them to a readable format
    files = []
    for item in path.iterdir():
        if item.is_file():
            size = item.stat().st_size
            if size >= 1 << 30:
                size_str = f"{size / (1 << 30):.2f} GB"
            elif size >= 1 << 20:
                size_str = f"{size / (1 << 20):.2f} MB"
            elif size >= 1 << 10:
                size_str = f"{size / (1 << 10):.2f} KB"
            else:
                size_str = f"{size} bytes"
            files.append({"File": item.name, "Size": size_str})
    return files

# ::CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def ls(path: str):
    """List all files in a folder with their file size."""
    directory = Path(path)
    if not directory.is_dir():
        print(f"[red]Error: '{path}' is not a valid directory.[/red]")
        raise typer.Exit()

    file_list = get_file_sizes(directory)
    df = pd.DataFrame(file_list)
    print(df.to_markdown(index=False))

# ::DEFAULT CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def version():
    """ get the version of the package """
    package_version = version(PKG_NAME)
    typer.echo(package_version)

# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":
    app()