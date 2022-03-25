from sklearn.ensemble import VotingClassifier


def NBAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('nb'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    return model