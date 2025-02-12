from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import sys
from logger import get_logger
from exception import CustomException

logger = get_logger(__name__)

def evaluate_model(model, X, y):
    try:
        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)
        mae = mean_absolute_error(y, y_pred)
       

        logger.info(f"Evaluation Results: R²: {r2}, MAE: {mae}")
        print(f"R² Score: {r2*100}\nMAE: {mae}\n")

    except Exception as e:
        logger.error("Error evaluating model", exc_info=True)
        raise CustomException(e, sys)
