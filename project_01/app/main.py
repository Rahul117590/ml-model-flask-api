from fastapi import FastAPI
from pathlib import Path
import json

app= FastAPI()

# first make the data path 
Data_file=Path(__file__).parent.parent/'data'/'patients.json'

# make the function to load the data form the data patient file 
def load_data():
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