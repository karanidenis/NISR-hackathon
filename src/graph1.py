from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def graph1():
    
# General Labor Force Stats
    st.header("General Labour Force Statistics")

    # Sidebar widget for area of residence selection
    area = st.sidebar.selectbox('Select Area of Residence', [
                                'Total', 'Male', 'Female', 'Urban', 'Rural', 'Participated', 'Not participated'])

    # Assuming df_b1 is your DataFrame containing the data from Table B.1
    # You would load your data here
    # df_b1 = pd.read_csv('path_to_your_csv.csv')

    # For demonstration purposes, we're creating a sample dataframe.
    df_b1 = pd.DataFrame({
        'Indicators': ['Working age population (16+ years)', 'Labour force', 'Employed', 'Unemployed', 'Out of labour force'],
        'Total': [8100430, 4847069, 3972193, 874876, 3253361],
        'Male': [3798558, 2640227, 2248640, 391587, 1158332],
        'Female': [4301872, 2206843, 1723553, 483289, 2095029],
        'Urban': [2441445, 1671352, 1405959, 265393, 770093],
        'Rural': [5658985, 3175717, 2566234, 609483, 2483267],
        'Participated': [2521332, 1299616, 972074, 327541, 1221716],
        'Not participated': [5579098, 3547454, 3000119, 547335, 2031645]
    })

    # Filter the DataFrame based on the selected area
    filtered_df = df_b1[['Indicators', area]]

    # Create the bar chart with the filtered data
    fig_b1 = px.bar(filtered_df, x='Indicators', y=area,
                    title=f'Labour Force Indicators in Rwanda - {area}')
    st.plotly_chart(fig_b1)
    
    st.markdown("------------------------------------------------------------")