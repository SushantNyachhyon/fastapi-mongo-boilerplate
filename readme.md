# Fastapi and Mongodb boilerplate

Boilerplate for fastapi and mongodb with amazing scafolding commandline tool


## Features

* enterprise folder structure
* repository pattern for database logic
* amazing commandline tool for project scafolding
* google based linting with YAPF formatting


## Technology

* uvicorn
* fastapi
* motor
* beanie
* typer
* aiofiles
* pylint
* pytest


## Project setup

* python3 -m venv venv
* source /venv/bin/activate
* pip install --upgrade pip
* pip install -r dependencies.txt
* cp .env.example .env
* python fir.py generatesecret
* python main.py

remember to set mongo connection string and db name in the env
