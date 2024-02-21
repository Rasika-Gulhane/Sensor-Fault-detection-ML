from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.data_access.sensor_data import SensorData
from sensor.components.data_ingestion import DataIngestion
from sensor.utils.main_utils import read_yaml_file
# from sensor.
import os,sys


env_file_path=os.path.join(os.getcwd(),"env.yaml")

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


# app = FastAPI()
# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

     
if __name__ == '__main__':
    try:
        # env_file_path = "/Users/rasikagulhane/Desktop/Sensor-Fault-detection-ML/env.yaml"
        # set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    # sesnor_data = SensorData()
    # dataframe = sesnor_data.export_collection_as_dataframe(collection_name = 'car')

    except Exception as e:
        logging.exception(e)
   

   

  