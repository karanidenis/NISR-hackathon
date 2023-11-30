import pandas as pd
import plotly.express as px
import streamlit as st

from data_frames import read_table, file_path


def graph6():
    # Process the data to create separate DataFrames
    
    df = read_table(file_path, 'Table B.5', 'A', 'I', 2, 24)
    # Exclude the overall total row (usually the first row in the total_df)
    total_df = df.iloc[2:7].copy()
    male_df = df.iloc[9:14].copy()
    female_df = df.iloc[16:21].copy()

    # Resetting indices
    total_df.reset_index(drop=True, inplace=True)
    male_df.reset_index(drop=True, inplace=True)
    female_df.reset_index(drop=True, inplace=True)

    # Setting the educational level as the index
    total_df.set_index(df.columns[0], inplace=True)
    male_df.set_index(df.columns[0], inplace=True)
    female_df.set_index(df.columns[0], inplace=True)

    # Creating the combined DataFrame for plotting
    combined_df = pd.concat([
        total_df['Labour force'].rename('Total'),
        male_df['Labour force'].rename('Male'),
        female_df['Labour force'].rename('Female')
    ], axis=1)

    # Create the visualization\
    fig = px.bar(combined_df, barmode='group')
    fig.update_layout(title='Labour Force by Educational Level and Gender',
                      xaxis_title='Educational Level',
                      yaxis_title='Labour Force')

    # Display the visualization in Streamlit
    st.plotly_chart(fig)


