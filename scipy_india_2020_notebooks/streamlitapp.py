import streamlit as st
import pandas as pd

def main():
    st.title("Basic Conference Demo")
    selected_value = st.slider ('Select Value', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    df = df[df.sepal_length==selected_value]
    st.write(df)

if __name__ == "__main__":
    main()