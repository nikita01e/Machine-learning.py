# -*- coding: utf-8 -*-
"""naive bayas pract2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PGX94fEMvTutl9vaoE16mJtK-hateAAE
"""

import pandas as pd

df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/spam.csv')
df.head()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(df['Category'],df['Message'],test_size=0.2)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer=CountVectorizer()
x_train_count=vectorizer.fit_transform(y_train)
x_test_count=vectorizer.transform(y_test)

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x_train_count,y_train)

y_pred=model.predict(x_test_count)

from sklearn.metrics import accuracy_score,classification_report
accuracy_score(y_test,y_pred)



report=classification_report(y_test,y_pred)
print(report)





