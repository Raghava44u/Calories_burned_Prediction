from data_load import load_data
from feature_engineering import preprocess_data
from model_training import train_model
from model_eval import evaluate_model
from visualization import plot_calories_distribution,BoxPlot,CountPlot,ScatterPlot

if __name__ == "__main__":
    df = load_data() 
    X, y, scaler = preprocess_data(df)  
    model = train_model(X, y) 
    evaluate_model(model, X, y) 
    plot_calories_distribution(df) 
    BoxPlot(df)
    CountPlot(df)
    ScatterPlot(df)
    
