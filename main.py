# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from urllib import response
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from aggregate import aggregate
from firebase import getGlobalModelFile, getGlobalModeldowloadURL, uploadModelToFirebase
from firebase_init import initializeFirebase

initializeFirebase()
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

@app.get('/dowloadGlobalModelURL/{project_id}')
def dowloadGlobalModelURLFromFirebase(project_id: str):
    dowloadURL = getGlobalModeldowloadURL(project_id)

    if(len(dowloadURL)== 0):
        return {
            "response" : "Error"
        }
    else : 
        return {
            "response" : dowloadURL
        }

@app.get('/getGlobalModelFile/{project_id}')
async def getGlobalModelFileFromFirebase(project_id: str):
    await getGlobalModelFile(project_id)
    return FileResponse('model-files/globalModel.pkl',media_type='application/octet-stream',filename=project_id)

@app.post('/uploadModelToFirebase/{project_id}')
async def uploadModelToFB(project_id : str , upload_file : UploadFile):
    return await uploadModelToFirebase(project_id , upload_file)