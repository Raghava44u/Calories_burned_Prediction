import pandas as pd
import sys
from exception import CustomException
from logger import get_logger

logger = get_logger(__name__)

def load_data():
    """Loads and merges datasets."""
    try:
        data1 = pd.read_csv("notebook/calories.csv")
        data2 = pd.read_csv("notebook/exercise.csv")

        data1.columns = data1.columns.str.strip()
        data2.columns = data2.columns.str.strip()

        if "User_ID" not in data1.columns or "User_ID" not in data2.columns:
            raise ValueError("'User_ID' column is missing in one of the datasets!")

        df = pd.merge(data2, data1, on="User_ID", how="left")
        logger.info(" Data successfully loaded and merged.")

        return df

    except Exception as e:
        logger.error("Error loading data", exc_info=True)
        raise CustomException(e, sys)
