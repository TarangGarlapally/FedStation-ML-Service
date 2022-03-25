from sklearn.ensemble import VotingClassifier


def SVMAggregation(models):
    estimators=[]
    for  i in range(len(models)):
        estimators.append(('svm'+str(i), models[i]))
    model = VotingClassifier(estimators=estimators, voting='hard')
    return model