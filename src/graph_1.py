import pandas as pd
import plotly.express as px
import streamlit as st

# the path to your Excel file
file_path = './data/labour_force_data.xlsx'

# Replace 'Sheet1' with your specific sheet name if needed
sheet_name = 'Table B.1'

# Read the Excel file, skipping the first two rows
df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2)
df = df.dropna(axis=1, how='all')  # Drop empty columns
df = df.dropna(axis=0, how='all')  # Drop empty rows

# Function to create and display the graph


def graph1(df):
    st.header("General Labour Force Statistics")

    # Sidebar widget for area of residence selection
    area = st.sidebar.selectbox('Select Area of Residence', [
                                'Total', 'Male', 'Female', 'Urban', 'Rural'])

    # Adjust the DataFrame to match the required structure
    df_slice = df.iloc[2:5]
    df_adjusted = pd.DataFrame({
        'Indicators': df_slice['Unnamed: 0'],
        'Total': df_slice['Total'],
        'Male': df_slice['Male'],
        'Female': df_slice['Female'],
        'Urban': df_slice['Urban'],
        'Rural': df_slice['Rural']
    })

    # Filter the DataFrame based on the selected area
    filtered_df = df_adjusted[['Indicators', area]]

    # # Create the bar chart with the filtered data
    # fig_b1 = px.bar(filtered_df, x='Indicators', y=area,
    #                 title=f'Labour Force Indicators in Rwanda - {area}')
    # st.plotly_chart(fig_b1)

    # Create a pie chart with the filtered data
    fig_pie = px.pie(filtered_df, values=area, names='Indicators',
                     title=f'Labour Force Distribution - {area}')
    st.plotly_chart(fig_pie)

    st.markdown("------------------------------------------------------------")


# Run the app
if __name__ == '__main__':
    graph1(df)
