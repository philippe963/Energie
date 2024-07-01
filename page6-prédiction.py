import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def app():
    st.title("Prédiction")
    
    # Chargement des données (exemple avec des données fictives)
    df = pd.DataFrame({
        'Feature1': np.random.randn(100),
        'Feature2': np.random.randn(100),
        'Target': np.random.randint(0, 2, 100)
    })
    
    X = df[['Feature1', 'Feature2']]
    y = df['Target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Exemple avec Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    st.write(f"Accuracy with Logistic Regression: {score}")
    
    # Exemple avec Decision Tree
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    st.write(f"Accuracy with Decision Tree: {score}")
    
    # Exemple avec K-Neighbors
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    st.write(f"Accuracy with K-Neighbors: {score}")
