import pickle
import uvicorn
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

# Start API
app = FastAPI()

#Load Model
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#Create inicial page
@app.get('/')
def home():
    return 'Welcome to Obesity Prediction app!'

@app.get('/predict')
def predict(Age: float, Gender: str, Height: float, Weight: float, family_history_with_overweight: str, FAVC: str, FCVC: float, NCP: float, CAEC: str, SMOKE: str, CH2O: float, SCC: str, FAF: float, TUE: float, CALC: str, MTRANS: str):
    df_input = pd.DataFrame([dict(
        Age = Age,
        Gender = Gender, 
        Height = Height, 
        Weight = Weight, 
        family_history_with_overweight = family_history_with_overweight, 
        FAVC = FAVC, 
        FCVC = FCVC, 
        NCP = NCP, 
        CAEC = CAEC, 
        SMOKE = SMOKE, 
        CH2O = CH2O, 
        SCC = SCC, 
        FAF = FAF, 
        TUE = TUE, 
        CALC = CALC, 
        MTRANS = MTRANS
    )])
    output = model.predict(df_input)[0]
    return output

class Customer(BaseModel):
    Age: float
    Gender: str
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str
    class Config:
        schema_extra = {
            'example': {
                "Age": 20,
                "Gender": "Male",
                "Height": 1.70,
                "Weight": 72,
                "family_history_with_overweight": "no",
                "FAVC": "no",
                "FCVC": 0.8,
                "NCP": 2,
                "CAEC": "no",
                "SMOKE": "yes",
                "CH2O": 1.5,
                "SCC": "yes",
                "FAF": 2,
                "TUE": 1.1,
                "CALC": "Sometimes",
                "MTRANS": "Walking"
            }
        }

@app.post('/predict_with_json')
def predict(data = Customer):
    df_input = pd.DataFrame([data.dict()])
    output = model.predict(df_input)[0]
    return output

class CustomerList(BaseModel):
    data: List[Customer]

@app.post('/mult_predict_with_json')
def predict(data: CustomerList):
    df_input = pd.DataFrame(data.dict()['data'])
    output = model.predict(df_input).tolist()
    return output

#Run API
if __name__ == '__main__':
    uvicorn.run(app)

