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
    dependency = df[df.index == kpi_id[0]]['dependency'].values[0]
    region = df[df.index == kpi_id[0]]['region'].values[0]
    area = df[df.index == kpi_id[0]]['area'].values[0]
    iata_chapter = df[df.index == kpi_id[0]]['iata_chapter'].values[0]
    frequency = df[df.index == kpi_id[0]]['frequency'].values[0]
    source = df[df.index == kpi_id[0]]['source'].values[0]
    target = df[df.index == kpi_id[0]]['target'].values[0]
    users = df[df.index == kpi_id[0]]['users'].values[0]
    data_owner = df[df.index == kpi_id[0]]['data_owner'].values[0]
    clients = df[df.index == kpi_id[0]]['clients'].values[0]
    return title, content, formula, dependency, region, area, iata_chapter, frequency, source, target, users, data_owner, clients

def app(df):
    st.title("KPI canvas")
    colA1, colA2 = st.beta_columns([2,1])
    kpi_title = colA2.selectbox('Seleccionar un KPI',  df['title'].values.tolist())
    kpi_id = find_id(df, kpi_title)
    title, content, formula, dependency, region, area, iata_chapter, frequency, source, target, users, data_owner, clients = get_data(df, kpi_id)
    st.title(title)
    colB1, colB2= st.beta_columns(2)
    colB1.subheader('Descripción')
    colB1.write(content)
    colB2.subheader('Formula')
    colB2.latex(formula)
    colC1, colC2, colC3 = st.beta_columns(3)
    colC1.subheader('Region')
    colC1.write(region)
    colC2.subheader('Area')
    colC2.write(area)
    colC3.subheader('Proceso IATA')
    colC3.write(iata_chapter)
    colD1, colD2, colD3 = st.beta_columns(3)
    colD1.subheader('Objetivo')
    colD1.write(target)
    colD2.subheader('Fuentes')
    colD2.write(source)
    colD3.subheader('Usuarios')
    colD3.write(users)
