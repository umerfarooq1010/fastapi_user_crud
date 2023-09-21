from email.policy import default
from sqlalchemy.sql import func
import sqlalchemy
from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Table,
    DateTime,
    Boolean,
)


from core.database import schema

metadata = sqlalchemy.MetaData(schema=schema)

User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("first_name", String(255), nullable=True),
    Column("last_name", String(255), nullable=True),
    Column("contact", String(127), nullable=True, default=None),
    Column("email", String(255), unique=True, nullable=True),
    Column("username", String(255), unique=True, nullable=True),
    Column("active", Boolean, nullable=True, default=False),
    Column("password", String(255), nullable=True),
    Column("company_name", String(255), nullable=True, default=None),
    Column("address", String(511), nullable=True, default=None),
    Column("city", String(127), nullable=True, default=None),
    Column("country", String(127), nullable=True, default=None),
    Column("postal_code", String(255), nullable=True, default=None),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)

Product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("name", String(255), nullable=False,unique=True),
    Column("description", String(255), nullable=True),
    Column("price", Integer, nullable=True, default=None),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)