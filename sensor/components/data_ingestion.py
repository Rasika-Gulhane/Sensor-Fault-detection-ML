from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.config_entity import DataIngestionConfig
from sensor.data_access.sensor_data import SensorData
import os, sys
from pandas import DataFrame

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config= data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
    
    def export_data_into_feature_store(self)-> DataFrame:
        # 'Export MongoDB collection records as DFrame in feature store'
        
        try:
            logging.info("export data from mongoDB into feature store")
            sesnor_data = SensorData()
            dataframe = sesnor_data.export_collection_as_dataframe(collection_name = self.data_ingestion_config.collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # create folder to store feature store
            dir_path = os.path.dirname(feature_store_file_path)
            os.mkdir(dir_path, exist_ok = True)

            dataframe.to_csv(feature_store_file_path, index= False, header= True)  
            return dataframe

        except Exception as e:
            raise SensorException(e,sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        pass
      
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("start initiate data ingestion")
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            logging.info("mid initiate data ingestion")
            data_ingestion_artifact= DataIngestionArtifact(trained_file_path = self.data_ingestion_config.training_file_path, 
            test_file_path = self.data_ingestion_config.testing_file_path)
            logging.info("mid (artifact stage) initiate data ingestion")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        

       