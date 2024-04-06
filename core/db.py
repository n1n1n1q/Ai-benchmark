"""Database"""

from peewee import *

# SQLite database using WAL journal mode and 64MB cache.
sqlite_db = SqliteDatabase(
    "parser.db", pragmas={"journal_mode": "wal", "cache_size": -1024 * 64}
)


class Car(Model):
    """Car entity"""

    class Meta:
        """Settings of model"""

        database = sqlite_db

    price = IntegerField(null=True)
    seller_name = CharField(max_length=256, null=True)
    car_name = CharField(max_length=256, null=True)
    engine = CharField(max_length=256)

    def __str__(self) -> str:
        """Return string representation of Car"""
        return f"Car(car_name={self.car_name}, seller={self.seller_name}, price={self.price}, \
engine={self.engine})"


sqlite_db.create_tables([Car])
