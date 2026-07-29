from fastapi import FastAPI,Path,HTTPException,Query
from pathlib import Path as filepath
import json
from typing import List,Dict

app= FastAPI()

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


    valid_field=['heiht','weight','BMI']
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


