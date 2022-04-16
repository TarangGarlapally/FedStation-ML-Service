from sklearn.ensemble import VotingRegressor


def KNNRAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('knn'+str(i), models[i]))
    model = VotingRegressor(estimators=estimators, voting='hard')
    model.estimators_ = models
    return model