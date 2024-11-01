from peewee import Model, CharField

class Prefix(Model):
    ip_prefix = CharField()
    region = CharField()
    service = CharField()
    network_border_group = CharField()

MODELS = [
    Prefix
]