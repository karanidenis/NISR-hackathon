# streamlit_app.py
import streamlit as st
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from graph1 import graph1
from graph2 import graph2
from graph3 import graph3
from graph4 import graph4
from graph5 import graph5

# Set page config to wide mode for a better layout.
st.set_page_config(layout="wide", page_title="Rwanda Labour Force Survey Dashboard",
                   page_icon=":bar_chart:", initial_sidebar_state="expanded", )

# Creating a container for the title
title_container = st.container()
with title_container:
    st.title("Rwanda Labour Force Survey Dashboard 2023:Q3")

# Creating a container for the graphs
graph_container = st.container()

# Introduction or Summary inside the graph container
with graph_container:
    st.markdown("""
            This dashboard provides insights into Rwanda's labour force dynamics, 
            highlighting the relationship between educational attainment, gender, and age-group with employment statistics.""")

    # Define a list of graph functions
    graphs = [graph5,
              #   graph1,
              graph2,
              graph3,
              graph4]

    # Initialize session state for the index of the current graph
    if 'current_graph_index' not in st.session_state:
        st.session_state.current_graph_index = 0

    # Display the current graph
    graphs[st.session_state.current_graph_index]()

# Creating a container for navigation buttons
button_container = st.container()
with button_container:
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Previous'):
            if st.session_state.current_graph_index > 0:
                st.session_state.current_graph_index -= 1
                st.experimental_rerun()

    with col2:
        if st.button('Next'):
            if st.session_state.current_graph_index < len(graphs) - 1:
                st.session_state.current_graph_index += 1
                st.experimental_rerun()
