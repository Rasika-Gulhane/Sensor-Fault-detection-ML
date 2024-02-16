#Sensor data that collect sensor data from Mongo DB and clean it and return as Data Frame
# This can help to give easy access of DF to another files

import numpy as np
import pandas as pd
import json
from sensor.logger import logging
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException
import sys
from typing import Optional


class SensorData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            logging.info("connection start for mongoDB in sensor data")
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            logging.info("connection success for mongoDB")

        except Exception as e:
            raise SensorException(e, sys)
        
    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)
            logging.info("success sensor data")

            return df
        
        

        except Exception as e:
            raise SensorException(e, sys)