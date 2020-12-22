# importing libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score , mean_squared_error , accuracy_score ,confusion_matrix , classification_report, roc_auc_score,roc_curve
#%%
def roc_auc(X,y, model):
    gradient_roc_auc = roc_auc_score(y,model.predict(X))
    fpr,tpr , thresholds = roc_curve(y , model.predict_proba(X)[:,1])
    plt.figure()
    plt.plot(fpr,tpr,label = 'AUC (area = %0.2f )' %gradient_roc_auc)
    plt.plot([0,1], [0,1] , 'r--')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel('False Pozitif Rate')
    plt.ylabel('True Pozitif Rate')
    plt.title('Receiver operating characteristic for ' + model.__class__.__name__ )
    plt.legend(loc = 'lower right')
    plt.show()

def machinelearning(X , y ,modelname):
    #read and split data   

    X_train,X_test , y_train,y_test = train_test_split(X,y,test_size=0.3,random_state = 42)
    # modelling
    model = modelname().fit(X_train , y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    name = model.__class__.__name__
    print(classification_report(y, model.predict(X)))
    roc_auc(X,y,model)
    return name ,accuracy
        
    
#%% reading data
data = pd.read_csv('diabetes.csv')
X=data.drop('Outcome' , axis=1)
y = data['Outcome']
print(data.describe())

#%%
models = [ RandomForestClassifier , GradientBoostingClassifier , KNeighborsClassifier,LogisticRegression ]
names = [ 'RandomForestClassifier' , 'GradientBoostingClassifier' , 'KNeighborsClassifier','LogisticRegression' ]
results =pd.DataFrame( columns = ['Models', 'Accuracy'])
#%%
for each in models:
    print(each)
    name ,acc = machinelearning(X, y ,each)
    result = pd.DataFrame([[name , acc]], columns = ['Models', 'Accuracy'])
    results = results.append(result)
#%%plotting accuracy
sns.barplot(x = 'Accuracy' , y = 'Models' ,data =results)
plt.title('Accuracy Scores')
plt.xlabel('Accuracy')
plt.show()
#%%checking roc , auc
