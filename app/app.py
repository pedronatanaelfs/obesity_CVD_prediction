import pickle
import pandas as pd
import streamlit as st

# Page Config
st.set_page_config(page_title ='Obesity level and Cardiovascular Risk Prediction')

# Page Title
st.title('Obesity level and Cardiovascular Risk Prediction')

# -- Parameters -- #
# Gender,Age,Height,Weight,family_history_with_overweight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS

age = st.number_input(label = 'Age', value = 18)
gender = st.selectbox(label = 'Gender', options = ['Female', 'Male'])
height = st.number_input(label = 'Height', value = 1.6)
weight = st.number_input(label = 'Weight', value = 70.0)
family_history_with_overweight = st.selectbox(label = 'Family History with Overweight', options = ['no', 'yes'])
favc = st.selectbox(label = 'Frequent Consumption of High Caloric Food', options = ['no', 'yes'])
fcvc = st.number_input(label = 'Frequency of Consumption of Vegetables (0-3)', value = 1.)
ncp = st.number_input(label = 'Number of Main Meals', value = 1.)
caec = st.selectbox(label = 'Consumption of Food between Meals', options = ['no', 'Sometimes', 'Frequently', 'Always'])
smoke = st.selectbox(label = 'SMOKE', options = ['no', 'yes'])
ch2o = st.number_input(label = 'Consumption of Water Daily', value = 1.)
scc = st.selectbox(label = 'Calories Consumption Monitoring', options = ['no', 'yes'])
faf = st.number_input(label = 'Fisical Activity Frequency (0-3)', value = 1.)
tue = st.number_input(label = 'Time Using Technology Devices (0-2)', value = 1.)
calc = st.selectbox(label = 'Consumption of Alcohol', options = ['no', 'Sometimes', 'Frequently'])
mtrans = st.selectbox(label = 'Transportation Used', options = ['Walking', 'Bike', 'Motorbike', 'Automobile', 'Public_Transportation'])

# -- Model -- #

with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def prediction():
    df_input = pd.DataFrame([{
        'Age': age,
        'Gender': gender,
        'Height': height,
        'Weight': weight,
        'family_history_with_overweight': family_history_with_overweight,
        'FAVC': favc,
        'FCVC': fcvc,
        'NCP': ncp,
        'CAEC': caec,
        'SMOKE': smoke,
        'CH2O': ch2o,
        'SCC': scc,
        'FAF': faf,
        'TUE': tue,
        'CALC': calc,
        'MTRANS': mtrans
    }])
    prediction = model.predict(df_input)[0]
    return prediction

if st.button('Predict'):
    obesity_predict = prediction()
    BMI = weight / (height * height)
    Obes_act = ''
    if BMI < 18.5:
        Obes_act = 'Insufficient_Weight'
    elif BMI < 25.0:
        Obes_act = 'Normal_Weight'
    elif BMI < 27.4:
        Obes_act = 'Overweight_Level_I'
    elif BMI < 30.0:
        Obes_act = 'Overweight_Level_II'
    elif BMI < 35.0:
        Obes_act = 'Obesity_Type_I'
    elif BMI < 40.0:
        Obes_act = 'Obesity_Type_II'
    elif BMI > 40.0:
        Obes_act = 'Obesity_Type_III'
    st.success(f'Actual Obesity Level: {Obes_act}\n\n'
        f'\nPrediction for the future: {obesity_predict}')
              
