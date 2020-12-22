# Diabetes
Hi everyone
I designed a small interface that calculates whether the person is diabetic or not, with a 75 percent success rate, based on values such as pregnancy, insulin value, body mass index etc. 
All you have to do is enter the requested information and press the 'Check' button.
## How did I decide on the model?
After examining the data, I started testing multiple machine learning algorithms in a for loop. Algorithms are:
* RandomForestClassifier
* GradientBoostingClassifier
* KNNClassifier
* LogisticRegression

I examined individual f1 scores, accuracy score and roc auc plots for these algorithms.
### F1-Scores
First of all, I added the table below if necessary to explain how the f1-score is calculated. This table expresses the confusion matrix.



| Predicted/Actual | Diabet(1)      |  Not Diabet(0) |        
|------------------| ---------------| ---------------|        
|     Diabet(1)    | True Positive  | False Positive |          
|  Not Diabet(0)   | False Negative | True Negative  |

Using this table, we can calculate Precision and Recall values.

|  | Description |
| --- | --- |
| Precision | True Positive / (True Positive + False Positive) |
| Recall| True Positive / (True Positive + False Negative) |
| F1-Score| 2 / (1/Precision + 1/Recall ) |

The highest F1-score, the better predictive power of the classification procedure. 
Then I examined the f1 scores of my models.

|   | Model                  | F1-Score | 
|------| ---| -----|   
| 0 | RandomForestClassifier | 0.94 |
| 1 | RandomForestClassifier | 0.89 |
| 0 | GradientBoostingClassifier | 0.92 |
| 1 | GradientBoostingClassifier | 0.84 |
| 0 | KNNClassifier | 0.83 |
| 1 | KNNClassifier | 0.65 |
| 0 | LogisticRegression | 0.83 |
| 1 | LogisticRegression| 0.64 |

As we can see, RandomForestClassifier gives the best result.
### Accuracy Scores 
I drew a bar chart to compare the accuracy scores of the models.
![](/images/barplot.png)
### ROC AUC Score
AUC - ROC curve is a performance measurement for classification problem at various thresholds settings.  
         - |  -
:-------------------------:|:-------------------------:
![](/images/randomforest_roc.png)  |  ![](/images/gradientboosting_roc.png)
![](/images/logic_roc.png)  |  ![](/images/knn_roc.png)

As you can see, RandomForestClassifier gives the best results here.

## Training 
After comparing the above models, I decided that the best model for this dataset is RandomForestClassifier and created my model.

## Interface
![](/images/diabetes_readme.png)

You can learn the result with the 'Check' button and 'Reset' all data with the reset button.
