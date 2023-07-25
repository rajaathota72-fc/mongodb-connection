from streamlit.connections import ExperimentalBaseConnection
from pymongo import MongoClient
import pandas as pd
import certifi
class MongoDBConnection(ExperimentalBaseConnection[MongoClient]):
    def __init__(self, connection_name: str, **kwargs) -> None:
        super().__init__(connection_name, **kwargs)

    def _connect(self, **kwargs) -> MongoClient:
        if 'mongo_uri' in kwargs:
            mongo_uri = kwargs.pop('mongo_uri')
        else:
            mongo_uri = self._secrets['mongo_uri']

        return MongoClient(mongo_uri, tlsCAFile=certifi.where(),**kwargs)

    def connection(self) -> MongoClient:
        return self._instance

    def find_document(self, db_name: str,collection_name: str, document_id: str):
        connection = self.connection()
        database = connection[db_name]
        collection = database[collection_name]
        collection.find_one({'_id':document_id})

    def insert_document(self, db_name: str,collection_name: str, document: dict):
        connection = self.connection()
        database = connection[db_name]
        collection = database[collection_name]
        collection.insert_one(document)

    def update_document(self, db_name: str, collection_name: str, document_id: str, update_data: dict):
        connection = self.connection()
        database = connection[db_name]
        collection = database[collection_name]
        filter_query = {"_id": document_id}
        update_query = {"$set": update_data}
        collection.update_one(filter_query, update_query)

    def delete_document(self, db_name: str, collection_name: str, document_id: str):
        connection = self.connection()
        database = connection[db_name]
        collection = database[collection_name]
        collection.delete_one({"_id": document_id})

    def get_all_documents(self, db_name: str, collection_name: str) -> pd.DataFrame:
        connection = self.connection()
        database = connection[db_name]
        collection = database[collection_name]
        cursor = [i for i in collection.find({})]
        df = pd.DataFrame.from_dict(list(cursor),orient='columns')
        return df
