from sklearn.ensemble import VotingRegressor


def RDGAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('rdg'+str(i), models[i]))
    model = VotingRegressor(estimators=estimators, voting='hard')
    model.estimators_ = models
    return model