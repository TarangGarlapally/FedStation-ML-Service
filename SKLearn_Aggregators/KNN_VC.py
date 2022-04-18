from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import LabelEncoder


def KNNAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('knn'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    model.estimators_ = models
    model.le_ = LabelEncoder().fit(models[0].classes_)
    return model