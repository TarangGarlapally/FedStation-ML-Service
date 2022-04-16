from sklearn.ensemble import VotingRegressor


def SVMRAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('svm'+str(i), models[i]))
    model = VotingRegressor(estimators=estimators, voting='hard')
    model.estimators_ = models
    return model