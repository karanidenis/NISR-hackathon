from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import streamlit as st


def graph2(df):

    st.header("Impact of Education Level on Employment Statistics")

    # Extract the relevant data for the first chart
    # Adjust indices as per your DataFrame
    df_b5 = df.iloc[1:7, [0, 6, 7, 8]]
    # df_b5.columns = ['Education_Level', 'Labour_force_participation_rate',
    #                  'Employment_to_population_ratio', 'Unemployment_rate']

    # Sidebar widget for gender selection
    selected_gender = st.sidebar.radio(
        "Select Gender", ["Total", "Male", "Female"])

    # Define index ranges for Total, Male, and Female data in the DataFrame
    index_ranges = {
        "Total": slice(1, 7),  # Assuming 'Total' data is from row 2 to row 7
        "Male": slice(8, 14),  # Assuming 'Male' data is from row 9 to row 14
        # Assuming 'Female' data is from row 16 to row 21
        "Female": slice(15, 21)
    }

    # Use the selected gender to determine which rows to select from the DataFrame
    gender_slice = index_ranges[selected_gender]

    # Extract the relevant data for the selected gender
    df_gender = df.iloc[gender_slice, [0, 6, 7, 8]]
    df_gender = df_gender.set_index('Unnamed: 0').reset_index()
    df_gender.columns = ['Education_Level', 'Labour_force_participation_rate',
                         'Employment_to_population_ratio', 'Unemployment_rate']

    # Interactive chart for education impact
    fig_b5 = make_subplots(rows=1, cols=3, subplot_titles=(
        'Labour_force_participation_rate',
        'Employment_to_population_ratio', 'Unemployment_rate'))

    # Interactive chart for education impact
    fig_b5 = go.Figure()

    # Adding traces for each rate
    fig_b5.add_trace(go.Bar(
        x=df_gender['Education_Level'],
        y=df_gender['Labour_force_participation_rate'],
        name='Labour Force Participation Rate'
    ))

    fig_b5.add_trace(go.Bar(
        x=df_gender['Education_Level'],
        y=df_gender['Employment_to_population_ratio'],
        name='Employment to Population Ratio'
    ))

    fig_b5.add_trace(go.Bar(
        x=df_gender['Education_Level'],
        y=df_gender['Unemployment_rate'],
        name='Unemployment Rate'
    ))

    # Customize layout with a title and axis labels
    fig_b5.update_layout(
        title=f"Labour Force Statistics by Education Level for {selected_gender} Population",
        xaxis_title="Education Level",
        yaxis_title="Rate (%)",
        barmode='group',
        margin=dict(l=60, r=60, t=50, b=50)
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig_b5)
 

    # # Interactive chart for education impact
    # fig_b5 = go.Figure()

    # # Adding traces for each rate
    # for column in df_b5.columns[1:]:
    #     fig_b5.add_trace(go.Bar(
    #         x=df_b5['Education_Level'],
    #         y=df_b5[column],
    #         name=column,
    #         marker_line_color='rgb(0,0,0)',
    #         marker_line_width=1.5,
    #         opacity=0.7
    #     ))

    # # Customize layout with a title and axis labels
    # fig_b5.update_layout(
    #     title="Labour Force Statistics by Education Level",
    #     xaxis_title="Education Level",
    #     yaxis_title="Rate (%)",
    #     legend_title="Indicators",
    #     barmode='group',
    #     margin=dict(l=60, r=60, t=50, b=50)  # Adjust margins to fit the title
    # )

    # st.plotly_chart(fig_b5)

    # Process data for subplots
    # Skip the first row which is a header
    education_levels = df['Unnamed: 0'][1:7]
    unemployed_df = df['Unemployed'][1:7]
    employed_df = df['Employed'][1:7]
    # Create subplots: one for unemployed data, one for employed data
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "Unemployed by Education Level", "Employed by Education Level"))

    # Add traces for unemployed data
    fig.add_trace(
        go.Bar(x=education_levels,
               y=unemployed_df, name='Unemployed Total'),
        row=1, col=1
    )

    # Add traces for employed data
    fig.add_trace(
        go.Bar(x=education_levels,
               y=employed_df, name='Employed Total'),
        row=1, col=2
    )

    # Update layout for clear visibility and unified look
    fig.update_layout(
        title_text="Employment Status by Education Level",
        barmode='group',
        height=600,
    )

    # Render the plot in Streamlit
    st.plotly_chart(fig)

    st.markdown("""
    The chart above illustrates the correlation between the level of education and various labour market statistics
    for the population aged 16 and over. Higher levels of education tend to be associated with higher labour force
    participation rates and employment-to-population ratios, alongside lower unemployment rates.
    """)

    st.markdown("------------------------------------------------------------")


# Run the app
if __name__ == '__main__':
    # Load your data here or pass the DataFrame to the function
    df = pd.read_excel('./data/labour_force_data.xlsx',
                       sheet_name='Table B.5', skiprows=1)
    df = df.dropna(axis=1, how='all')  # Drop empty columns
    df = df.dropna(axis=0, how='all')  # Drop empty rows
    graph2(df)
