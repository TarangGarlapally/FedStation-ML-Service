from sklearn.ensemble import VotingClassifier


def DTAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('dt'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    return model