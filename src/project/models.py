from datetime import datetime

from sqlalchemy import Table, MetaData, Column, BigInteger, String, JSON, \
    TIMESTAMP, ForeignKey, Integer

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_data", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
