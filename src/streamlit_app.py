# Set page configuration
# from graph4 import graph4
from data_frames import read_table
from graph5 import graph5
from graph2 import graph2
from graph1 import graph1
from graph4 import graph_4
from graph3 import graph3
import streamlit as st
import pandas as pd

from time_series_graph import time_series_graph


# Load your data here for each graph
df_b1 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.1', skiprows=2)
df_b1.dropna(axis=1, how='all', inplace=True)
df_b1.dropna(axis=0, how='all', inplace=True)

df_b5 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.5', skiprows=1)
df_b5.dropna(axis=1, how='all', inplace=True)
df_b5.dropna(axis=0, how='all', inplace=True)

df_7 = pd.read_excel('./data/labour_force_data.xlsx',
                     sheet_name='Table B.7', skiprows=2)
df_7.dropna(axis=1, how='all', inplace=True)
df_7.dropna(axis=0, how='all', inplace=True)

df_b8 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.8', skiprows=2)
df_b8.dropna(axis=1, how='all', inplace=True)
df_b8.dropna(axis=0, how='all', inplace=True)

df_17 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.17', skiprows=2)
df_17.dropna(axis=1, how='all', inplace=True)
df_17.dropna(axis=0, how='all', inplace=True)

df_time_series = read_table(
    "./data/labour_force_data.xlsx",  "Table 0", "A", "L", 3, 27)

# Title container
with st.container():
    st.title("Rwanda Labour Force Survey Dashboard 2023:Q3")

# Graph container
with st.container():
    st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.
    """)

    # Define a list of graph functions
    graph_functions = [graph1, time_series_graph,
                       graph2, graph3, graph5, graph_4]
    # Add other DataFrames to this list
    dataframes = [df_b1, df_time_series, df_b5, df_b5, df_7, df_17, df_b8]

    # Initialize session state for the index of the current graph
    if 'current_graph_index' not in st.session_state:
        st.session_state.current_graph_index = 0

    # Display the current graph
    current_graph_index = st.session_state.current_graph_index

    # Call the current graph function with appropriate parameters
    for i in range(len(graph_functions)):
        if i == current_graph_index:
            if i == 4:  # Special case for graph3
                graph_functions[i](df_7, df_17)
            elif i == 5:  # Special case for graph4
                graph_functions[i](df_b8)
            else:
                graph_functions[i](dataframes[i])

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
