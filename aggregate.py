import firebase



# Aggregation function for TFlite models : Returns Ensemble model for the given TFlite models
def aggregateTFlite(models):
    pass



#Aggregation function for SKlearn models : Returns Ensemble model for the given SKlearn models
def aggregateSKlearn(models):
    pass



# Main aggregate function : Returns Final Ensemble Model
def aggregate(project_id): 
    models = firebase.downloadModels(project_id)
    if models[0].type == "TFlite":
        finalModel = aggregateTFlite(models)
    elif models[0].type == "SKlearn":
        finalModel = aggregateSKlearn(models)
    
    result = firebase.uploadModel(finalModel, project_id)

    if(result.status == "success"):
        return "success"