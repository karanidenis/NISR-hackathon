from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def graph4():
    st.header("Labour Force Statistics by Age Group")

    # Assuming df_b7 is your DataFrame containing the data from Table B.7
    # You would load your data here
    # df_b7 = pd.read_csv('path_to_your_csv.csv')

    # For demonstration purposes, we're creating a sample dataframe.
    employed_population_data = {
        'Age_Group': [
            'Total', '15-19 yrs', '20-24 yrs', '25-29 yrs', '30-34 yrs',
            '35-39 yrs', '40-44 yrs', '45-49 yrs', '50-54 yrs', '55-59 yrs', '60-64 yrs'
        ],
        'Total': [3972193, 322790, 586840, 603320, 567053, 540358, 489003, 295037, 221177, 135729, 130148],
        'Male': [2248640, 182765, 350693, 333086, 322444, 302996, 287918, 154501, 117691, 69726, 75328],
        'Female': [1723553, 140025, 236147, 270234, 244610, 237362, 201086, 140536, 103486, 66004, 54820],
        'Urban': [1405959, 89475, 206420, 223444, 236013, 216230, 171792, 103190, 70905, 40266, 30984],
        'Rural': [2566234, 233315, 380420, 379876, 331041, 324128, 317212, 191848, 150273, 95463, 99164],
    }

    df_employed_b7 = pd.DataFrame(employed_population_data)

    # Sidebar widget for age group selection
    selected_sex = st.sidebar.selectbox(
        'Select Sex for employed population', ['Total', 'Male', 'Female'])

    # If 'Total' is selected, we show data for both Male and Female.
    if selected_sex == 'Total':
        filtered_df = df_employed_b7.copy()
    else:
        filtered_df = df_employed_b7[['Age_Group', selected_sex]]

    # Create the bar chart using Plotly
    fig = go.Figure()

    # Add trace for the selected sex
    fig.add_trace(go.Bar(
        x=filtered_df['Age_Group'],
        y=filtered_df[selected_sex],
        name=selected_sex
    ))

    # Customize layout with a title and axis labels
    fig.update_layout(
        title=f"Employment Statistics by Age Group - {selected_sex}",
        xaxis_title="Age Group",
        yaxis_title="Number of Employed Persons",
        barmode='group',
        legend_title="Sex"
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig)

    # Summary
    st.markdown(f"""
    The bar chart displays the distribution of employed persons across different age groups for the selected sex category.
    This interactive feature allows us to observe trends and patterns in employment, such as which age groups have higher or lower
    employment rates, and how these patterns differ between males and females.
    """)

    # Assuming df_b17 is your DataFrame containing the data from Table B.17
    # You would load your data here
    # df_b17 = pd.read_csv('path_to_your_csv.csv')

    # For demonstration purposes, we're creating a sample dataframe.
    unemployed_population_data = {
        'Age_Group': [
            'Total', '16-24 yrs', '25-34 yrs', '35-54 yrs', '55-64 yrs', '65+ yrs'
        ],
        'Total': [874876, 280990, 268769, 283066, 36253, 5799],
        'Male': [391587, 147422, 87766, 134292, 18178, 3929],
        'Female': [483289, 133569, 181002, 148775, 18074, 1870],
        'Urban': [265393, 88112, 87171, 81989, 5588, 2534],
        'Rural': [609483, 192878, 181598, 201077, 30665, 3265],
    }


    df_employed_b17 = pd.DataFrame(unemployed_population_data)

    # Sidebar widget for age group selection
    sex = st.sidebar.selectbox(
        'Select Sex for Unemployed population', ['Total', 'Male', 'Female'], key='sex_select')

    # If 'Total' is selected, we show data for both Male and Female.
    if sex == 'Total':
        filtered_df = df_employed_b17.copy()
    else:
        filtered_df = df_employed_b17[['Age_Group', sex]]

    # Create the bar chart using Plotly
    fig = go.Figure()

    # Add trace for the selected sex
    fig.add_trace(go.Bar(
        x=filtered_df['Age_Group'],
        y=filtered_df[sex],
        name=sex
    ))

    # Customize layout with a title and axis labels
    fig.update_layout(
        title=f"Unemployment Statistics by Age Group - {sex}",
        xaxis_title="Age Group",
        yaxis_title="Number of Unemployed Persons",
        barmode='group',
        legend_title="Sex"
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig)

    # Summary
    st.markdown(f"""
    The bar chart displays the distribution of unemployed persons across different age groups for the selected sex category.
    This interactive feature allows us to observe trends and patterns in unemployment, such as which age groups have higher or lower
    uemployment rates, and how these patterns differ between males and females.
    """)
    
    st.markdown("------------------------------------------------------------")
