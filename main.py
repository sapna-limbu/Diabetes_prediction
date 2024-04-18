import streamlit as st
import pandas as pd
import os
import pickle

# Load the pre-trained model
current_dir = os.path.dirname(__file__)
pickle_file_path = os.path.join(current_dir, "diabetes_pred.pkl")
with open(pickle_file_path, "rb") as f:
    model = pickle.load(f)

# Define the prediction function
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    input_data = pd.DataFrame({
        'Pregnancies': [Pregnancies],
        'Glucose': [Glucose],
        'BloodPressure': [BloodPressure],
        'SkinThickness': [SkinThickness],
        'Insulin': [Insulin],
        'BMI': [BMI],
        'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
        'Age': [Age]
    })
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.title('🏥DiabeteEase')
    st.write('Please enter the following information:')
    
    # Input fields for user to enter data
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, value=0)
    glucose = st.number_input('Glucose', min_value=0, max_value=200, value=0)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=122, value=0)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=0)
    insulin = st.number_input('Insulin', min_value=0, max_value=846, value=0)
    bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=0.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.42, value=0.0)
    age = st.number_input('Age', min_value=0, max_value=81, value=0)
    
    # Make prediction when 'Predict' button is clicked
    if st.button('Predict'):
        prediction = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
        if prediction == 1:
            st.error('Please visit the doctor; you may have diabetes!')
        else:
            st.success('You may not have diabetes; however, regular health monitoring is recommended!')

if __name__ == "__main__":
    main()
