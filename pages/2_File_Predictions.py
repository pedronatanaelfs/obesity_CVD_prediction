import pickle
import pandas as pd
import streamlit as st

# Page Config
st.set_page_config(
    page_title ='Obesity level Prediction - File Prediction',
    page_icon = 'img/icon.png'
    )

st.sidebar.header('File Prediction')
st.title("Calculate Predictions by CSV File")
st.image('img/obes.jpg')

st.markdown("Predict obesity level using a csv file:")

# -- Model -- #
with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

data = st.file_uploader('Upload your file')
if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction = insurance_prediction)

    st.markdown('Obesity level prediction at the end: ')
    st.write(df_output)
    st.download_button(label = 'Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
                       mime = 'text/csv',
                       file_name='predicted_obesity.csv')