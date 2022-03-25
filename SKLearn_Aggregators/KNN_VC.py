from sklearn.ensemble import VotingClassifier


def KNNAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('knn'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    return model