# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from fastapi import FastAPI
from aggregate import aggregate

app = FastAPI()

@app.get('/')
def welcome():
    return "Hello"


@app.get('/aggregate/{project_id}')
def projectAggregation(project_id: str): 
    response = aggregate(project_id)
    if response == "success":
        return {"response": "Success"}
    else:
        return {"response": "Aggregation Failed"}
