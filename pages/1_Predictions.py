import pickle
import pandas as pd
import streamlit as st

# Page Config
st.set_page_config(
    page_title ='Obesity level Prediction - Predictions',
    page_icon = 'img/icon.png'
    )

st.sidebar.header('Predictions')
# Page Title
st.title('Calculate Predictions')
st.image('img/obes.jpg')

# -- Parameters -- #
# Gender,Age,Height,Weight,family_history_with_overweight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS

age = st.number_input(label = 'What is your age?', value = 18)
gender = st.radio('Select your gender',['Female', 'Male'])
height = st.number_input(label = 'What is your height in meters?', value = 1.6)
weight = st.number_input(label = 'What is your weight in kilograms?', value = 70.0)
family_history_with_overweight = st.radio('Do you have family history with overweight?',['no', 'yes'])
favc = st.radio('Do you eat high caloric food frequently?',['no', 'yes'])
fcvc = st.slider(label = 'How often do you consume vegetables? (0 = Never / 3 = Always)', min_value = 0., max_value = 3.)
ncp = st.number_input(label = 'How many main meals you have daily?', value = 1.)
caec = st.radio('Do you snack between meals?',['no', 'Sometimes', 'Frequently', 'Always'])
smoke = st.radio('Do you smoke?',['no', 'yes'])
ch2o = st.number_input(label = 'How many liters of water do you drink a day?', value = 1.)
scc = st.radio('Do you monitor your calorie consumption?',['no', 'yes'])
faf = st.slider(label = 'What is yout fisical activity frequency? (0 = Sedentary / 3 = High level activity)', min_value = 0., max_value = 3.)
tue = st.slider(label = 'How long do you use technological devices? (0 = Never / 2 = All the time)', min_value = 0., max_value = 2.)
calc = st.radio('Do you consume alcohol?',['no', 'Sometimes', 'Frequently'])
mtrans = st.radio('Which means of transport do you use most?',['Walking', 'Bike', 'Motorbike', 'Automobile', 'Public_Transportation'])

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
    try:
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
    except Exception as error:
        st.error(f"Couldn't predict the input data. The following error occurred: \n\n{error}")
