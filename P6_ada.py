import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
col_names = ['Reservation', 'Raining', 'BadService','Satur','Result']

hoteldata = pd.read_csv("hotel.csv", header=None, names=col_names)
feature_cols = ['Reservation', 'Raining', 'BadService','Satur']
X = hoteldata[feature_cols] 
y = hoteldata.Result

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=1) 

adahotel = AdaBoostClassifier(n_estimators=6, learning_rate=2)
adahotel= adahotel.fit(X_train,y_train)

y_pred = adahotel.predict(X_test)

print("ytest = \n", y_test)
print("ypred = \n", y_pred)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))