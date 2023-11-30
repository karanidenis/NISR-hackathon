import pandas as pd
import plotly.express as px
import streamlit as st

from data_frames import read_table, file_path

# Streamlit app

def graph3(df):
    # Read the table using the provided function
    teal = '#FF7F50'
    dark_blue = '#008080'
    light_blue = '#006af9'
    colors = [dark_blue, light_blue, teal]
    # Process the data to create separate DataFrames
    # Exclude the overall total row (usually the first row in the total_df)
    total_df = df.iloc[2:7].copy()  # Adjusted to exclude the overall total
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
    fig = px.bar(combined_df, barmode='group', color_discrete_sequence=colors)
    fig.update_layout(title='Labour Force by Educational Level and Gender',
                      xaxis_title='Educational Level',
                      yaxis_title='Labour Force')

    # Display the visualization in Streamlit
    st.plotly_chart(fig)


if __name__ == "__main__":
    df = read_table(file_path, 'Table B.5', 'A', 'I', 2, 24)
    graph3(df)
