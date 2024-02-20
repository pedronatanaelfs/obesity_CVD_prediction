import pickle
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


# Page Config
st.set_page_config(
    page_title ='Obesity Level Predictio - Data Overview',
    page_icon = 'img/icon.png'
    )

st.sidebar.header('Data Overview')
# Page Title
st.title('Data Overview')
st.image('img/obes.jpg')
st.markdown("""

# Training Data
     
&ensp;The data used to train the model is shown bellow. The attributes related with eating habits are: 
- Frequent consumption of high caloric food (FAVC),
- Frequency of consumption of vegetables (FCVC),
- Number of main meals (NCP),
- Consumption of food between meals (CAEC),
- Consumption of water daily (CH20) and 
- Consumption of alcohol (CALC). 
&ensp;The attributes related with the physical condition are: 
- Calories consumption monitoring (SCC), 
- Physical activity frequency (FAF), 
- Time using technology devices (TUE) and
- Transportation used (MTRANS)

""")
df_train = pd.read_csv('data/train.csv').set_index('id')

st.write(df_train)

st.markdown("""
&ensp;The target column is NObeyesdad, that is the prediction of obesity reached by the article: https://www.sciencedirect.com/science/article/pii/S2352340919306985
""")

desired_order = ['Obesity_Type_III', 'Obesity_Type_II', 'Obesity_Type_I', 'Overweight_Level_II', 'Overweight_Level_I', 'Normal_Weight', 'Insufficient_Weight']

st.markdown("""
&ensp;The distribution of point can give us a clear view of the groups that can be well predicted only with High and Weight, as seen in the graphic bellow.
""")

st.scatter_chart(data = df_train, x = 'Height', y = 'Weight',  color = 'NObeyesdad')

st.markdown("""
&ensp;The boxplot that follows shows us a clear relationship between other variables and the obesity predictions, where 0 represent Insuficient Weight and 6 the Obesity level III: 
""")

st.image('img/boxplot.png')

st.markdown("""
&ensp;Next, we can see the correlation of every variable with NObeyesdad in the heatmap that follows. Other variabels were added to show a clear correlation between the predictions and the BMI that is calculated based on Weight divided by Hight squared. The NObeyesdad_2 is the BMI mapped to be comparable with the originally predicted from dataset: 
""")

st.image('img/heatmap.png')

st.markdown("""
&ensp;Those and more details about the modelation step you can find on Github repository: https://github.com/pedronatanaelfs/obesity_CVD_prediction 
""")
