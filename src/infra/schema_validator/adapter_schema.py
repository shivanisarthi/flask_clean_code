from schema import Schema
from src.application.validator import Validator


class SchemaAdapter(Validator):
    schema: Schema

    def __init__(self, schema) -> None:
        super().__init__()
        self.schema = schema

    def validate(self, data):
        try:
            self.schema.validate(data._asdict())
            return None
        except Exception as e:
            return e
