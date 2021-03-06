'''
Firebase Credentials 
'''

'''imports'''
from distutils.log import error
from unicodedata import name
from fastapi import UploadFile
import firebase_admin
from firebase_admin import storage
import os
import pickle as pkl
import json
import sys
''''''


# Download models from firebase : Returns list of models
def downloadModels(project_id):
    try:
        if os.path.isdir('model-file/') == False:
            os.mkdir('model-files/')
        if os.path.isdir('model-files/local/') == False:
            os.mkdir('model-files/local/')
        ds = storage.bucket()
        file_names = list()
        L = len(project_id)
        for b in ds.list_blobs(): 
            file_names.append(b.name)
        
        for file_path in file_names :
            file_dir = file_path[0:L]
            if(file_dir == project_id and len(file_path) > L+1):
                print("matched",file_path[L+1:])
                bob = ds.blob(file_path)
                bob.download_to_filename("model-files/local/"+ file_path[L+1:])
        
        # uploading models onto list 
        models = list()
        files = os.listdir("model-files/local/")
        for file in files:
            filename = "model-files/local/"+file
            loaded_model = pkl.load(open(filename, 'rb'))
            models.append(loaded_model)

        dir = 'model-files/local/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        os.rmdir('model-files/local')
        os.rmdir('model-files')
        
        return models
    except:
        return "error"




# Upload model to firebase : Returns response object with status property
def uploadModel(finalModel, project_id):
    if os.path.isdir('model-files/') == False:
        os.mkdir('model-files/')
    pkl.dump(finalModel, open("model-files/globalModel.pkl", 'wb'))
    ds = storage.bucket()
    bob = ds.blob("globalModels/"+project_id+".pkl")
    bob.upload_from_filename("model-files/globalModel.pkl")


    #removing all files in model-files/local and globalmodel.pkl

    # dir = 'model-files/local/'
    # for f in os.listdir(dir):
    #     os.remove(os.path.join(dir, f))
    os.remove('model-files/globalModel.pkl')
    # os.rmdir('model-files/local')
    os.rmdir('model-files')
    
    return "success"



# download Global Model url from Firebase
def getGlobalModeldownloadURL(project_id):
    ds = storage.bucket()
    bob = ds.blob("globalModels/"+project_id+".pkl")
    downloadURL  = bob._get_download_url(ds.client)      
    return downloadURL

# Dummy function to download the file from firebase
def getFile(project_id):
    ds = storage.bucket()
    bob = ds.blob("InputProcessors/"+project_id+".py")
    downloadURL  = bob._get_download_url(ds.client)      
    return downloadURL

async def getGlobalModelFile(project_id):
    if not os.path.exists("model-files"):
        os.makedirs("model-files")
    ds = storage.bucket()
    bob = ds.blob("globalModels/"+project_id+".pkl")
    bob.download_to_filename("model-files/"+project_id+".pkl"); 

def getGlobalModelFileForResult(project_id):
    try:
        if not os.path.exists("model-files"):
            os.makedirs("model-files")
        ds = storage.bucket()
        bob = ds.blob("globalModels/"+project_id+".pkl")
        if bob.exists():
            bob.download_to_filename("model-files/"+project_id+".pkl");
        else:
            return "error"
        return "success"
    except Exception as e:
        return "error"

# upload Models to Firebase
async def uploadModelToFirebase(project_id , model : UploadFile):
    ds = storage.bucket()
    bob = ds.blob(project_id+"/" + model.filename +".pkl")
    try:
        bob.upload_from_file(model.file)
        return "File Uploaded"
    except Exception as e:
        print(e)
        return "Error"
    finally:
        model.file.close()

# upload input processing file to Firebase
def uploadInputProcessorFile(project_id , inputProcessFile : UploadFile):
    ds = storage.bucket()
    bob = ds.blob("InputProcessors/"+project_id+".py")
    try:
        bob.upload_from_file(inputProcessFile.file)
        return "File Uploaded"
    except Exception as e:
        print(e)
        return "Error"
    finally:
        inputProcessFile.file.close()

def getInputProcessorFile(project_id):
    try:
        ds = storage.bucket()
        bob = ds.blob("InputProcessors/"+project_id+".py")
        if bob.exists():
            bob.download_to_filename(project_id+'.py');
        else:
            return "error"
    except Exception as e:
        return "error"
