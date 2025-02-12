from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, KFold
import sys
import os
from logger import get_logger
from exception import CustomException
import joblib

logger = get_logger(__name__)

def train_model(X, y):
   
    try:
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)

        cv_scores = cross_val_score(model, X, y, cv=kf, scoring="r2")
        logger.info(f"Cross-Validation R2 Scores: {cv_scores}")
        logger.info(f"Mean R2 Score: {cv_scores.mean()}")

        model.fit(X, y) 
        logger.info("Model training completed.")
        model_path = "models/calories_model.pkl"
        model_dir = os.path.dirname(model_path) 
        if not os.path.exists(model_dir):
              os.makedirs(model_dir, exist_ok=True) 
              joblib.dump(model, model_path) 
              logger.info(f"Model saved at {model_path}")

      
        return model

    except Exception as e:
        logger.error("Error training model", exc_info=True)
        raise CustomException(e, sys)
