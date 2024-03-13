from flask import g, current_app
from db import DB


def get_db():
    if 'db' not in g:
        g.db = DB()
    return g.db


@current_app.teardown_appcontext
def close_db(error):
    if error:
        current_app.logger.exception(error)
    db = g.pop('db', None)
    if db is not None:
        db.cur.close()
        db.conn.close()
