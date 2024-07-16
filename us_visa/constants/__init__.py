import os
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

# MONGODB_URL_KEY = "MONGODB_URL"

home_dir = Path(__file__).parent.parent.parent
env_filepath = home_dir / ".env"

load_dotenv(env_filepath)

MONGODB_URL_KEY = os.environ.get("MONGODB_URL")

PIPELINE_NAME = "usvisa"
ARTIFACT_DIR = "artifact"

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

MODEL_FILE_NAME = "model.pkl"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = COLLECTION_NAME
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2