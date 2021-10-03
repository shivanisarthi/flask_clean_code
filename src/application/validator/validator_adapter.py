from schema import Schema


def validator_adapter(input: dict, schema: Schema) -> Exception:
    try:
        schema.validate(input._asdict())
        return None
    except Exception as e:
        return e
