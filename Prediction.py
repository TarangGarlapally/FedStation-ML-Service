def Prediction(models,periods,freq):
    results = []
    for model in models:
        future = model.make_future_dataframe(periods=periods,freq=freq)
        forecast = model.predict(future)
        result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].iloc[periods*(-1):]
        results.append(result)
    
    # Averaging of results in all models
    response = {}
    for i in range(periods):
        yhatSum = 0
        yhat_lowerSum = 0
        yhat_upperSum = 0
        for result in results:
            yhatSum += result.iloc[i]['yhat']
            yhat_lowerSum += result.iloc[i]['yhat_lower']
            yhat_upperSum += result.iloc[i]['yhat_upper']
        yhatavg = yhatSum/len(results)
        yhat_loweravg = yhat_lowerSum/len(results)
        yhat_upperavg = yhat_upperSum/len(results)
        response[str(results[0].iloc[i]['ds'])] = {
                                            'yhat':yhatavg,
                                            'yhat_lower':yhat_loweravg,
                                            'yhat_upper':yhat_upperavg
        }
    response['status']=200
    return response
