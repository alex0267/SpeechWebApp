#!/bin/bash

alembic upgrade head
python -m api.app
