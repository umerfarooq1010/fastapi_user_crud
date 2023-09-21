import math
from datetime import datetime, date
from typing import Union
from pydantic import BaseModel,field_validator
import re
from passlib.hash import pbkdf2_sha256


def check_email(value: str):
    email_regex = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    if not email_regex.match(value):
        raise ValueError("Invalid email address.")
    else:
        return True

def has_special_char(value: str):
    special_char_regex = re.compile(r"[^a-zA-Z0-9]")
    return special_char_regex.search(value) is not None



class UserEmailSchema(BaseModel):
    email: str

    @field_validator("email")
    def check_email(v: str):
        if check_email(v):
            return v.lower()


class UserCreateSchema(UserEmailSchema):
    first_name: str
    last_name: str
    username: str
    password: str
    contact: Union[str, None] = None
    active: Union[bool, None] = None
    company_name: Union[str, None] = None
    address: Union[str, None] = None
    city: Union[str, None] = None
    country: Union[str, None] = None
    postal_code: Union[str, None] = None

    @field_validator("password")
    def password_hash(cls, v: str):
        if len(v) < 8:
            raise ValueError(
                "Password must have at least one (digit, upper case, lower case, special character) & min 8 in length"
            )
        if len(v) > 20:
            raise ValueError(
                "Password must have at least one (digit, upper case, lower case, special character) & min 8 in length"
            )
        if not any(char.isdigit() for char in v):
            raise ValueError(
                "Password must have at least one (digit, upper case, lower case, special character) & min 8 in length"
            )
        if not any(char.isupper() for char in v):
            raise ValueError(
                "Password must have at least one (digit, upper case, lower case, special character) & min 8 in length"
            )
        if not any(char.islower() for char in v):
            raise ValueError(
                "Password must have at least one (digit, upper case, lower case, special character) & min 8 in length"
            )
        if not has_special_char(v):
            raise ValueError(
                "Password must have at least one (digit, upper case, lower case, special character) & min 8 in length"
            )
        return pbkdf2_sha256.hash(v)


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    contact: Union[str, None] = None
    active: Union[bool, None] = None
    company_name: Union[str, None] = None
    address: Union[str, None] = None
    city: Union[str, None] = None
    country: Union[str, None] = None
    postal_code: Union[str, None] = None

class UserSchemaUpdate(BaseModel):
    first_name: str
    # last_name: str
    # contact: str
    # active: bool
    # company_name: str
    # address: str
    # city: str
    # country:  str
    # postal_code: str




class SchemaCreateItem(BaseModel):
    name: str
    description: str
    price: int

class SchemaAllItems(SchemaCreateItem):
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

