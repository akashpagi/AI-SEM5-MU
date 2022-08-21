import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

col_names = ['Reservation', 'Raining', 'BadService','Satur','Result']
hoteldata=pd.read_csv("hotel.csv",header=None,names=col_names)
feature_cols = ['Reservation', 'Raining', 'BadService','Satur']

x=hoteldata[feature_cols]
y=hoteldata.Result
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

clf=DecisionTreeClassifier(criterion="entropy",max_depth=5)
clf=clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)
print("y_test =",y_test)
print("y_pred =",y_pred)

print("Accuracy :",metrics.accuracy_score(y_test,y_pred))
dot_data=StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,feature_names=feature_cols,
                class_names=['Leave','Wait'])
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Hotel.png')
