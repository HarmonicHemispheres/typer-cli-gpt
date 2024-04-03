"""
Copyright 2024 Filinious Inc

DESCRIPTION:
    A script to list and sort files by size in a folder, displaying sizes in GB, MB, KB, or bytes.

INSTALL:
    pip install rich

USAGE EXAMPLE:
    > python filesorter.py show

LICENSE:
    BSD License
"""


# ::IMPORTS ------------------------------------------------------------------------ #

# CLI framework - https://pypi.org/project/typer/
import typer

# Data types for validation - https://docs.python.org/3/library/typing.html
from typing import Optional

# Cross-platform path handling - https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# Standard library import for package version retrieval - https://docs.python.org/3/library/importlib.metadata.html
from importlib.metadata import version

# Rich print, ask, and table for better formatting and interactive prompts - https://rich.readthedocs.io/
from rich import print
from rich.prompt import Prompt
from rich.table import Table

# Additional import for file system operations
import os

# Import for mathematical operations
import math

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "filesorter"

# ::CORE LOGIC --------------------------------------------------------------------- #
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def list_files(ignore_exts=[]):
    files = []
    for entry in os.scandir('.'):
        if entry.is_file() and not any(entry.name.endswith(ext) for ext in ignore_exts):
            files.append((entry.name, convert_size(os.path.getsize(entry.path))))
    return sorted(files, key=lambda x: x[1])

# ::CLI COMMANDS ------------------------------------------------------------------- #
@app.command()
def show():
    """Asks the user if any file extensions should be ignored, then lists files in the current folder with their file size in a readable format and sorts them by size."""
    extensions = Prompt.ask("Enter file extensions to ignore, separated by commas (e.g., .jpg,.png)").split(',')
    files = list_files(extensions)

    table = Table(title="File Sizes")
    table.add_column("File", justify="left")
    table.add_column("Size", justify="right")

    for file, size in files:
        table.add_row(file, size)

    print(table)

# ::DEFAULT CLI COMMANDS ----------------------------------------------------------- #
@app.command()
def version():
    """Get the version of the package."""
    package_version = version(PKG_NAME)
    typer.echo(package_version)

# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":
    app()
