from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pathlib import Path as filepath
import json
from typing import List,Dict,Annotated,Literal
from pydantic import BaseModel,Field,computed_field
import os

app= FastAPI()

# create the class of base model
class Patient(BaseModel):
    id:Annotated[str,Field(...,description='ID of the patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='Name of patient city')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender:Annotated[Literal['male','female','other'],Field(...,description='gender of the patient')]
    height:Annotated[float,Field(...,gt=0,description='height of the patient in Meters')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the patient in Kgs')]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30 :
            return 'Normal'
        else:
            return 'Obesses'




# first make the data path 
Data_file=filepath(__file__).parent.parent/'data'/'patients.json'

# make the function to load the data form the data patient file 
def load_data()->List[Dict]:
    if not Data_file.exists():
        return[]
    with open(Data_file,'r',encoding='utf-8') as f:
        return json.load(f)


@app.get('/')
def home():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message':'A fully funcitonal API to manage your Patient records'}

@app.get('/view')
def view():
    data=load_data()
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='Id of the patient in the DB',
example='P001')):
    # load all the patient
    data=load_data()
    # now check that patient_id from the given patient data
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient not found')
# now we add on more endpoint that help the data in the sorted order
@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='sort on bassis of hight,weight,or BMI'),
order:str=Query('asc',description='sort in asc or desc order')):


    valid_field=['height','weight','bmi']
    if sort_by not in valid_field:
        raise HTTPException(status_code=404,detail=f'Invalid field you have to put in{valid_field}')
    if order not in ('asc','desc'):
        raise HTTPException(status_code=404,detail='you have to put the right input')
    
    #load the data 
    data=load_data()
    # now solve the problem of reverse
    sort_order=True if order=='desc' else False
        
    # now the logic of sorted u have to right here 
    sorted_data=sorted(data.values(),key=lambda x:x.get('sort_by',0),reverse=sort_order)
    return sorted_data



def save_data(data: Dict[str, Dict]):
    with open(Data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


@app.post('/create')
def create_patient(patient:Patient):
    # load the existing data
    data=load_data()

    # check the paitent already exist
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')
    # add the new patient in the database
    data[patient.id]=patient.model_dump(exclude={'id'})

    # save in the python file
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})

