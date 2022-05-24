import firebase
import os
from sklearn.base import BaseEstimator
from pmdarima.arima import auto_arima
from Fedstation.EnsembleARIMA import EnsembleARIMA
from SKLearn_Aggregators.LR_VC import LRAggregation
from SKLearn_Aggregators.SVM_VC import SVMAggregation
from SKLearn_Aggregators.NB_VC import NBAggregation
from SKLearn_Aggregators.KNN_VC import KNNAggregation
from SKLearn_Aggregators.DT_VC import DTAggregation
from SKLearn_Aggregators.LnR_VR import LnRAggregation
from SKLearn_Aggregators.DT_VR import DTRAggregation
from SKLearn_Aggregators.LS_VR import LSAggregation
from SKLearn_Aggregators.RDG_VR import RDGAggregation
from SKLearn_Aggregators.KNN_VR import KNNRAggregation
from SKLearn_Aggregators.SVM_VR import SVMRAggregation


# Aggregation function for special models : Returns Ensemble model for the given special models
def aggregateSpecial(models):
    globalModel = EnsembleARIMA(models)
    return globalModel


# Aggregation function for TFlite models : Returns Ensemble model for the given TFlite models
def aggregateTFlite(models):
    pass



#Aggregation function for SKlearn models : Returns Ensemble model for the given SKlearn models
def aggregateSKlearn(models):
    if type(models[0]).__name__ == "LogisticRegression":
        return LRAggregation(models)
    elif type(models[0]).__name__ == "SVC":
        return SVMAggregation(models)
    elif type(models[0]).__name__ == "GaussianNB":
        return NBAggregation(models)
    elif type(models[0]).__name__ == "KNeighborsClassifier":
        return KNNAggregation(models)
    elif type(models[0]).__name__ == "MultinomialNB":
        return NBAggregation(models)
    elif type(models[0]).__name__ == "BernoulliNB":
        return NBAggregation(models)
    elif type(models[0]).__name__ == "ComplementNB":
        return NBAggregation(models)
    elif type(models[0]).__name__ == "CategoricalNB":
        return NBAggregation(models)
    elif type(models[0]).__name__ == "DecisionTreeClassifier":
        return DTAggregation(models)
    elif type(models[0]).__name__ == "LinearRegression":
        return LnRAggregation(models)
    elif type(models[0]).__name__ == "Ridge":
        return RDGAggregation(models)
    elif type(models[0]).__name__ == "Lasso":
        return LSAggregation(models)
    elif type(models[0]).__name__ == "DecisionTreeRegressor":
        return DTRAggregation(models)
    elif type(models[0]).__name__ == "KNeighborsRegressor":
        return KNNRAggregation(models)
    elif type(models[0]).__name__ == "SVR":
        return SVMRAggregation(models)


# Main aggregate function : Returns Final Ensemble Model
def aggregate(project_id): 
    models = firebase.downloadModels(project_id)
    try:
        if isinstance(models[0], BaseEstimator) == False:
                finalModel = aggregateTFlite(models)
        elif isinstance(models[0], BaseEstimator) == True:
            if type(models[0]).__name__ == "ARIMA":
                finalModel = aggregateSpecial(models)
            else:
                finalModel = aggregateSKlearn(models)
        result = firebase.uploadModel(finalModel, project_id)
        return result
    except:
        return "error"
    
