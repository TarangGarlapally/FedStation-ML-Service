from sklearn.ensemble import VotingRegressor


def LSAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('ls'+str(i), models[i]))
    model = VotingRegressor(estimators=estimators, voting='hard')
    model.estimators_ = models
    return model