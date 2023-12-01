import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data_frames import read_table


tab_selector = st.sidebar.radio('Show', ['Graph', 'Data'], key="graphshow")
selected_option = st.sidebar.selectbox(
    'Select Option', ['Female Vs Male', 'Urban vs Rural', 'Total'], index=0, key="graphoption")

df_employment_pop_ratio = read_table(
    "./data/labour_force_data.xlsx",  "Table 0", "G", "L", 3, 27)


# def employment_rate(df):
#     if tab_selector == 'Graph':

#         # Get the selected option from dropdown

#         # Plot based on selected option
#         if selected_option == 'Female Vs Male':
#             # Plot both Male and Female lines with markers
#             fig = px.line(df, x='Years', y=['Male', 'Female'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
#                           line_shape='linear', markers=True, color_discrete_sequence=['blue', 'green'])
#         elif selected_option == 'Urban vs Rural':
#             # Plot both Urban and Rural lines with markers
#             fig = px.line(df, x='Years', y=['Urban', 'Rural'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
#                           line_shape='linear', markers=True, color_discrete_sequence=['purple', 'orange'])
#         elif selected_option == 'Total':
#             # Plot the Total line with markers
#             fig = px.line(df, x='Years', y='Total', labels={'value': 'Y-axis'}, line_dash_sequence=['solid'],
#                           line_shape='linear', markers=True, color_discrete_sequence=['red'])

#         # Customize the chart
#         # fig.update_layout(title='Gender and Residence Data Visualization')

#         # Add trace for the x-axis
#         fig.add_trace(go.Scatter(x=df['Years'], y=df['Years'], mode='lines',
#                                  name='Years', line=dict(color='black', dash='dash')))
#         fig.update_layout(title='Unemployment Rate (2016 - 2023)',
#                           xaxis_title='Years', yaxis_title='Unemployment Rate (%)')
#         fig.update_yaxes(range=[0, 60])
#         fig.update_xaxes(tickangle=-60)

#         st.plotly_chart(fig)

#     elif tab_selector == 'Data':
#         # Display data on the second tab
#         st.subheader('Sample Data:')
#         st.dataframe(df)


def time_series_graph(df):
    # Set the title of the web app
    # st.title('Unemployment Rate (2016 - 2023)')

    # Sidebar tabs for navigation

    if tab_selector == 'Graph':

        # Get the selected option from dropdown
        selected_option = st.sidebar.selectbox(
            'Select Option', ['Female Vs Male', 'Urban vs Rural', 'Total'], index=0)

        # Plot based on selected option
        if selected_option == 'Female Vs Male':
            # Plot both Male and Female lines with markers
            fig = px.line(df, x='Years', y=['Male', 'Female'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['blue', 'green'])
        elif selected_option == 'Urban vs Rural':
            # Plot both Urban and Rural lines with markers
            fig = px.line(df, x='Years', y=['Urban', 'Rural'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['purple', 'orange'])
        elif selected_option == 'Total':
            # Plot the Total line with markers
            fig = px.line(df, x='Years', y='Total', labels={'value': 'Y-axis'}, line_dash_sequence=['solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['red'])

        # Customize the chart
        # fig.update_layout(title='Gender and Residence Data Visualization')

        # Add trace for the x-axis
        fig.add_trace(go.Scatter(x=df['Years'], y=df['Years'], mode='lines',
                                 name='Years', line=dict(color='black', dash='dash')))
        fig.update_layout(title='Unemployment Rate (2016 - 2023)',
                          xaxis_title='Years', yaxis_title='Unemployment Rate (%)')
        fig.update_yaxes(range=[0, 60])
        fig.update_xaxes(tickangle=-60)
        st.plotly_chart(fig)
        # ========================

        if selected_option == 'Female Vs Male':
            # Plot both Male and Female lines with markers
            fig2 = px.line(df_employment_pop_ratio, x='Years', y=['Male', 'Female'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['blue', 'green'])
        elif selected_option == 'Urban vs Rural':
            # Plot both Urban and Rural lines with markers
            fig2 = px.line(df_employment_pop_ratio, x='Years', y=['Urban', 'Rural'], labels={'value': 'Y-axis'}, line_dash_sequence=['solid', 'solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['purple', 'orange'])
        elif selected_option == 'Total':
            # Plot the Total line with markers
            fig2 = px.line(df_employment_pop_ratio, x='Years', y='Total', labels={'value': 'Y-axis'}, line_dash_sequence=['solid'],
                          line_shape='linear', markers=True, color_discrete_sequence=['red'])

        # Customize the chart
        # fig.update_layout(title='Gender and Residence Data Visualization')

        # Add trace for the x-axis
        fig.add_trace(go.Scatter(x=df['Years'], y=df_employment_pop_ratio['Years'], mode='lines',
                                 name='Years', line=dict(color='black', dash='dash')))
        fig.update_layout(title='Unemployment Rate (2016 - 2023)',
                          xaxis_title='Years', yaxis_title='Unemployment Rate (%)')
        fig.update_yaxes(range=[0, 60])
        fig.update_xaxes(tickangle=-60)
        st.plotly_chart(fig2)

    elif tab_selector == 'Data':
        # Display data on the second tab
        st.subheader('Sample Data:')
        st.dataframe(df)
        st.dataframe(df_employment_pop_ratio)

    print(df_employment_pop_ratio)
    employment_rate(df_employment_pop_ratio)


# Example usag
data = {
    'Years': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Male': [12, 15, 10, 25, 30, 20, 18, 22],
    'Female': [8, 10, 12, 18, 28, 15, 20, 25],
    'Urban': [5, 10, 8, 15, 20, 18, 12, 17],
    'Rural': [7, 12, 10, 18, 25, 15, 10, 15],
    'Total': [20, 25, 18, 43, 55, 35, 30, 42],
}

# # Create a DataFrame from the sample data
# df = pd.DataFrame(data)

# # Call the function
# time_series_graph(df)
