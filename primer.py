"""
Copyright 2024 Robby

DESCRIPTION:
    A script to calculate and list prime numbers

INSTALL:
    pip install typer rich

USAGE EXAMPLE:
    > python primer.py calc 10

LICENSE:
    MIT License
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

# Rich print for better formatting - https://rich.readthed.com/
from rich import print
from rich.console import Console

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "primer"

# ::CORE LOGIC --------------------------------------------------------------------- #
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# ::CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def calc(n: int):
    """ Calculate n number of prime numbers then print them all out """
    console = Console()
    with console.status(f"[green4] Calculating prime numbers... [/green4]", spinner="dots") as status:
        primes = calculate_primes(n)
        console.print(f"First {n} prime numbers:", style="bold green")
        print(primes)

@app.command()
def version():
    """ get the version of the package """
    package_version = version(PKG_NAME)
    typer.echo(package_version)

# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":  # ensure importing the script will not execute
    app()