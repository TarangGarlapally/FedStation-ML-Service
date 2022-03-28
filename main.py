# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from fastapi import FastAPI
from aggregate import aggregate
from firebase_init import initializeFirebase
from firebase import downloadModels , uploadModel

initializeFirebase()
downloadModels("k_k")
uploadModel("KKK")
app = FastAPI()

@app.get('/')
def welcome():
    return "Hello"


@app.get('/aggregate/{project_id}')
def projectAggregation(project_id: str): 
    response = aggregate(project_id)
    if response == "success":
        return {"response":"Okay 🥚"}
    else:
        return {"response": "Error somewhere 🤧"}
