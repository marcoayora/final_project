import streamlit as st
import pandas as pd
import h2o

df = pd.read_csv("C:/Users/Marco/Desktop/IronHack/projects/final_project/Data/prediction_idealista.csv")


# Streamlit App
st.title('Property Price Prediction App')

# User input widgets
typology_Value = st.selectbox("Select home type", ["home", "chalet"])
price= None
area = st.number_input("Enter square mt footage:", min_value=25, value=50)

district_options = ["Nou Barris", "Horta Guinardó", "Eixample", "Sant Martí", "Sants-Montjuïc", "Gràcia", "Sarrià-Sant Gervasi", "Les Corts", "Sant Andreu", "Ciutat Vella"]
builttype_options = ["new development", "second hand / in good condition", "second hand / to be restored"]
district = st.selectbox("Select district:", district_options)
builttype_Value = st.selectbox("Select build type:", builttype_options)
# district = st.text_input("Enter district:")
# builttype_Value = st.text_input("Enter build type:")
roomnumber = st.number_input("Enter room number:", min_value=0, value=1)
bathnumber = st.number_input("Enter bath number:", min_value=0, value=1)
haslift = st.checkbox("Has lift")
hasswimmingpool = st.checkbox("Has swimming pool")
hasheating = st.checkbox("Has heating")
hasterrace = st.checkbox("Has terrace")
hasparkingspace = st.checkbox("Has parking space")
hasairconditioning = st.checkbox("Has air conditioning")
hasgarden = st.checkbox("Has garden")

if st.button('Predict Price'):
    new_row = pd.DataFrame([[typology_Value, price, area, district, builttype_Value, roomnumber, bathnumber, haslift, hasswimmingpool, hasheating, hasterrace, hasparkingspace, hasairconditioning, hasgarden]], columns=df.columns)

    df = pd.concat([df, new_row], ignore_index=True)

    user_input_df = df.copy()
    user_input_df.fillna(0, inplace=True)

 #CLEANING!!

    ad_typology_Value_mapping = {
        'home': 0,
        'chalet': 1,
    }
    user_input_df['ad_typology_Value'] = user_input_df['ad_typology_Value'].replace(ad_typology_Value_mapping)

    # Mapping for 'ad_builttype_Value'
    builttype_mapping = {
        'new development': 0,
        'second hand / in good condition': 1,
        'second hand / to be restored': 2,
    }
    user_input_df['ad_builttype_Value'] = user_input_df['ad_builttype_Value'].replace(builttype_mapping)

    # One-hot encoding for 'ad_district'
    user_input_df= pd.get_dummies(user_input_df, columns=['ad_district'], drop_first=True)

    # Convert the entire DataFrame to integers
    user_input_df = user_input_df.astype(int)

# Function to initialize H2O and make predictions

    # Initialize H2O
    h2o.init()

    # Model path
    model_path = "C:/Users/Marco/Desktop/IronHack/projects/final_project/StackedEnsemble_AllModels_1_AutoML_1_20231206_103316"

    # Select the last row from the user DataFrame
    df_user_predict = user_input_df.iloc[[-1]]

    # Load the H2O model
    loaded_model = h2o.load_model(model_path)

    # Convert the Pandas DataFrame to an H2OFrame
    h2o_df = h2o.H2OFrame(df_user_predict)

    # Perform predictions using the loaded model and H2OFrame
    predictions = loaded_model.predict(h2o_df)
    
    # Calculate the mean of predictions (modify as needed based on your use case)
    prediction = predictions.mean()

   
    st.write(f'The predicted price is {round(prediction[0], 2):,.0f}€')

    