from fastapi import FastAPI,HTTPException,Query
from main import get_all_products

app=FastAPI()

@app.get('/')
def home():
    return {'Hello Kuchhu Pucchu'}

@app.get('/products')
def list_products(
    name: str=Query(
        default=None,
        min_length=1,
        max_length=50,
        description='Search by product name (case insensitive)')):
        return name
