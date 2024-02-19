# #Configiuration for MongoDB 

# import pymongo
# import os
# from sensor.constant.database import DATABASE_NAME
# from sensor.constant.env_variable import MONGODB_URL_KEY
# # from urllib.parse import quote_plus
# import certifi


# ca = certifi.where()

# class MongoDBClient:
#     client = None
# #     client = pymongo.MongoClient(
# #     # "mongodb://localhost:27017/?ssl=true&ssl_certfile=path/to/certificate.pem"
# # )

#     def __init__(self, database_name = DATABASE_NAME) -> None:
#         try:
#             if MongoDBClient.client is None:
#                 # mongo_db_url = os.getenv(MONGODB_URL_KEY)


#                 # username = "gulhanerasika"
#                 # password = "h2kEouS6X0BHhZGe"
#                 mongo_db_url = "mongodb+srv://gulhanerasika:h2kEouS6X0BHhZGe@cluster0.yk2gnsm.mongodb.net/?retryWrites=true&w=majority".format(quote_plus(username), quote_plus(password))

#                 MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
#             self.client = MongoDBClient.client
#             self.database = self.client[database_name]
#             self.database_name = database_name
#         except Exception as e:
#             raise e


# import pymongo
# import os
# from sensor.constant.database import DATABASE_NAME
# from sensor.constant.env_variable import MONGODB_URL_KEY
# import certifi

# ca = certifi.where()

# class MongoDBClient:
#     client = pymongo.MongoClient(
#         "mongodb://localhost:27017/?ssl=true&ssl_ca_certs=path/to/certificate.pem"
#     )

#     def __init__(self, database_name=DATABASE_NAME) -> None:
#         try:
#             if MongoDBClient.client is None:
#                 mongo_db_url = os.getenv(MONGODB_URL_KEY)
#                 MongoDBClient.client = pymongo.MongoClient(
#                     mongo_db_url, tlsCAFile=ca
#                 )
#             self.client = MongoDBClient.client
#             self.database = self.client[database_name]
#             self.database_name = database_name
#         except Exception as e:
#             raise e




import pymongo
import os
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
from urllib.parse import quote_plus
import certifi

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if not mongo_db_url:
                    # If the environment variable is not set, you can set the connection string directly
                    username = "gulhanerasika"
                    password = "h2kEouS6X0BHhZGe"
                    mongo_db_url = f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@cluster0.yk2gnsm.mongodb.net/?retryWrites=true&w=majority"

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e



