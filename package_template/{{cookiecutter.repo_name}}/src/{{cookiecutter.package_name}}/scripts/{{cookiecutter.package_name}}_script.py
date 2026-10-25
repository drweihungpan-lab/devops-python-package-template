"""CLI script for the {{cookiecutter.package_name}} package. This will be called on the command line"""

import click

from {{cookiecutter.package_name}}.{{cookiecutter.module_name}} import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def {{cookiecutter.package_name}}_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
