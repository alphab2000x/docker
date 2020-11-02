#!/usr/bin/env python
# coding: utf-8

# ## Import

# In[40]:


import seaborn as sns;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as TTS
from sklearn.model_selection import cross_val_score;
from sklearn.preprocessing import LabelEncoder;
from sklearn.ensemble import RandomForestClassifier

# pipeline elements
from sklearn.decomposition import PCA # PCA = Principal Component Analysis
from sklearn.neighbors import KNeighborsClassifier as KNN 

# pipeline materiaux
from sklearn.pipeline import Pipeline # PCA = Principal Component Analysis
from sklearn.model_selection import GridSearchCV

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from stop_words import get_stop_words


# ## Liens :

# Télécharger le dataset : 
#    <a href="https://drive.google.com/file/d/1OEWrVjE7B2d23-eQrTMcJpRJMxoB6iUH/view?usp=sharing ">labels.csv</a>

# ## Fonction

# In[19]:


# Créer une mesure de performance

def accuracy(preds, target):
    M = target.shape[0] # Nombre d'exemple
    total_correctes = (preds == target).sum()
    accuracy = total_correctes / M
    return accuracy


# ## Collecte de données

# In[20]:


# On récupère notre Dataset et la stocke dans une variable

labels = pd.read_csv('data/labels.csv')


# In[21]:


labels


# In[22]:


labels.info()


# In[23]:


labels['class'].unique()


# In[24]:


# On va séparer notre target de nos colonnes

Y = labels['class'].astype('category').cat.codes # La target va être la class
X = labels.drop('class', axis='columns')


# In[25]:


# Maintenant que l'on a créé nos colonnes, on supprime nos de base vue que l'on en a plus besoin

X = X.drop(['tweet'],axis=1)


# In[26]:


# On enlève toutes les valeurs NaN

X = X.dropna(how='any')


# In[27]:


X_tr, X_te, Y_tr, Y_te = TTS(X, Y,              # features, target
                            stratify = Y,       # Va prendre une proportion aux hasard de valeurs différentes histoire de ne pas avoir des cas où l'on a que des même valeur
                            random_state=777,   # Sert à fixer le harsard pour ne pas avoir des résultat différents à chaque tests.
                            train_size=0.8)     # 50% de X_train et Y_train et 50% de Y_test et Y_test


# In[39]:


clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True)))


# In[ ]:




