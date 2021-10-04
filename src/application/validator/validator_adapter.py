from schema import Schema


def validator_adapter(data: dict, schema: Schema) -> Exception:
    try:
        schema.validate(data._asdict())
        return None
    except Exception as e:
        return e
