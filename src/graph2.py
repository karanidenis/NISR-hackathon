from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from graph6 import graph6


def graph2():

    st.header("Impact of Education Level on Employment Statistics")

    # Assuming df_b5 is your DataFrame containing the data from Table B.5


    # Data for the unemployed population by level of education
    unemployed_data = {
        'Education_Level': ['Total', 'None', 'Primary', 'Lower_secondary', 'Upper_secondary', 'University'],
        'Total': [874876, 357109, 293168, 74611, 105424, 44565],
        'Male': [391587, 174271, 122029, 32734, 43710, 18842],
        'Female': [483289, 182838, 171138, 41877, 61713, 25723],
        'Urban': [265393, 77041, 56554, 30190, 61343, 40265],
        'Rural': [609483, 280068, 236613, 44421, 44081, 4300],
        'Participated': [327541, 141634, 132302, 28309, 23756, 1540],
        'Not participated': [547335, 215475, 160865, 46302, 81668, 43025]
    }

    # Data for the employed population by level of education
    employed_data = {
        'Education_Level': ['Total', 'None', 'Primary', 'Lower_secondary', 'Upper_secondary', 'University'],
        'Total': [3972193, 1825744, 1277562, 278889, 346961, 243037],
        'Male': [2248640, 994006, 769758, 157728, 186336, 140811],
        'Female': [1723553, 831738, 507804, 121161, 160625, 102226],
        'Urban': [1405959, 448242, 421828, 128546, 194297, 213046],
        'Rural': [2566234, 1377503, 855734, 150342, 152664, 29991],
        'Participated': [972074, 559028, 314831, 47071, 37023, 14121],
        'Not participated': [3000119, 1266716, 962731, 231818, 309938, 228916]
    }

    # Convert data to dataframes
    unemployed_df = pd.DataFrame(unemployed_data)
    employed_df = pd.DataFrame(employed_data)

    # Create subplots: one for unemployed data, one for employed data
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "Unemployed by Education Level", "Employed by Education Level"))

    # Add traces for unemployed data
    fig.add_trace(
        go.Bar(x=unemployed_df['Education_Level'],
               y=unemployed_df['Total'], name='Unemployed Total'),
        row=1, col=1
    )
    # ... Add other unemployed traces if needed ...

    # Add traces for employed data
    # Add traces for employed data
    fig.add_trace(
        go.Bar(x=employed_df['Education_Level'],
               y=employed_df['Total'], name='Employed Total'),
        row=1, col=2
    )
    # Optionally add more traces for different categories (Male, Female, etc.)

    # Update layout for clear visibility and unified look
    fig.update_layout(
        title_text="Employment Status by Education Level",
        barmode='group',
        height=600,
        # Since we are in Streamlit, we don't need to set a fixed width. Streamlit will take care of it.
    )

    # Render the plot in Streamlit
    graph6()
    st.plotly_chart(fig)
    

    st.markdown("""
    The chart above illustrates the correlation between the level of education and various labour market statistics
    for the population aged 16 and over. Higher levels of education tend to be associated with higher labour force
    participation rates and employment-to-population ratios, alongside lower unemployment rates.
    """)
    
    st.markdown("------------------------------------------------------------")