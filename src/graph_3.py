import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Function to create the bar chart


def graph3():
    st.header("Gender disparities in labour market outcomes")

    # Read the data from the Excel file
    df = pd.read_excel('./data/labour_force_data.xlsx',
                       sheet_name='Table B.8', skiprows=2)
    # Drop rows and columns with all NaN values
    df = df.dropna(axis=1, how='all').dropna(axis=0, how='all')
    # Reset index if necessary
    df.reset_index(drop=True, inplace=True)

    # Define the columns for the bar chart
    df.columns = ['Occupation_Group', 'Total', 'Male', 'Female',
                  'Urban', 'Rural', 'Participated', 'Not participated']

    # Sidebar widget for gender selection
    selected_gender = st.sidebar.radio(
        "Select Gender", ["Both", "Male", "Female"])

    # Plotting the bar chart using Plotly
    fig_b8 = go.Figure()

    if selected_gender == "Both":
        fig_b8.add_trace(go.Bar(
            x=df['Occupation_Group'],
            y=df['Male'],
            name='Male',
            marker_color='blue'
        ))
        fig_b8.add_trace(go.Bar(
            x=df['Occupation_Group'],
            y=df['Female'],
            name='Female',
            marker_color='magenta'
        ))
    else:
        fig_b8.add_trace(go.Bar(
            x=df['Occupation_Group'],
            y=df[selected_gender],
            name=selected_gender,
            marker_color='blue' if selected_gender == "Male" else 'magenta'
        ))

    # Customize layout with a title and axis labels
    fig_b8.update_layout(
        title="Gender Disparities in Labour Market by Occupation Group",
        xaxis_title="Occupation Group",
        yaxis_title="Number of Employed Persons",
        barmode='group',
        margin=dict(l=60, r=60, t=50, b=50)
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig_b8)

    # Summary
    st.markdown("""
    The visualization above demonstrates the gender disparities across different occupation groups in Rwanda's labor market. 
    Significant disparities are evident in several sectors. For instance, 'Service and sales workers' 
    show a higher female representation, while 'Craft and related trades workers', 'Elementary occupations' and 'Plant and machine operators and assemblers' 
    are predominantly male-dominated. The data suggests a need for gender-targeted policies in occupational sectors to ensure 
    equitable employment opportunities.
    """)
    st.markdown("------------------------------------------------------------")


# Run the graph3 function when the script is executed
if __name__ == '__main__':
    graph3()
