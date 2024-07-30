
y_pred= Regression.predict(x_test)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

new_data= {'area':2450, 'bedrooms':3, 'bathrooms':2, 'stories':2, 'mainroad':1, 'guestroom':0, 'basement':1, 'hotwaterheating':0, 'airconditioning':1, 'parking':1, 'prefarea':1, 'furnishingstatus':2}

index = [1]

my_data= pd.DataFrame(new_data, index)

new_predictions=Regression.predict(my_data)

print("The house price of the given house is", new_predictions)