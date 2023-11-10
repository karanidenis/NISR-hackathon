from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def graph3():
    st.header("Gender disparities in labour market outcomes")

    employed_data_b8 = {
        'Occupation_Group': [
            'Total', 'Managers', 'Professionals', 'Technicians_and_associate_professionals',
            'Clerical_support_workers', 'Service_and_sales_workers',
            'Skilled_agricultural_forestry_and_fishery_workers',
            'Craft_and_related_trades_workers', 'Plant_and_machine_operators_and_assemblers',
            'Elementary_occupations'
        ],
        'Male': [2248640, 21065, 159306, 20100, 11104, 324510, 99776, 273962, 105903, 1232913],
        'Female': [1723553, 16745, 99358, 8781, 18491, 396234, 84648, 91998, 4045, 1003253]
    }

    df_employed_b8 = pd.DataFrame(employed_data_b8)

    # Plotting the bar chart using Plotly
    fig_b8 = go.Figure()

    fig_b8.add_trace(go.Bar(
        x=df_employed_b8['Occupation_Group'],
        y=df_employed_b8['Male'],
        name='Male',
        marker_color='blue'
    ))

    fig_b8.add_trace(go.Bar(
        x=df_employed_b8['Occupation_Group'],
        y=df_employed_b8['Female'],
        name='Female',
        marker_color='magenta'
    ))

    # Customize layout with a title and axis labels
    fig_b8.update_layout(
        title="Gender Disparities in Labour Market by Occupation Group",
        xaxis_title="Occupation Group",
        yaxis_title="Number of Employed Persons",
        barmode='group',
        margin=dict(l=60, r=60, t=50, b=50)  # Adjust margins to fit the title
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