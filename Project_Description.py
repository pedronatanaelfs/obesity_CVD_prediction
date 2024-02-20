import streamlit as st

st.set_page_config(
    page_title = "Obesity Level Prediction",
    page_icon = 'img/icon.png'
)

st.sidebar.header('Project Description')

st.write("# Welcome to Obesity Level Prediction App.")
st.write('\n\n')

st.image('img/obes.jpg')

st.markdown(
    '''
    # Obesity Prediction App

## Overview
The Obesity Prediction App is a data-driven tool designed to estimate the obesity level of an individual based on their habits and physical traits. Utilizing a machine learning model trained on a diverse dataset from Mexico, Peru, and Colombia, the app provides personalized predictions by analyzing user-input data with accuracy higher than 90%.

- Github Repository: https://github.com/pedronatanaelfs/obesity_CVD_prediction

## Dataset
The dataset used for training comprises information gathered through a web platform survey, where anonymous users from the specified countries, aged between 14 and 61, shared details about their eating habits and physical conditions. The dataset consists of 17 attributes and 2111 records, ensuring a comprehensive representation of various lifestyles and demographics.
Access the article: https://www.sciencedirect.com/science/article/pii/S2352340919306985

## Features
- **User-Friendly Interface:** The app boasts an intuitive interface, allowing users to input their data effortlessly.
- **Personalized Predictions:** By leveraging advanced machine learning algorithms, the app tailors predictions based on individual responses, providing a nuanced understanding of obesity risk.
- **Data Security:** Privacy is a top priority. The app ensures the confidentiality of user information and follows ethical data handling practices.

## How It Works
1. **Input Data:** Users answer a series of questions related to their eating habits and physical condition.
2. **Prediction:** The app processes the input data through the trained machine learning model to generate a personalized obesity level prediction.
3. **Insights:** Users receive insights into the factors contributing to their predicted obesity level, fostering awareness and potential lifestyle changes.

## Benefits
- **Health Awareness:** Users gain insights into their potential obesity risk, promoting proactive health management.
- **Tailored Recommendations:** The app suggests personalized recommendations for maintaining a healthy lifestyle.
- **Research Contribution:** By participating, users contribute to ongoing research in the field of obesity prediction and prevention.

## Get Started
1. **Acess the app:** Please *go to the next pages* to get the predictions through the sidebar.
2. **Answer Questions:** Complete the survey to receive your personalized obesity level prediction.
3. **Explore Insights:** Understand the contributing factors and receive tailored recommendations for a healthier lifestyle.

Take control of your health with the Obesity Prediction App — your personalized guide to a healthier future.

'''
)

st.markdown('<a href="Predictions" target="_self">Make Predictions</a>', unsafe_allow_html=True)