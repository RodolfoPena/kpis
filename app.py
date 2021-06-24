import app1
import app2
import app3
import streamlit as st
from  gsheetsdb import connect
import pandas as pd


conn = connect()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)




def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

def create_dataframe():
    sheet_url = st.secrets["public_gsheets_url"]
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    df = pd.DataFrame()
    for data in rows:
        # Ajustar aquí en función de las columnas
        row = {
            'id': data.id, 
            'title': data.title, 
            'content': data.content, 
            'type':data.type, 
            'formula': data.formula, 
            'dependency': data.dependency,
            'region': data.region,
            'area': data.area,
            'iata_chapter': data.iata_chapter,
            'frequency': data.frequency,
            'source': data.source,
            'target': data.target,
            'users': data.users,
            'data_owner': data.data_owner,
            'clients': data.clients
            }
        df = df.append(row, ignore_index=True)
    return df

st.set_page_config(
    page_title="Aerosan",
    page_icon="ExOp",
    layout="wide",
    initial_sidebar_state="expanded",
)

local_css("style.css")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

PAGES = {
    "KPI contexto": app1,
    "KPI árbol": app2,
    "KPI canvas": app3
}

st.sidebar.title('Navegación')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]

df = create_dataframe()
page.app(df)





# st.sidebar.title("KPI's Aerosan")
# st.sidebar.write('A continuación se presenta un levantamiento de los KPIs disponibles en Aerosan')
# st.sidebar.selectbox('Proceso', ['Importaciones', 'Exportaciones', 'Deposito Aduanero'])


# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)













 

