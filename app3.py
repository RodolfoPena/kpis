import streamlit as st
import pandas as pd


def find_id(df, title):
    index = df.index
    condition = df['title'] == title
    kpis_indices = index[condition]
    kpis_indices_list = kpis_indices.tolist()
    return kpis_indices_list

def get_data(df, kpi_id):
    title = df[df.index == kpi_id[0]]['title'].values[0]
    content = df[df.index == kpi_id[0]]['content'].values[0]
    formula = df[df.index == kpi_id[0]]['formula'].values[0]
    return title, content, formula

def app(df):
    st.title("KPI canvas")
    colA1, colA2 = st.beta_columns([2,1])
    kpi_title = colA2.selectbox('Seleccionar un KPI',  df['title'].values.tolist())
    kpi_id = find_id(df, kpi_title)
    title, content, formula = get_data(df, kpi_id)
    st.title(title)
    colB1, colB2= st.beta_columns(2)
    colB1.write(content)
    colB2.latex(formula)
    colC1, colC2, colC3 = st.beta_columns(3)
    colC1.write('hola')
    colC2.write('que tal')
    colC3.write('Aqui estamos')