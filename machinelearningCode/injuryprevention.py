# -*- coding: utf-8 -*-
"""
Created on Thu April 28 19:15:01 2023

@author: pranayak
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Low Injury Chance'
    else:
      return '!!High Injury Chance!!'
  
    
  
def main():
    
    
    # giving a title
    st.title('Injury Prevention Web App')
    
    
    # getting the input data from the user
    Age = st.number_input('Age of the Person', min_value=0, max_value=120, step=1)
    Pregnancies = st.number_input('Heart Rate (bpm)', min_value=0, max_value=180, step=1)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=150, step=1)
    BMI = st.number_input('BMI value', min_value=0, max_value=50, step=1)
    Glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1)
    #BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=150, step=1)
    SkinThickness = st.number_input('Cortisol Level', min_value=0, max_value=100, step=1)
    Insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, step=1)
    #BMI = st.number_input('BMI value', min_value=0, max_value=50, step=1)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0, max_value=3, step=1)
    #Age = st.number_input('Age of the Person', min_value=0, max_value=120, step=1)
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Injury Detection Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    predict_button = st.session_state.get('predict_button')
    if predict_button:
        st.markdown(f'<style>.css-3xq2te{{color: #FFF; background-color: #673AB7; border-radius: 0.75rem; padding: 0.6rem 1rem; font-size: 1rem; font-weight: 500; border: none;}}</style>', unsafe_allow_html=True)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
   
