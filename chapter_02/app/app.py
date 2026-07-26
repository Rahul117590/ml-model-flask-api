from fastapi import FastAPI
from main import get_all_products

app=FastAPI()

@app.get('/')
def root():
    return ('mesage')

@app.get('/products')
def products():
    return get_all_products()
    