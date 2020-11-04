#!/usr/bin/env python
# coding: utf-8

# ## Import

# In[79]:


import seaborn as sns;
import matplotlib.pyplot as plt
import pandas as pd;
import numpy as np;
import streamlit as st
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

# In[80]:


# Créer une mesure de performance

def accuracy(preds, target):
    M = target.shape[0] # Nombre d'exemple
    total_correctes = (preds == target).sum()
    accuracy = total_correctes / M
    return accuracy


# In[105]:


def compare(list):
    tmp = 0
    proba = 0
    for i in range(len(list)):
        if list[i] > list[tmp]:
            tmp = i
            proba = list[i]
    return tmp, proba

def myClasse(classT, proba):
    print(" Classe : %d avec %f %%. " % (classT, proba))
    st.success(" Classe : %d avec %f %%. " % (classT, proba))
    return


# ## Collecte de données

# In[106]:


clf = load('labelsTrained.joblib')


# In[107]:


stdInput = st.text_input("Input valeur : ", "test")


# In[108]:


if st.button("Predict"):
    classT, proba = compare(clf.predict_proba([stdInput])[0])
    myClasse(classT, proba)

