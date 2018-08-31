import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    '''Establish a connection to the database if database not in g
    else, return the db.

    This avoids unecessary connections and reuses connections
    '''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'], # Database path
            detect_types=sqlite3.PARSE_DECLTYPES # Parses declared types from the schema file
        )
        g.db.row_factory = sqlite3.Row # Rows behave as dictionaries

    return g.db


def close_db(e=None):
    '''Remove the database from g'''
    db = g.pop('db', None) # Returns None if no db is popped

    if db is not None:
        db.close()



def init_db():
    '''Clear/restart the database by rerunning the schema.sql file'''
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# # Give a name to the CLI command
# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     '''Create the command line command to create the database
#     by running the schema.sql file
#     '''
#     init_db()
#     click.echo('Initialized the database.')


# def init_app(app):
#     '''Add the init-db command to CLI and add close_db() to teardown context '''
#     app.teardown_appcontext(close_db) # Always does this before sending off the request
#     app.cli.add_command(init_db_command) # Adds your command line interface (CLI) 
