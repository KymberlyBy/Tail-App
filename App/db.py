from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()

def migrateApp(app):
    return Migrate(app, db)

def create_database():
    db.create_all()

#def init_database():
 #   db.init_app(app)


"""
import sqlite3

import click
from flask import current_app, temp

def get_db():
    if 'db' not in temp:
        temp.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        temp.db.row_factory = sqlite3.Row()
    return temp.db


def close_db(e=None):
    db = temp.pop ('db', None)

    if fb is not None:
        db.close()


def init_db():
    db = get_db();

    with current_app.open_resource('schema.sql') as temp:
        db.executescript(temp.read().decode('utf-8'))

@click.command('init-db')
def initi_db_command():
    init_db()
    click.echo('Database initialized')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    """