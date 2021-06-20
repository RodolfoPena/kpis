import streamlit as st
from  gsheetsdb import connect
import pandas as pd
import graphviz as graphviz



def create_graph(df):
    graph = graphviz.Digraph()
    for index, row in df.iterrows():
        if row['dependency'] != None:
            graph.edge(row['title'], df[df['id'] == row['dependency']]['title'].values[0])
    return graph

def app(df):
    st.title('KPI tree')
    st.write('A continuación se presenta el árbol de KPIs')
    graph = create_graph(df)
    st.graphviz_chart(graph)
