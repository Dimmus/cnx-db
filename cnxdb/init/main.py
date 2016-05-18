# -*- coding: utf-8 -*-
import os
import logging
import sys
import warnings

import psycopg2

from .manifest import get_schema


here = os.path.abspath(os.path.dirname(__file__))
SCHEMA_DIR = os.path.join(here, '..', 'schema')

logger = logging.getLogger('cnxdb')


def init_db(connection_string, as_venv_importable=False):
    """Initialize the database from the given ``connection_string``."""
    with psycopg2.connect(connection_string) as db_connection:
        with db_connection.cursor() as cursor:
            for schema_part in get_schema(SCHEMA_DIR):
                cursor.execute(schema_part)
    if as_venv_importable:
        init_venv(connection_string)


def init_venv(connection_string):
    """Initialize a Python virtual environment for trigger importation."""
    pass


__all__ = (
    'init_db',
    'init_venv',
)
