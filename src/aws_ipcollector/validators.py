from peewee import Model

def list_contains_models(rows: list) -> bool:
    return any([ isinstance(row, Model) for row in rows ])

def list_contains_models_of_single_type(rows):
    return all([ isinstance(row, type(rows[0])) for row in rows ])