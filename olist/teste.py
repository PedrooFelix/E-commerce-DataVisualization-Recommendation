import streamlit as st
import pandas as pd

st.title("This is a EDA WEBsite")
st.write("SJASDJAKLSDJALSKD")
file_input = st.file_uploader("Please put your CSV HERE")

if file_input is not None:
    df = pd.read_csv(file_input)
    if st.checkbox('Table Head'):
        n_lines = st.number_input('How many lines do you want to see?',min_value=1,step=1)
        selected_columns = df.columns
        selected_columns = st.multiselect('What columns do u want tu see?',df.columns)
        if len(selected_columns) == 0:
            st.write(df.head())
        else:
            st.write(df.head(n_lines)[selected_columns])
    if st.checkbox('null'):
        st.write(df.isnull().sum())
    if st.checkbox('Description'):
        st.write(df.describe())
    if st.checkbox('Table Shape'):
        st.write(f'The table has {df.shape[0]} lines and {df.shape[1]} columns')
    if st.checkbox('Type Columns'):
        st.write(df.dtypes)
    if st.checkbox('Filter dataframe'):
        filter_columns = st.multiselect('What columns will be your filter ?',df.columns)
        for column in filter_columns:
            possible_values = df[column].unique()
            filter_value = st.multiselect(f'Whats values you want in the {column}?',possible_values)
        #mask = df.columns[]
        #df.loc[]