from peewee import (
    CharField,
    TextField,
    ForeignKeyField,
    DateTimeField,
    BooleanField,
    FloatField,
    IntegerField,
)
from core.db import BaseModel, db


class Problem(BaseModel):
    """
    Model for problem
    """

    name = CharField(max_length=256)
    url = CharField(max_length=256)
    difficulty = FloatField()
    statement = TextField()


class Tag(BaseModel):
    """
    Tag for problem
    """

    problem = ForeignKeyField(Problem, backref="tags")
    name = CharField(max_length=64)


class Thread(BaseModel):
    """
    Thread object
    Represents chat with AI bot
    """

    date = DateTimeField()
    is_manual = BooleanField()
    is_solved = BooleanField()


class Submission(BaseModel):
    """
    Submission object
    Represents request and response to AI
    and info about submission
    """

    thread = ForeignKeyField(Thread, backref="submissions")
    message = TextField()
    response = TextField()

    is_passed = BooleanField()
    has_runtime_error = BooleanField()
    pass_percentage = FloatField()


db.create_tables([Problem, Tag, Thread, Submission])
