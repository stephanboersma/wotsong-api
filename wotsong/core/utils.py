import base64
import re
from typing import Type
from marshmallow import Schema

def snake_to_camel(target):
    return {re.sub(r'_([a-z])', lambda x: x.group(1).upper(), key): target[key] for key in target}

def camel_to_snake(target):
    return {re.sub(r'[A-Z]', lambda x: '_' + x.group(0).lower(), key): target[key] for key in target}

def validate_schema(schema: Type[Schema], payload: dict):
    errors = schema.validate(schema(),payload)
    if errors:
        raise AssertionError(str(errors))

def base64_encode(text: str) -> str:
    bytes = text.encode("ascii")
    base64_bytes = base64.b64encode(bytes)
    return base64_bytes.decode("ascii")