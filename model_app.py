import joblib
import streamlit as st

model = joblib.load("regression.joblib")

size = st.number_input("Enter the size of the house (in sq ft)", min_value=0.0, step=100.0)
bedrooms = st.number_input("Enter the number of bedrooms", min_value=0, step=1)
has_garden = st.number_input("Does the house have a garden? (0 for No, 1 for Yes)", min_value=0, max_value=1, step=1)

if st.button("Predict Price"):
    input_data = [[size, bedrooms, has_garden]]
    
    prediction = model.predict(input_data)
    
    st.write(f"The predicted price of the house is: ${prediction[0]:,.2f}")
