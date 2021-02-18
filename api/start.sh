#!/bin/bash

alembic upgrade head
python make_credentials.py
python -m ser_api.app
