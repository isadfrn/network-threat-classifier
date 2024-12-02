import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    fbeta_score,
    roc_curve,
    auc
)
import matplotlib.pyplot as plt

df = pd.read_csv('processed_data.csv')

features = ['l_ipn', 'r_asn', 'f', 'weekday', 'is_weekend', 'month']
X = df[features]
y = df['compromised']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

svm_clf = SVC(kernel='rbf', probability=True, random_state=42)
svm_clf.fit(X_train_res, y_train_res)

y_pred = svm_clf.predict(X_test)
y_proba = svm_clf.predict_proba(X_test)[:, 1]

conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(conf_matrix)

accuracy = accuracy_score(y_test, y_pred)
print("Acurácia: {:.2f}%".format(accuracy * 100))

precision = precision_score(y_test, y_pred)
print("Precisão: {:.2f}%".format(precision * 100))

recall = recall_score(y_test, y_pred)
print("Recall: {:.2f}%".format(recall * 100))

f1 = f1_score(y_test, y_pred)
print("F1 Score: {:.2f}%".format(f1 * 100))

fbeta = fbeta_score(y_test, y_pred, beta=0.5)
print("Fβ Score (β=0.5): {:.2f}%".format(fbeta * 100))

fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
print("AUC da Curva ROC: {:.2f}%".format(roc_auc * 100))

plt.figure()
plt.plot(fpr, tpr, color='darkorange', label='Curva ROC (AUC = %0.2f%%)' % (roc_auc * 100))
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Característica de Operação do Receptor (ROC)')
plt.legend(loc="lower right")
plt.savefig('roc_curve.png')
plt.close()
