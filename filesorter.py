"""
Copyright 2024 Filinious Inc

DESCRIPTION:
    A script to list and sort files by size in a folder

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

# Rich print for better formatting - https://rich.readthedocs.io/
from rich import print

# Additional import for file system operations
import os

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "filesorter"

# ::CORE LOGIC --------------------------------------------------------------------- #
def list_files(ignore_exts=[]):
    files = []
    for entry in os.scandir('.'):
        if entry.is_file() and not any(entry.name.endswith(ext) for ext in ignore_exts):
            files.append((entry.name, os.path.getsize(entry.path)))
    return sorted(files, key=lambda x: x[1])

# ::CLI COMMANDS ------------------------------------------------------------------- #
@app.command()
def show():
    """Asks the user if any file extensions should be ignored, then lists files in the current folder with their file size and sorts them by size."""
    extensions = typer.prompt("Enter file extensions to ignore, separated by commas (e.g., .jpg,.png)").split(',')
    files = list_files(extensions)
    for file, size in files:
        print(f"{file}: {size} bytes")

# ::DEFAULT CLI COMMANDS ----------------------------------------------------------- #
@app.command()
def version():
    """Get the version of the package."""
    package_version = version(PKG_NAME)
    typer.echo(package_version)

# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":
    app()