from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np
from us_visa.logger import logger



class USvisaData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=DATABASE_NAME)->pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """

            collection = self.mongo_client.database[collection_name]
            # logger.info(f"{collection = }")

            df = pd.DataFrame(list(collection.find()))
            # logger.info(f"{df.head()}")
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e,sys)
        


# usvisa_data = USvisaData()
# dataframe = usvisa_data.export_collection_as_dataframe(collection_name="visa_data")
# logger.info(f"Shape of dataframe: {dataframe.shape}")