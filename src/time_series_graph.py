import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data_frames import read_table

colors = ['#006af9', '#008080', '#ff7f50']


def time_series_graph(df):
    # Set the title of the web app
    # st.title('Unemployment Rate (2016 - 2023)')

    # Sidebar tabs for navigation

    # get the first 6 columns from df
    df1 = df.iloc[:, :6]
    tab_selector = st.sidebar.selectbox(
        'Select view mode', ['Graph', 'Data'], key="graphshow")
    selected_option = st.sidebar.selectbox(
        'Select Option', ['Female Vs Male', 'Urban vs Rural', 'Total'], index=0, key="graphoption2")

    if tab_selector == 'Graph':

        # Plot based on selected option
        if selected_option == 'Female Vs Male':
            # Plot both Male and Female lines with markers
            fig = px.line(df1, x='Years', y=['Male', 'Female'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=[colors[0], colors[2]])
        elif selected_option == 'Urban vs Rural':
            # Plot both Urban and Rural lines with markers
            fig = px.line(df1, x='Years', y=['Urban', 'Rural'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['blue', 'green'])
        elif selected_option == 'Total':
            # Plot the Total line with markers
            fig = px.line(df1, x='Years', y='Total', labels={'value': 'Y-axis'}, line_dash_sequence=['solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=[colors[1]])

        fig.update_layout(title='Unemployment Rate (2016 - 2023)',
                          xaxis_title='Years', yaxis_title='Unemployment Rate (%)')
        fig.update_yaxes(range=[0, 80])
        fig.update_xaxes(tickangle=-60, showline=True,  linecolor='black')

        st.plotly_chart(fig)
        # ========================

        st.markdown("""The Unemployment Rate is relatively high among females. 
                    There is closely equal unemployment rate between urban and rural areas.
                    """)

    # trim the last 6 columns of df
    df_employment_pop_ratio = df.iloc[:, 6:]
    # rename column name "Years.1" to "Years"
    df_employment_pop_ratio.rename(columns={'Years.1': 'Years', 'Total.1': 'Total', 'Male.1': 'Male',
                                            'Female.1': 'Female', 'Urban.1': 'Urban', 'Rural.1': 'Rural'}, inplace=True)

    # print("df_employement_pop_ratio")
    # print(df_employment_pop_ratio)
    if tab_selector == 'Graph':
        if selected_option == 'Female Vs Male':
            # Plot both Male and Female lines with markers
            fig2 = px.line(df_employment_pop_ratio, x='Years', y=['Male', 'Female'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                           line_shape='linear', markers=True, color_discrete_sequence=[colors[0], colors[2]])
        elif selected_option == 'Urban vs Rural':
            # Plot both Urban and Rural lines with markers
            fig2 = px.line(df_employment_pop_ratio, x='Years', y=['Urban', 'Rural'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                           line_shape='linear', markers=True, color_discrete_sequence=['blue', 'green'])
        elif selected_option == 'Total':
            # Plot the Total line with markers
            fig2 = px.line(df_employment_pop_ratio, x='Years', y='Total', labels={'value': 'Y-axis'}, line_dash_sequence=['solid'],
                           line_shape='linear', markers=True, color_discrete_sequence=[colors[1]])

        fig2.update_layout(title='Employement to Population Ratio (16+ years) (2016 - 2023)',
                           xaxis_title='Years', yaxis_title='Employment Rate (%)')
        fig2.update_yaxes(range=[0, 80])
        fig2.update_xaxes(tickangle=-60)
        st.plotly_chart(fig2)

    elif tab_selector == 'Data':
        # Display data on the second tab
        st.subheader('Raw Data:')
        st.dataframe(df1)
        st.dataframe(df_employment_pop_ratio)
