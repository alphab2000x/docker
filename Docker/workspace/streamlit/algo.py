#!/usr/bin/env python
# coding: utf-8

# ## Import

# In[12]:


import seaborn as sns;
import matplotlib.pyplot as plt
import pandas as pd;
import numpy as np;
from joblib import dump, load
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
from sklearn.compose import make_column_transformer


# ## Liens :

# Télécharger le dataset : 
#    <a href="https://drive.google.com/file/d/1OEWrVjE7B2d23-eQrTMcJpRJMxoB6iUH/view?usp=sharing ">labels.csv</a>

# ## Fonction

# In[2]:


# Créer une mesure de performance

def accuracy(preds, target):
    M = target.shape[0] # Nombre d'exemple
    total_correctes = (preds == target).sum()
    accuracy = total_correctes / M
    return accuracy


# ## Collecte de données

# In[3]:


# On récupère notre Dataset et la stocke dans une variable

labels = pd.read_csv('data/labels.csv')


# In[4]:


labels


# In[5]:


labels.info()


# In[6]:


# On enlève toutes les valeurs NaN

labels = labels.dropna(how='any')


# In[7]:


# On va séparer notre target de nos colonnes

Y = labels['class'].astype('category').cat.codes # La target va être la class
X = labels['tweet'].astype(str) # La target va être la class


# In[8]:


clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)


# In[9]:


X


# In[10]:


clf.fit(X,Y)


# In[13]:


clf.predict(X)


# In[20]:


clf.predict_proba(X)


# In[16]:


dump(clf, 'labelsTrained.joblib')

