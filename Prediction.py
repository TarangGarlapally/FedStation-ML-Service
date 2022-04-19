def Prediction(models,periods):
    results = []
    for model in models:
        result = model.predict(n_periods=periods)
        results.append(result)
    
    # Averaging of results in all models
    response = {}
    for i in range(periods):
        sum=0
        for result in results:
            sum += result[i]
        response[i] = sum/len(results)
    response['status']=200
    return response
