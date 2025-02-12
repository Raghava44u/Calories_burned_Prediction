from sklearn.preprocessing import LabelEncoder, StandardScaler
import sys
from logger import get_logger
from exception import CustomException

logger = get_logger(__name__)

def preprocess_data(df):
    try:
        df["Gender"] = LabelEncoder().fit_transform(df["Gender"])

        X = df.drop(columns=["User_ID", "Calories"])
        y = df["Calories"]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        logger.info("Data preprocessing completed.")
        return X_scaled, y, scaler

    except Exception as e:
        logger.error("Error in preprocessing data", exc_info=True)
        raise CustomException(e, sys)
