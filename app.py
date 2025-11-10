import pandas as pd
import streamlit as st
import joblib

# Load Model
model = joblib.load('xgb_model.jb')

# App Title
st.set_page_config(page_title="🏡 House Price Predictor", layout="centered")
st.title("🏠 House Price Prediction App")
st.markdown(
    """
    Enter the details below to predict the **estimated house price**.  
    Adjust the sliders or numbers and click **Predict Price**.
    """
)

# Input Features
inputs = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
    'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
    'CentralAir'
]

# Create input form
with st.form("house_input_form"):
    st.subheader("🏗️ Property Details")
    
    col1, col2 = st.columns(2)
    input_data = {}

    # Numeric inputs in two columns for better layout
    for i, feature in enumerate(inputs):
        if feature == 'CentralAir':
            continue  # handled later
        col = col1 if i % 2 == 0 else col2
        with col:
            input_data[feature] = st.number_input(
                f"{feature}",
                value=0.0,
                step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces'] else 0.1
            )

    st.subheader("🌡️ Air Conditioning")
    input_data['CentralAir'] = st.radio(
        "Central Air Available?",
        options=['Yes', 'No'],
        horizontal=True
    )

    submitted = st.form_submit_button("💰 Predict Price")

if submitted:
    # Convert categorical to numeric
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == "Yes" else 0

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data], columns=inputs)

    # Display user input
    with st.expander("🔍 View Input Data"):
        st.dataframe(input_df.style.highlight_max(axis=0))

    # Make Prediction
    predictions = model.predict(input_df)

    # Display result
    st.success(f"🏡 **Predicted House Price:** ${predictions[0]:,.2f}")

    st.balloons()  # 🎈 for fun!
