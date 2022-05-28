import streamlit as st
import pandas as pd
from sklearn import datasets

def app():
    st.write("Berikut beberapa contoh `Dataset`.")

    st.write("Berikut ini adalah DataFrame dari dataset `iris`.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)

   
    st.write("""

    Berikut ini adalah DataFrame dari dataset `kanker payudara`.
    """)

    breast_cancer = datasets.load_breast_cancer()
    X = pd.DataFrame(breast_cancer.data, columns = breast_cancer.feature_names)
    df = pd.concat([X], axis=1)

    st.write(df)

    st.write("""

    Berikut ini adalah DataFrame dari dataset `digits`.
    """)

    digits = datasets.load_digits()
    X = pd.DataFrame(digits.data, columns = digits.feature_names)
    df = pd.concat([X], axis=1)

    st.write(df)

