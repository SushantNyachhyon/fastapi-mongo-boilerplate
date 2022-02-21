"""
commands for scafolding project structure
"""
import os
import re
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
        f.close()


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


def _response_content(name: str):
    content = f'"""\n{name} responses\n"""\n'
    content += 'from core.models import SchemaFactory\n\n\n'
    content += f'class {name.capitalize()}(SchemaFactory):\n'
    content += f'    """\n    {name} response class\n    """\n'
    return content


def _request_content(name: str):
    content = f'"""\n{name} requests\n"""\n'
    content += 'from core.models import BaseModel\n\n\n'
    content += f'class {name.capitalize()}(BaseModel):\n'
    content += f'    """\n    {name} request class\n    """\n'
    return content


def _repository_content(name: str):
    content = f'"""\n{name} repository\n"""\n'
    content += 'from abc import ABCMeta, abstractmethod\n\n'
    content += f'from .models import {name.capitalize()}\n\n\n'
    content += f'class {name.capitalize()}Abstract:\n'
    content += '    __metaclass__ = ABCMeta\n\n'
    content += '    @abstractmethod\n'
    content += f'    async def find_by_id(self, {name}_id: str):\n'
    content += '        pass\n\n\n'
    content += f'class {name.capitalize()}Repository({name.capitalize()}Abstract):\n'
    content += '    def __init__(self):\n'
    content += f'        self.model = {name.capitalize()}\n\n'
    content += f'    async def find_by_id(self, {name}_id: str):\n'
    content += '        pass\n'
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
    _write(f'{path}/requests.py', _request_content(name))
    _write(f'{path}/responses.py', _response_content(name))
    _write(f'{path}/controllers.py', _controller_content(name))
    _write(f'{path}/repository.py', _repository_content(name))
    typer.echo(typer.style('Module created', fg=typer.colors.GREEN))


@app.command()
def generatesecret():
    hex_key = _generate_hex()
    with open('.env', mode='r', encoding='utf-8') as f:
        with open('.env.temp', mode='w', encoding='utf-8') as temp:
            pattern = re.compile('APP_SECRET.+')
            for line in f.readlines():
                if pattern.match(line):
                    line = pattern.sub(f'APP_SECRET={hex_key}', line)
                temp.write(line)
            temp.close()
        f.close()
        os.rename('.env.temp', '.env')
    typer.echo(typer.style(hex_key, fg=typer.colors.GREEN))


@app.command()
def configapp(
    name: str = typer.Option(..., prompt=True),
    description: str = typer.Option(..., prompt=True),
    version: str = typer.Option(..., prompt=True)
):
    with open('.env', mode='r', encoding='utf-8') as f:
        with open('.env.temp', mode='w', encoding='utf-8') as temp:
            name_pattern = re.compile('APP_NAME.+')
            desc_pattern = re.compile('APP_DESCRIPTION.+')
            version_pattern = re.compile('APP_VERSION.+')
            for line in f.readlines():
                if name_pattern.match(line):
                    line = name_pattern.sub(f'APP_NAME={name}', line)
                if desc_pattern.match(line):
                    line = desc_pattern.sub(
                            f'APP_DESCRIPTION={description}',
                            line
                        )
                if version_pattern.match(line):
                    line = version_pattern.sub(
                            f'APP_VERSION={version}',
                            line
                        )
                temp.write(line)
            temp.close()
        f.close()
        os.rename('.env.temp', '.env')
    typer.echo(
        typer.style('App config set successfully', fg=typer.colors.GREEN)
    )


if __name__ == '__main__':
    app()
