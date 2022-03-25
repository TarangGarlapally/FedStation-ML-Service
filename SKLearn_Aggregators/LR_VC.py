from sklearn.ensemble import VotingClassifier


def LRAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('lr'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    return model