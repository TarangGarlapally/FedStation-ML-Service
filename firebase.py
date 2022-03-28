'''
Firebase Credentials 
'''

'''dummy imports please remove them if found'''
from unicodedata import name
import firebase_admin
from firebase_admin import storage
import os
''''''


# Download models from firebase : Returns list of models
def downloadModels(project_id):
    ds = storage.bucket()
    file_names = list()
    L = len(project_id)
    for b in ds.list_blobs(): 
        file_names.append(b.name)
    print(file_names , L )
    
    for file_path in file_names :
        file_dir = file_path[0:L]
        print(file_dir , file_path[L+1:])
        if(file_dir == project_id and len(file_path) > L+1):
            print("matched",file_path[L+1:])
            bob = ds.blob(file_path)
            bob.download_to_filename("model-files/local/"+ file_path[L+1:])


# Upload model to firebase : Returns response object with status property
def uploadModel(project_id):
    ds = storage.bucket()
    print(ds.list_blobs)
    bob = ds.blob("globalModels/"+project_id)
    bob.upload_from_filename("model-files/globalModel.pkl")

    #removing all files in model-files/local 
    
    
    
    dir = 'model-files/local/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

