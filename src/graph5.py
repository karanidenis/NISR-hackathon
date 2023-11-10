import streamlit as st
import pandas as pd
import plotly.express as px

from data_frames import read_table, file_path, TABLE_B1

# Function to create the plot


def graph5():
    st.header("General working-age population distribution (16+ years)")
    # Sidebar widget for area of residence selection
    st.sidebar.selectbox('Gender', ['Male', 'Female'])
    # Adjust these parameters as needed for your Excel file
    df = read_table(file_path, TABLE_B1, 'A', 'D', 3, 7)
    # Convert the number columns to integers to remove any decimals
    df['Total'] = df['Total'].astype(int)
    df['Male'] = df['Male'].astype(int)
    df['Female'] = df['Female'].astype(int)

    # print the dataframe for debugging
    print(df)

    # Get the total working-age population which is the first row's 'Total' after converting to int
    total_working_age_population = df.iloc[0, 1]
    print(total_working_age_population)

    # Drop the rows that are not needed (e.g., headers or subtotals)
    df = df.drop([0, 1])  # adjust indices accordingly

    # Ensure the DataFrame has the category names
    df.rename(columns={df.columns[0]: 'Category'}, inplace=True)

    # Add a 'Gender Distribution' column for hover data
    df['Gender Distribution'] = df.apply(
        lambda x: f"Male: {x['Male']}, Female: {x['Female']}", axis=1)

    # Drop unnecessary columns to simplify the DataFrame
    df = df[['Category', 'Total', 'Gender Distribution']].rename(columns={
        'Total': 'Total'})

    # Creating the pie chart using Plotly Express
    fig = px.pie(df, values='Total', names='Category', hover_data=['Gender Distribution'],
                 )

    # Customize the pie chart to show labels and percentage
    fig.update_traces(textposition='inside', textinfo='percent+label')

    # Add annotation for the total working-age population
    fig.add_annotation(text=f"Total Working-Age Population: {total_working_age_population:,}",
                       x=0.5, y=1.15, showarrow=False, font_size=18, xanchor='center', yanchor='top')

    # Adjust the layout to make space for the annotation
    fig.update_layout(margin=dict(t=100))

    # Display the chart using Streamlit
    st.plotly_chart(fig)
    summary_text = """
    This chart visualizes the employment distribution within the working-age population. Each slice represents a category of the labor force, including those who are employed, unemployed, and out of the labor force.
    """
    st.markdown(summary_text)
    st.markdown("------------------------------------------------------------")


if __name__ == "__main__":
    graph5()
