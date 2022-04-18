from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import LabelEncoder


def SVMAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('svm'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    model.estimators_ = models
    model.le_ = LabelEncoder().fit(models[0].classes_)
    return model