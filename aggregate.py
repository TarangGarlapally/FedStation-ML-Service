import firebase
import os
from sklearn.base import BaseEstimator
from SKLearn_Aggregators.LR_VC import LRAggregation
from SKLearn_Aggregators.SVM_VC import SVMAggregation
from SKLearn_Aggregators.NB_VC import NBAggregation
from SKLearn_Aggregators.KNN_VC import KNNAggregation
from SKLearn_Aggregators.DT_VC import DTAggregation

# Aggregation function for TFlite models : Returns Ensemble model for the given TFlite models
def aggregateTFlite(models):
    pass



#Aggregation function for SKlearn models : Returns Ensemble model for the given SKlearn models
def aggregateSKlearn(models):
    if type(models[0]).__name__ == "LogisticRegression":
        LRAggregation(models)
    elif type(models[0]).__name__ == "SVC":
        SVMAggregation(models)
    elif type(models[0]).__name__ == "GaussianNB":
        NBAggregation(models)
    elif type(models[0]).__name__ == "KNeighborsClassifier":
        KNNAggregation(models)
    elif type(models[0]).__name__ == "MultinomialNB":
        NBAggregation(models)
    elif type(models[0]).__name__ == "BernoulliNB":
        NBAggregation(models)
    elif type(models[0]).__name__ == "ComplementNB":
        NBAggregation(models)
    elif type(models[0]).__name__ == "CategoricalNB":
        NBAggregation(models)
    elif type(models[0]).__name__ == "DecisionTreeClassifier":
        DTAggregation(models)




# Main aggregate function : Returns Final Ensemble Model
def aggregate(project_id): 
    models = firebase.downloadModels(project_id)
    if isinstance(models[0], BaseEstimator) == False:
        finalModel = aggregateTFlite(models)
    elif isinstance(models[0], BaseEstimator) == True:
        finalModel = aggregateSKlearn(models)
    
    result = firebase.uploadModel(finalModel, project_id)

    if(result["status"] == "success"):
        return "success"