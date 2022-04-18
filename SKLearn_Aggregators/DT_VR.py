from sklearn.ensemble import VotingRegressor


def DTRAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('dt'+str(i), models[i]))
    model = VotingRegressor(estimators=estimators, voting='hard')
    model.estimators_ = models
    return model