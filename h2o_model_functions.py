import h2o
import pandas as pd
from sklearn.metrics import r2_score
import streamlit as st

# In your h2o_model_functions.py
def load_h2o_model(model_path):
    # Initialize H2O (only once)
    h2o.init()

    # Load the H2O model
    loaded_model = h2o.load_model(model_path)

    return loaded_model

model_path = 'C:/Users/Marco\Desktop/IronHack/projects/final_project/StackedEnsemble_AllModels_1_AutoML_1_20231206_103316'
loaded_model = load_h2o_model(model_path)


# Function to make predictions
def make_predictions(loaded_model, input_data):
    # Convert input data to H2OFrame
    h2o_df = h2o.H2OFrame(input_data)

    # Make predictions
    predictions = loaded_model.predict(h2o_df)
    predictions_df = predictions.as_data_frame()
    prediction_values = predictions_df['predict'].values

    return prediction_values

# Example usage in Streamlit
if __name__ == "__main__":
    # Load the H2O model
    loaded_model = load_h2o_model()

    # Load your input data (replace this with your actual data loading logic)
    df_ready = pd.read_csv('path/to/your/data.csv')

    # Example: Input data for prediction
    input_data = {
        'Feature 1': 25,
        'Feature 2': 30,
        'Feature 3': 'District A',
        # Add more features here
    }

    # Make predictions
    predictions = make_predictions(loaded_model, input_data)

    # Display predictions
    st.write(f"Predictions: {predictions}")

    # Shutdown H2O when done (optional)
    h2o.shutdown()
