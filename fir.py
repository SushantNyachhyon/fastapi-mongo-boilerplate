"""
commands for scafolding project structure
"""
import os
from secrets import token_hex
import typer

app = typer.Typer()


def _create_or_get_storage_path(path: str) -> None:
    try:
        os.makedirs(path)
    except OSError as ex:
        print(ex)


def _write(path: str, content: str) -> None:
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(content)


def _api_content(name: str):
    content = f'"""\n{name} routes\n"""\n'
    content += 'from fastapi import APIRouter\n'
    content += 'from . import controllers\n\n'
    content += '\n'
    content += f"route = APIRouter(prefix='/{name}')\n\n"
    content += "@route.get('')\n"
    content += 'async def index():\n'
    content += '    return await controller.index()\n'
    return content


def _model_content(name: str):
    content = f'"""\n{name} models\n"""\n'
    content += 'from core.models import DocumentFactory\n\n\n'
    content += f'class {name.capitalize()}(DocumentFactory):\n'
    content += f'    """\n    {name} document class\n    """\n'
    content += '\n'
    content += '    class Collection:\n'
    content += f"        name = '{name}es'\n"
    return content


def _schema_content(name: str):
    content = f'"""\n{name} schemas\n"""\n'
    content += 'from core.models import SchemaFactory\n\n\n'
    content += f'class {name.capitalize()}(SchemaFactory):\n'
    content += f'    """\n    {name} schema class\n    """\n'
    return content


def _controller_content(name: str):
    content = f'"""\n{name} controllers\n"""\n\n'
    content += 'async def index():\n'
    content += "    return {'name': 'controller'}\n"
    return content


def _generate_hex():
    return token_hex(32)


@app.command()
def createmodule(name: str):
    path = f'app/{name}'
    typer.echo(f'Creating module: {name}')
    _create_or_get_storage_path(path)
    _write(f'{path}/__init__.py', '')
    _write(f'{path}/apis.py', _api_content(name))
    _write(f'{path}/models.py', _model_content(name))
    _write(f'{path}/schemas.py', _schema_content(name))
    _write(f'{path}/controllers.py', _controller_content(name))
    typer.echo(typer.style('Module created', fg=typer.colors.GREEN))


@app.command()
def gensecret():
    typer.echo(typer.style(_generate_hex(), fg=typer.colors.GREEN))


if __name__ == '__main__':
    app()
