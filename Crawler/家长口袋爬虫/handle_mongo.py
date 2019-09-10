from pymongo import MongoClient

__all__ = ['ConnectMongo']


class ConnectMongo:
    collection_name = 'test_mongo'
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DATABASE = "test"

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['ParentChart']

    def add_one(self, db_name, data):
        ''' 新增数据 '''
        return self.db[db_name].insert_one(data)
