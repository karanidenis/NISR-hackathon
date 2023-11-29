from graph_3 import graph_3
from graph_1 import graph_1
import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide", page_title="Rwanda Labour Force Survey Dashboard",
#                    page_icon=":bar_chart:", initial_sidebar_state="expanded")

from graph2 import graph2
from graph_4 import graph4
from graph_3 import graph_3
from graph6 import graph6

# Load your data here for each graph
df_b1 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.1', skiprows=2)
df_b1.dropna(axis=1, how='all', inplace=True)
df_b1.dropna(axis=0, how='all', inplace=True)

df_b5 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.5', skiprows=1)
df_b5.dropna(axis=1, how='all', inplace=True)
df_b5.dropna(axis=0, how='all', inplace=True)

df_b7 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.7', skiprows=2)
df_b7.dropna(axis=1, how='all', inplace=True)
df_b7.dropna(axis=0, how='all', inplace=True)

df_b8 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.8', skiprows=2)
df_b8.dropna(axis=1, how='all', inplace=True)
df_b8.dropna(axis=0, how='all', inplace=True)

df_b17 = pd.read_excel('./data/labour_force_data.xlsx',
                       sheet_name='Table B.17', skiprows=2)
df_b17.dropna(axis=1, how='all', inplace=True)
df_b17.dropna(axis=0, how='all', inplace=True)

# Title container
# Graph container
with st.container():
    st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.
    """)

    # Define a list of graph functions
    graph_functions = [graph_1, graph2, graph_3, graph4, graph6]
    # Add other DataFrames like df_b2, df_b3, etc., to this list.
    dataframes = [df_b1, df_b5, df_b7, df_b17, df_b5]

    # Initialize session state for the index of the current graph
    if 'current_graph_index' not in st.session_state:
        st.session_state.current_graph_index = 0

    # Display the current graph
    current_graph_index = st.session_state.current_graph_index
    graph_functions[current_graph_index](dataframes[current_graph_index])

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Previous'):
        if st.session_state.current_graph_index > 0:
            st.session_state.current_graph_index -= 1
            st.experimental_rerun()

with col2:
    if st.button('Next'):
        if st.session_state.current_graph_index < len(graph_functions) - 1:
            st.session_state.current_graph_index += 1
            st.experimental_rerun()


