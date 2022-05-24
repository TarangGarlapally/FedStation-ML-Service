# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from urllib import response
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import FileResponse
from aggregate import aggregate
from fastapi.middleware.cors import CORSMiddleware
from firebase import getFile,getGlobalModelFile, getGlobalModeldownloadURL, uploadModelToFirebase,uploadInputProcessorFile, downloadModels, getInputProcessorFile, getGlobalModelFileForResult
from firebase_init import initializeFirebase
from Prediction import Prediction
import importlib
import os
import pickle
import shutil

initializeFirebase()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def welcome():
    return "Hello"

@app.get('/fileDownload/{project_id}')
def downloadFile(project_id):
    downloadURL = getFile(project_id)
    if(len(downloadURL)== 0):
        return {
            "response" : "Error"
        }
    else : 
        return {
            "response" : downloadURL
        }


@app.get('/aggregate/{project_id}')
def projectAggregation(project_id: str):    
    response = aggregate(project_id)
    if response == "success":
        return {"response":"Okay"}
    else:
        return {"response": "Error somewhere 🤧"}

@app.get('/downloadGlobalModelURL/{project_id}')
def downloadGlobalModelURLFromFirebase(project_id: str):
    downloadURL = getGlobalModeldownloadURL(project_id)

    if(len(downloadURL)== 0):
        return {
            "response" : "Error"
        }
    else : 
        return {
            "response" : downloadURL
        }

@app.get('/getGlobalModelFile/{project_id}')
async def getGlobalModelFileFromFirebase(project_id: str):
    await getGlobalModelFile(project_id)
    return FileResponse('model-files/'+project_id+'.pkl',media_type='application/octet-stream',filename=project_id)

# @app.get('/specialCaseTimeSeries/{project_id}/predict/{periods}')
# def specialCaseTimeSeriesPredict(project_id: str, periods: int):
#     models = downloadModels(project_id)
#     if(len(models) == 0):
#         return {
#             "response" : "No models Error"
#         }
#     result = Prediction(models,periods)
#     return {"response": result}


@app.post('/uploadModelToFirebase/{project_id}')
async def uploadModelToFB(project_id : str , upload_file : UploadFile = File(...)):
    return await uploadModelToFirebase(project_id , upload_file)

@app.post('/uploadInputProcessFile')
async def uploadInputProcessFile(file : UploadFile = File(...), id : str = Form(...)):
    return uploadInputProcessorFile(id , file)

@app.post('/getModelResult/{project_id}')
async def getModelResult(project_id: str, input: Request):
    if os.path.exists("./__pycache__"):
        shutil.rmtree("./__pycache__")
        
    # download input processor file
    getInputProcessorFile(project_id)
    # download global model
    getGlobalModelFileForResult(project_id)
    
    model = None
    # load model
    with open("./model-files/"+project_id+".pkl", 'rb') as f:
        model = pickle.load(f)

    test = __import__(project_id)

    result = test.processInputAndPredict(await input.json(), model)
    
    os.remove("./"+project_id+".py")
    os.remove("./model-files/"+project_id+".pkl")
    return result