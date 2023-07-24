from streamlit.connections import ExperimentalBaseConnection
from pymongo import MongoClient
import pandas as pd

class MongoDBConnection(ExperimentalBaseConnection[MongoClient]):
    def __init__(self, connection_name: str, **kwargs) -> None:
        super().__init__(connection_name, **kwargs)

    def _connect(self, **kwargs) -> MongoClient:
        if 'mongo_uri' in kwargs:
            mongo_uri = kwargs.pop('mongo_uri')
        else:
            mongo_uri = self._secrets['mongo_uri']

        return MongoClient(mongo_uri, **kwargs)

    def connection(self) -> MongoClient:
        return self._instance

    def insert_document(self, collection_name: str, document: dict):
        connection = self.connection()
        collection = connection.get_database()[collection_name]
        collection.insert_one(document)

    def update_document(self, collection_name: str, document_id: str, update_data: dict):
        connection = self.connection()
        collection = connection.get_database()[collection_name]
        filter_query = {"_id": document_id}
        update_query = {"$set": update_data}
        collection.update_one(filter_query, update_query)

    def delete_document(self, collection_name: str, document_id: str):
        connection = self.connection()
        collection = connection.get_database()[collection_name]
        collection.delete_one({"_id": document_id})

    def get_all_documents(self, collection_name: str) -> pd.DataFrame:
        connection = self.connection()
        collection = connection.get_database()[collection_name]
        cursor = collection.find({})
        df = pd.DataFrame(list(cursor))
        return df
