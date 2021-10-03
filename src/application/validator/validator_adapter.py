from schema import Schema


def validator_adapter(data: dict, schema: Schema) -> Exception:
    try:
        schema.validate(data)
        return None
    except Exception as e:
        return e
