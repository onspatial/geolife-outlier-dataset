# utils/mongo.py
# index database by Latitude and Longitude
def indexWithLatLong(mongoURI, dataBaseName, collectionName):
    from pymongo import MongoClient
    try:
        client = MongoClient(mongoURI)
        database = client[dataBaseName]
        collection = database[collectionName]
        collection.create_index([('Latitude', 1), ('Longitude', 1)])
    except Exception as e:
        print('mongo.indexWithLatLong: ', e)
    finally:
        client.close()


def saveMany(mongoURI, dataBaseName, collectionName, dataList):
    from pymongo import MongoClient
    try:
        client = MongoClient(mongoURI)
        database = client[dataBaseName]
        collection = database[collectionName]
        collection.insert_many(dataList)
    except Exception as e:
        print('mongo.saveMany: ', e)
    finally:
        client.close()


def saveOne(mongoURI, dataBaseName, collectionName, geoJSON):
    from pymongo import MongoClient
    try:
        client = MongoClient(mongoURI)
        database = client[dataBaseName]
        collection = database[collectionName]
        collection.insert_one(geoJSON)
    except Exception as e:
        print('mongo.saveOne: ', e)
    finally:
        client.close()


def deleteAll(mongoURI, dataBaseName, collectionName):
    from pymongo import MongoClient
    try:
        client = MongoClient(mongoURI)
        database = client[dataBaseName]
        collection = database[collectionName]
        # collection.delete_many()
    except Exception as e:
        print('mongo.deleteAll: ', e)
    finally:
        client.close()


def getAllData(mongoURI, dataBaseName, collectionName):
    from pymongo import MongoClient
    try:
        client = MongoClient(mongoURI)
        database = client[dataBaseName]
        collection = database[collectionName]
        data = collection.find({})
        print('mongo.getAllData: ', data)
        return list(data)
    except Exception as e:
        print('mongo.getAllData: ', e)
    finally:
        client.close()


def getByCoordinate(mongoURI, dataBaseName, collectionName, Latitude, Longitude):
    from pymongo import MongoClient
    try:
        client = MongoClient(mongoURI)
        database = client[dataBaseName]
        collection = database[collectionName]
        return collection.find_one({'Latitude': Latitude, 'Longitude': Longitude})
    except Exception as e:
        print('mongo.get_by_id: ', e)
    finally:
        client.close()
