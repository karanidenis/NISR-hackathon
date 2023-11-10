from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go




def graph2():

    st.header("Impact of Education Level on Employment Statistics")

    # Assuming df_b5 is your DataFrame containing the data from Table B.5
    # You would load your data here
    # df_b5 = pd.read_csv('path_to_your_csv.csv')

    # For demonstration purposes, we're creating a sample dataframe.
    df_b5 = pd.DataFrame({
        'Education_Level': ['None', 'Primary', 'Lower_secondary', 'Upper_secondary', 'University'],
        'Labour_force_participation_rate': [58.3, 59.7, 48.2, 68.3, 86.9],
        'Employment_to_population_ratio': [48.8, 48.5, 38.1, 52.4, 73.5],
        'Unemployment_rate': [16.4, 18.7, 21.1, 23.3, 15.5]
    })

    # Interactive chart for education impact
    fig_b5 = go.Figure()

    # Adding traces for each rate
    for column in df_b5.columns[1:]:
        fig_b5.add_trace(go.Bar(
            x=df_b5['Education_Level'],
            y=df_b5[column],
            name=column,
            marker_line_color='rgb(0,0,0)',
            marker_line_width=1.5,
            opacity=0.7
        ))

    # Customize layout with a title and axis labels
    fig_b5.update_layout(
        title="Labour Force Statistics by Education Level",
        xaxis_title="Education Level",
        yaxis_title="Rate (%)",
        legend_title="Indicators",
        barmode='group',
        margin=dict(l=60, r=60, t=50, b=50)  # Adjust margins to fit the title
    )

    st.plotly_chart(fig_b5)

    # Data for the unemployed population by level of education
    unemployed_data = {
        'Education_Level': ['Total', 'None', 'Primary', 'Lower_secondary', 'Upper_secondary', 'University'],
        'Total': [874876, 357109, 293168, 74611, 105424, 44565],
        'Male': [391587, 174271, 122029, 32734, 43710, 18842],
        'Female': [483289, 182838, 171138, 41877, 61713, 25723],
        'Urban': [265393, 77041, 56554, 30190, 61343, 40265],
        'Rural': [609483, 280068, 236613, 44421, 44081, 4300],
        'Participated': [327541, 141634, 132302, 28309, 23756, 1540],
        'Not participated': [547335, 215475, 160865, 46302, 81668, 43025]
    }

    # Data for the employed population by level of education
    employed_data = {
        'Education_Level': ['Total', 'None', 'Primary', 'Lower_secondary', 'Upper_secondary', 'University'],
        'Total': [3972193, 1825744, 1277562, 278889, 346961, 243037],
        'Male': [2248640, 994006, 769758, 157728, 186336, 140811],
        'Female': [1723553, 831738, 507804, 121161, 160625, 102226],
        'Urban': [1405959, 448242, 421828, 128546, 194297, 213046],
        'Rural': [2566234, 1377503, 855734, 150342, 152664, 29991],
        'Participated': [972074, 559028, 314831, 47071, 37023, 14121],
        'Not participated': [3000119, 1266716, 962731, 231818, 309938, 228916]
    }

    # Convert data to dataframes
    unemployed_df = pd.DataFrame(unemployed_data)
    employed_df = pd.DataFrame(employed_data)

    # Create subplots: one for unemployed data, one for employed data
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "Unemployed by Education Level", "Employed by Education Level"))

    # Add traces for unemployed data
    fig.add_trace(
        go.Bar(x=unemployed_df['Education_Level'],
               y=unemployed_df['Total'], name='Unemployed Total'),
        row=1, col=1
    )
    # ... Add other unemployed traces if needed ...

    # Add traces for employed data
    # Add traces for employed data
    fig.add_trace(
        go.Bar(x=employed_df['Education_Level'],
               y=employed_df['Total'], name='Employed Total'),
        row=1, col=2
    )
    # Optionally add more traces for different categories (Male, Female, etc.)

    # Update layout for clear visibility and unified look
    fig.update_layout(
        title_text="Employment Status by Education Level",
        barmode='group',
        height=600,
        # Since we are in Streamlit, we don't need to set a fixed width. Streamlit will take care of it.
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig)

    st.markdown("""
    The chart above illustrates the correlation between the level of education and various labour market statistics
    for the population aged 16 and over. Higher levels of education tend to be associated with higher labour force
    participation rates and employment-to-population ratios, alongside lower unemployment rates.
    """)
    
    st.markdown("------------------------------------------------------------")