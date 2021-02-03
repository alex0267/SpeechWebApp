#!/bin/bash

alembic upgrade head
python -m ser_api.app
