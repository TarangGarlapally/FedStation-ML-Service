# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
from aggregate import aggregate

app = FastAPI()

# Model Structure - Class
class ModelParams(BaseModel):
    email: str
    classes_: List[float]
    coef_: List[List[float]]
    intercept_: List[float]
    n_iter_: List[int]

@app.get('/')
def welcome():
    return "Hello"


#use any authentication to accept requests
@app.get('/aggregate/{project_id}')
def projectAggregation(project_id: str): 
    response = aggregate(project_id)
    if response == "success":
        return {"response":"Okay 🥚"}
    else:
        return {"response": "Error somewhere 🤧"}
