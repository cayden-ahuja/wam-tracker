import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Signs session cookie + csrf tokens on forms... real apps load this from env
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-only-change')
    # SQLite db file in project root (gitignored)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')