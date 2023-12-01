from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import streamlit as st


def graph2(df):

    st.header("Impact of Education Level on Employment")

    # Extract the relevant data for the first chart
    # Adjust indices as per your DataFrame
    df_b5 = df.iloc[1:7, [0, 6, 7, 8]]

    # colors = ['#006af9', '#000080', '#36454F']
    light_blue = '#006af9'
    dark_blue = '#008080'
    teal = '#FF7F50'
    # Sidebar widget for gender selection
    selected_gender = st.sidebar.radio(
        "Filter by Sex", ["Total", "Male", "Female"])

    # Define index ranges for Total, Male, and Female data in the DataFrame
    index_ranges = {
        "Total": slice(1, 7),
        "Male": slice(8, 14),
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
        x=df_gender['Education_Level'], marker_color='#006af9',
        y=df_gender['Labour_force_participation_rate'],
        name='Labour Force Participation Rate'
    ))

    fig_b5.add_trace(go.Bar(
        x=df_gender['Education_Level'], marker_color=teal,
        y=df_gender['Employment_to_population_ratio'],
        name='Employment to Population Ratio'
    ))

    fig_b5.add_trace(go.Bar(
        x=df_gender['Education_Level'], marker_color=dark_blue,
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

    st.markdown("""
    The chart above illustrates the correlation between the level of education and various labour market statistics
    for the population aged 16 and over. Higher levels of education tend to be associated with higher labour force
    participation rates and employment-to-population ratios, alongside lower unemployment rates.
    """)

    # Process data for subplots
    # Skip the first row which is a header
    education_levels = df['Unnamed: 0'][1:7]
    unemployed_df = df['Unemployed'][1:7]
    employed_df = df['Employed'][1:7]
    # Create subplots: one for unemployed data, one for employed data
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "Employed by Education Level", "Unmployed by Education Level"))

    # Add traces for unemployed data
    # Add traces for employed data
    fig.add_trace(
        go.Bar(x=education_levels, marker_color='#006af9',
               y=employed_df, name='Employed Total'),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=education_levels, marker_color=teal,
               y=unemployed_df, name='Unemployed Total'),
        row=1, col=2
    )

    # Update layout for clear visibility and unified look
    fig.update_layout(
        title_text="Employment Status by Education Level",
        barmode='group',
        height=600,
    )

    # Render the plot in Streamlit
    view_mode = st.sidebar.selectbox(
        "View Mode for second plot", ["Chart", "Raw Data"])
    if view_mode == "Chart":
        st.plotly_chart(fig)
    elif view_mode == "Raw Data":
        st.write(df)
    else:
        st.plotly_chart(fig)

    st.markdown("""
    The visual show employment trends by education level, 
    revealing higher unemployment among the uneducated and higher employment amonf the educated for the population aged 16 and over. 
    University-educated individuals have lower unemployment rates, indicating that higher education correlates with improved employment prospects.
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
