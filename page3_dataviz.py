import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def app():
    st.title("Data Visualisation")
    
    # Exemple d'utilisation de Pandas et Plotly
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [23, 45, 56, 78]
    })
    
    fig = px.bar(df, x='Category', y='Values', title='Bar Plot with Plotly')
    st.plotly_chart(fig)
    
    # Exemple d'utilisation de Seaborn et Matplotlib
    data = np.random.randn(100)
    sns.histplot(data, kde=True)
    plt.title('Histogram with Seaborn')
    st.pyplot(plt)
    plt.clf()