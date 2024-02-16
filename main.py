from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.data_access.sensor_data import SensorData
from sensor.components.data_ingestion import DataIngestion
import sys


     
if __name__ == '__main__':
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    # sesnor_data = SensorData()
    # dataframe = sesnor_data.export_collection_as_dataframe(collection_name = 'car')

   

   

  