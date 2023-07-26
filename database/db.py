#!/usr/bin/python
from config import config
from sqlalchemy import create_engine


def create_db_engine():
    params = config()

    CONN_STRING = (
        f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    )
    return create_engine(CONN_STRING)
