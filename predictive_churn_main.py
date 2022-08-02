# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:48:17 2022

@author: Admin
"""

import numpy as np
import pickle
import streamlit as st


#loading the model
loaded_model = pickle.load(open('C:/Users/Admin.DESKTOP-ISGPM4M/project\Project_3/final_project/tele_churn_trained_model.sav','rb'))
    

def churn_prediction(input_data):
    
    input_data_1 = np.asarray(input_data)
    #st.write(input_data_1.shape)
    input_data_1_reshaped = input_data_1.reshape(1,-1)
    #st.write(input_data_1_reshaped.shape)
    
    #checking the prediction
    prediction_1 = loaded_model.predict(input_data_1_reshaped)
    
    if(prediction_1[0] == 0):
        return ('This person is not going to churn')
    else:
        return ('This person is going to Churn')
    
    
    
#def main():
st.title('Churn Prediction Web App')

account_length          = st.sidebar.number_input('Account length', min_value = 0)
str_voice_mail_plan     = st.sidebar.radio('Voice Mail Plan', ['Yes','No'])

if str_voice_mail_plan == 'Yes':
    voice_mail_plan     = 1
else:
    voice_mail_plan     = 0
    
#st.write(voice_mail_plan)

voice_mail_messages     = st.sidebar.number_input('Voice Mail Messages',min_value=0)
evening_minutes         = st.sidebar.number_input('Evening Minutes')
night_minutes           = st.sidebar.number_input('Night Minutes')
international_minutes   = st.sidebar.number_input('International Minutes')
customer_service_calls  = st.sidebar.number_input('Customer Service Calls', min_value=0)

str_international_plan      = st.sidebar.radio('International Plan', ['Yes','No'])

if str_international_plan == 'Yes':
    international_plan     = 1
else:
    international_plan     = 0

#st.write(international_plan)
    
day_calls               = st.sidebar.number_input('Day Calls', min_value=0)
evening_calls           = st.sidebar.number_input('Evening Calls', min_value=0)
night_calls             = st.sidebar.number_input('Night Calls', min_value=0)
international_calls     = st.sidebar.number_input('International Calls', min_value=0)
total_charge            = st.sidebar.number_input('Total Charge')

# code for prediction
churn_status = ''

#creating submit button
if st.button('Predict Churn Status'):
    churn_status= churn_prediction([account_length,voice_mail_plan,voice_mail_messages,evening_minutes,
                                    night_minutes,international_minutes,customer_service_calls,international_plan,
                                    day_calls,evening_calls,night_calls,international_calls,total_charge])


st.success(churn_status)    





