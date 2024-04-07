"""Database"""

from peewee import *

# SQLite database using WAL journal mode and 64MB cache.
db = SqliteDatabase('analyzer.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class BaseModel(Model):
    """Car entity"""

    class Meta:
        """Settings of model"""
        database = db

