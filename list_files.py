"""
Copyright 2024 Robby

DESCRIPTION:
    A script to list files in a folder along with their file sizes with a relative size unit depending on the file 
    (e.g., GB, MB, KB, Bytes) and display the file name and size in a rich.table.

INSTALL:
    pip install typer pathlib rich

USAGE EXAMPLE:
    > python file_lister.py list_files ./some_folder

LICENSE:
    MIT License
"""

# ::IMPORTS ------------------------------------------------------------------------ #

# CLI framework - https://pypi.org/project/typer/
import typer

# Data types for validation - https://docs.python.org/3/library/typing.html
from typing import Optional

# Cross-platform path handling - https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# Rich print for better formatting - https://rich.readthedocs.io/
from rich import print
from rich.table import Table
from rich.console import Console

import math

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "file_lister"

# ::CORE LOGIC --------------------------------------------------------------------- #
def get_file_size(path: Path) -> str:
    size_bytes = path.stat().st_size
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

# ::CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def list_files(folder_path: str):
    """Lists all files in the specified folder along with their sizes in a rich.table."""
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"The path {folder_path} is not a valid directory.")
        raise typer.Exit()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("File Name", style="dim")
    table.add_column("Size")

    for file_path in folder.iterdir():
        if file_path.is_file():
            size = get_file_size(file_path)
            table.add_row(file_path.name, size)

    console = Console()
    console.print(table)

# ::DEFAULT CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def version():
    """ get the version of the package """
    package_version = version(PKG_NAME)
    typer.echo(package_version)

# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":
    app()