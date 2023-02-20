# coding: utf-8

from generator.metaprog.types import Void
from generator.metaprog.singleton import Singleton
from generator.config.rules.dev.database import DB as DATABASE_CONFIG
import generator.config.builders.database as database_config_builder

import pymongo
from pymongo.collection import Collection as DatabaseCollection
from typing import Optional


class Database(metaclass=Singleton):
    def __init__(self):
        def build_config(self) -> Void:
            database_config_builder.append_dynamic_conf(DATABASE_CONFIG)
            print(DATABASE_CONFIG)

        def index_database(self) -> Void:
            db_table: DatabaseCollection = self._get_db_table()
            db_table.create_index([ ("phone_number", pymongo.ASCENDING) ])

        def initialize(self) -> Void:
            build_config(self)
            self._disabled_persistence = DATABASE_CONFIG["DISABLE_PERSISTENCE"]
            self._mongo_client = pymongo.MongoClient(DATABASE_CONFIG["MONGO_DB_CONNECTION_URI"])
            self._db_name_key = DATABASE_CONFIG["MONGO_DB_NAME"]
            self._db = self._mongo_client[self._db_name_key]
            self._db_table_key = DATABASE_CONFIG["MONGO_DB_TABLE"]
            index_database(self)

        initialize(self)


    @staticmethod
    def _retrieve_last_saved_phone_operator_code(entry: dict) -> str:
        data: str = entry["operator_code"]
        return data


    @staticmethod
    def _retrieve_last_saved_phone_country_code(entry: dict) -> str:
        data: str = entry["country_code"]
        return data


    @staticmethod
    def _retrieve_last_saved_phone_number_suffix(entry: dict) -> str:
        data: str = entry["generated_suffix"]
        return data


    @staticmethod
    def is_finite_collection(data: dict) -> bool:
        for key in data:
            if data[key] != "-1":
                return False
        return True


    def _get_db_table(self) -> DatabaseCollection:
        db_table_key: str = self._db_table_key
        db_table: DatabaseCollection = self._db[db_table_key]
        return db_table


    def _retrieve_last_saved_phone_number_entry(self) -> Optional[dict]:
        db_table: DatabaseCollection = self._get_db_table()

        try:
            last_saved_phone_number_entry: dict = db_table.find_one(
                sort=[("_id", pymongo.DESCENDING)])
            return last_saved_phone_number_entry
        except:
            return None


    def save_phone_number(self, phone_number: str, country_code: str, operator_code: str, phone_number_suffix: str) -> Void:
        if self._disabled_persistence:
            return

        db_table: DatabaseCollection = self._get_db_table()
        database_entry: dict = {
            "phone_number": phone_number,
            "country_code": country_code,
            "operator_code": operator_code,
            "generated_suffix": phone_number_suffix
        }

        db_table.update_one({"phone_number": phone_number}, {
                            "$set": database_entry}, upsert=True)


    def retrieve_last_saved_phone_metadatas(self) -> Optional[dict]:
        if self._disabled_persistence:
            return None
        entry: Optional[dict] = self._retrieve_last_saved_phone_number_entry()
        if entry is None:
            return None
        metadatas: dict = {}
        metadatas["phone_number_suffix"] = self._retrieve_last_saved_phone_number_suffix(entry)
        metadatas["phone_number_country_code"] = self._retrieve_last_saved_phone_country_code(entry)
        metadatas["phone_number_operator_code"] = self._retrieve_last_saved_phone_operator_code(entry)
        return metadatas


    def append_finite_collection_indicator(self) -> Void:
        self.save_phone_number("-1", "-1", "-1", "-1")
