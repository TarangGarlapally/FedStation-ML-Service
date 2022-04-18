from sklearn.ensemble import VotingRegressor


def LnRAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('lnr'+str(i), models[i]))
    model = VotingRegressor(estimators=estimators, voting='hard')
    model.estimators_ = models
    return model