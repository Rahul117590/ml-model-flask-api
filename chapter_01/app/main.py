from fastapi import FastAPI

# route/object of fastapi
app=FastAPI()

@app.get("/")
def root():
    return {'message : hello Kuchu Pucchu'}


