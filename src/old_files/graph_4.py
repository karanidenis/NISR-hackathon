import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def graph4(df):
    st.header("Gender disparities in labour market outcomes")

    # Clean data
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    df_b7 = df
    df_b17 = df
    # Rename the first column to 'Occupation_Group' for consistency
    df_b7.columns = ['Occupation_Group'] + df_b7.columns[1:].tolist()
    df_b17.columns = ['Occupation_Group'] + df_b17.columns[1:].tolist()

    # Sidebar for gender selection
    gender_options = ['Total', 'Male', 'Female']
    selected_gender = st.sidebar.radio('Select Gender', gender_options)

    # Plot for Table B.7
    fig_b7 = go.Figure()

    if selected_gender == 'Total':
        # Include both 'Male' and 'Female' data
        fig_b7.add_trace(go.Bar(
            x=df_b7['Occupation_Group'], y=df_b7['Male'], name='Male', 
            # marker_color='blue'
            ))
        fig_b7.add_trace(go.Bar(
            x=df_b7['Occupation_Group'], y=df_b7['Female'], name='Female',
            # marker_color='red'
            ))
    else:
        # Only include the selected gender data
        fig_b7.add_trace(go.Bar(
            x=df_b7['Occupation_Group'], y=df_b7[selected_gender], name=selected_gender))

    fig_b7.update_layout(title=f"Employment Statistics - {selected_gender}",
                         xaxis_title='Occupation Group', yaxis_title='Number of Persons')
    st.plotly_chart(fig_b7)

    # Summary
    st.markdown(f"""
    The bar chart displays the distribution of employed persons across different age groups for the selected sex category.
    This interactive feature allows us to observe trends and patterns in employment, such as which age groups have higher or lower
    employment rates, and how these patterns differ between males and females.
    """)

    # Plot for Table B.17
    fig_b17 = go.Figure()

    if selected_gender == 'Total':
        # Include both 'Male' and 'Female' data
        fig_b17.add_trace(go.Bar(
            x=df_b17['Occupation_Group'], y=df_b17['Male'], name='Male', 
            # marker_color='blue'
            ))
        fig_b17.add_trace(go.Bar(
            x=df_b17['Occupation_Group'], y=df_b17['Female'], name='Female',
            # marker_color='red'
            ))
    else:
        # Only include the selected gender data
        fig_b17.add_trace(go.Bar(
            x=df_b17['Occupation_Group'], y=df_b17[selected_gender], name=selected_gender))

    fig_b17.update_layout(
        title=f"Unemployment Statistics - {selected_gender}", xaxis_title='Occupation Group', yaxis_title='Number of Persons', margin=dict(l=60, r=60, t=50, b=50))
    st.plotly_chart(fig_b17)

    # Summary
    st.markdown(f"""
    The bar chart displays the distribution of unemployed persons across different age groups for the selected sex category.
    This interactive feature allows us to observe trends and patterns in unemployment, such as which age groups have higher or lower
    uemployment rates, and how these patterns differ between males and females.
    """)


if __name__ == '__main__':
    # Load data
    df = pd.read_excel('data/labour_force_data.xlsx',
                       sheet_name='Table B.7', skiprows=2)
    # drop last row
    df = df.iloc[:-1]
    df = pd.read_excel('data/labour_force_data.xlsx',
                       sheet_name='Table B.17', skiprows=2)
    #  drop last row
    df = df.iloc[:-1]
    graph4(df)
