"""
Copyright 2024 Robby

DESCRIPTION:
    A Python script to simulate boid flocking using Pygame

INSTALL:
    pip install typer pygame numpy pandas rich

USAGE EXAMPLE:
    > python boid_simulation.py launch_sim --boids 100 --boid_speed 2.5

LICENSE:
    This is free and unencumbered software released into the public domain.

    Anyone is free to copy, modify, publish, use, compile, sell, or
    distribute this software, either in source code form or as a compiled
    binary, for any purpose, commercial or non-commercial, and by any
    means.
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

# Game programming framework - https://www.pygame.org/
import pygame

# Powerful data structures for data analysis - https://pandas.pydata.org/
import pandas as pd

# Numerical operations - https://numpy.org/
import numpy as np

# Rich print for better formatting - https://rich.readthed.com/
from rich import print

# ::SETUP -------------------------------------------------------------------------- #
app = typer.Typer(
    add_completion=False, 
    no_args_is_help=True,
)

# ::GLOBALS --------------------------------------------------------------------- #
PKG_NAME = "boid_simulation"

# ::CORE LOGIC --------------------------------------------------------------------- #
class Boid:
    def __init__(self, x, y, vx, vy):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy

    def update(self, boids, speed, width, height):
        # Implement alignment, cohesion, and separation rules here
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 2)

def create_boid(width: int, height: int):
    # Create and return a Boid object at a random position
    pass

def run_simulation(boids: int, boid_speed: float):
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    boid_list = [create_boid(width, height) for _ in range(boids)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for boid in boid_list:
            boid.update(boid_list, boid_speed, width, height)
            boid.draw(screen)

        pygame.display.flip()
        pygame.time.delay(10)

    pygame.quit()

# ::CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def launch_sim(boids: int = typer.Argument(..., help="Number of boids in the simulation"),
               boid_speed: float = typer.Argument(..., help="Speed of each boid")):
    """ Run the boid flocking simulation """
    run_simulation(boids, boid_speed)

# ::DEFAULT CLI COMMANDS ---------------------------------------------------------------------------- #
@app.command()
def version():
    """ Get the version of the package """
    package_version = version(PKG_NAME)
    typer.echo(package_version)

# ::EXECUTE ------------------------------------------------------------------------ #
if __name__ == "__main__":
    app()