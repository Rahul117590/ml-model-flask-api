from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated # it is used to add the disctioption in the pydantic model
import pickle
import pandas as pd
import os


# we first load the our pickle file from the data folder
pickle_file=os.path.join('data','model.pkl')
with open(pickle_file,'rb') as f:
    model=pickle.load(f)

# make the fast api object 
app=FastAPI()
tier_1_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune']
tier_2_cities = ['Jaipur', 'Lucknow', 'Indore', 'Bhopal', 'Nagpur']

# design the pydantic model for incoming the data
class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='age of the user')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the user')]
    income_lpa:Annotated[float,Field(...,gt=0,description='income of the user')]
    smoker:Annotated[bool,Field(...,description='is user somker yes or no')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='height of user in meter')]
    city:Annotated[str,Field(...,description='the city where user lived')]
    occupation:Annotated[Literal['retired','freelancer','student','government_job',
    'business_owner','unemployed','private_job'],Field(...,description='choose the occupation of the model')]
 # now the second part we need to make the secong part that is bmi
    
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi >30:
            return 'high'
        elif self.smoker and self.bmi >27:
            return 'medium'
        else:
            return 'low' 
    @computed_field
    @property
    def age_group(self)->str:
        if self.age <25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'senior'

    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

# @app.post('/predict')
# def predict_premium(data:UserInput):
#     # we have to pass the data as input in the data frame
#     input_df=pd.DataFrame([{
#         'bmi':data.bmi,
#         'age_group':data.age_group,
#         'lifestyle_risk':data.lifestyle_risk,
#         'city_tier':data.city_tier,
#         'income':data.income_lpa,
#         'occupation':data.occupation
#     }])
#     prediction=model.predict(input_df)[0]
#     return JSONResponse(status_code=200,content={'predicted_categroy':prediction})
@app.post('/predict')
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'age': data.age,
        'weight': data.weight,
        'height': data.height,
        'income_lpa': data.income_lpa,
        'bmi': data.bmi,
        'smoker': data.smoker,
        'city': data.city
    }])

    # automatic one-hot encoding
    input_df = pd.get_dummies(input_df, columns=['smoker', 'city'])

    # model ke exact columns se align karo, missing columns 0 se fill
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={'predicted_category': str(prediction)})




