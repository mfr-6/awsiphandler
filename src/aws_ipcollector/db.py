import os
from src.aws_ipcollector.models import MODELS, Prefix
from peewee import SqliteDatabase, Model
from progress.bar import Bar

class DbHandler:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.db = self.get_database()

    def __get_declared_models(self):
        return MODELS

    def __initialize(self, db: SqliteDatabase) -> None:
        db.create_tables(self.__get_declared_models())

    def get_database(self) -> SqliteDatabase:
        db = SqliteDatabase(self.db_path)
        db.bind(self.__get_declared_models())

        if not os.path.exists(self.db_path):
            self.__initialize(db)
    
        return db
        
    def bulk_insert(self, model: Model, rows: list[dict]) -> None:
        with self.db.atomic():
            with Bar(f"Bulk Insert, Model: {model.__name__}...", max=len(rows)) as bar:
                for row in rows:
                    model.create(**row)
                    bar.next()
    
    def purge_table(self, model: Model) -> int:
        query = model.delete()
        return query.execute()
    
    def get_prefixes(self) -> list[Prefix]:
        return Prefix.select()
    
    def get_prefixes_by_region(self, region_name: str) -> list[Prefix]:
        return Prefix.select().where(Prefix.region == region_name)

