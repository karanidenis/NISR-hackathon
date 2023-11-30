from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import streamlit as st

from graph_6 import graph6


def graph2(df):
    st.sidebar.radio('Select Gender', [
        'Male', 'Female'])
    st.header("Impact of Education Level on Employment Statistics")
    graph6()

    # Process data for subplots
    # Skip the first row which is a header
    education_levels = df['Unnamed: 0'][1:7]
    unemployed_df = df['Unemployed'][1:7]
    employed_df = df['Employed'][1:7]
    # Create subplots: one for unemployed data, one for employed data
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "Unemployed by Education Level", "Employed by Education Level"))

    # Add traces for unemployed data
    fig.add_trace(
        go.Bar(x=education_levels,
               y=unemployed_df, name='Unemployed Total'),
        row=1, col=1
    )

    # Add traces for employed data
    fig.add_trace(
        go.Bar(x=education_levels,
               y=employed_df, name='Employed Total'),
        row=1, col=2
    )

    # Update layout for clear visibility and unified look
    fig.update_layout(
        title_text="Employment Status by Education Level",
        barmode='group',
        height=600,
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig)

    st.markdown("""
    The chart above illustrates the correlation between the level of education and various labour market statistics
    for the population aged 16 and over. Higher levels of education tend to be associated with higher labour force
    participation rates and employment-to-population ratios, alongside lower unemployment rates.
    """)

    st.markdown("------------------------------------------------------------")


# Run the app
if __name__ == '__main__':
    # Load your data here or pass the DataFrame to the function
    df = pd.read_excel('./data/labour_force_data.xlsx',
                       sheet_name='Table B.5', skiprows=1)
    df = df.dropna(axis=1, how='all')  # Drop empty columns
    df = df.dropna(axis=0, how='all')  # Drop empty rows
    graph2(df)
