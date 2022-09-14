import streamlit as st
import pandas as pd

st.title('🎈 Sample Streamlit ')


default_url = 'https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv'
st.sidebar.subheader('Input')
data_url = st.sidebar.text_input('URL', default_url)

if data_url:
    st.subheader('Output')
    st.warning(f'current url input {data_url}')
    df = pd.read_csv(data_url)
    
    # can do EDA with Streamlit
    # get last column
    df_last_column = df.iloc[:,-1]
    df_option = df_last_column.unique()
    option = st.selectbox(
     'Select a Class Value',
      df_option)
    df_show = df[df_last_column == option] 
    st.write('You selected:', option)
    st.write(df_show)
    column_names = df_show.columns[-1]
    df_species_mean = df_show.groupby(column_names).mean()
    st.write(df_species_mean)
    st.bar_chart(df_species_mean)
else:
    st.subheader('Enter your input')
    st.error('Wait for your input!')