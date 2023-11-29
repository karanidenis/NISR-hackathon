import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd

 
# Load your data here for each graph
df_b1 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.1', skiprows=2)
df_b1.dropna(axis=1, how='all', inplace=True)
df_b1.dropna(axis=0, how='all', inplace=True)

df_b5 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.5', skiprows=1)
df_b5.dropna(axis=1, how='all', inplace=True)
df_b5.dropna(axis=0, how='all', inplace=True)

df_b7 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.7', skiprows=2)
df_b7.dropna(axis=1, how='all', inplace=True)
df_b7.dropna(axis=0, how='all', inplace=True)

df_b8 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.8', skiprows=2)
df_b8.dropna(axis=1, how='all', inplace=True)
df_b8.dropna(axis=0, how='all', inplace=True)

df_b17 = pd.read_excel('./data/labour_force_data.xlsx',
                       sheet_name='Table B.17', skiprows=2)
df_b17.dropna(axis=1, how='all', inplace=True)
df_b17.dropna(axis=0, how='all', inplace=True)

# Title container
# Graph container
with st.container():
    st.title("Rwanda Labour Force Survey Dashboard 2023:Q3")

    st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.
    """)

    # Custom CSS for styling the metric boxes
    st.markdown("""
    <style>
    .metric-box {
        # background-color: #009688;
        # background-color: #1f2c56;
        # background-color: blue;
        background-color: #006af9;
        border-radius: 10px;
        padding: 15px;
        color: white;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 0.2em;
    }
    .metric-label {
        font-size: 1em;
    }
    # .data-container {
    #     margin-top: 20px;
    # }
    </style>
    """, unsafe_allow_html=True)

    # Function to display metric boxes
    st.header("General Labour Force Statistics")


    def create_metric_box(label, value):

        st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)


    # Layout for metric boxes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_metric_box("Working Population (Age: 16+ years)", "8,100,430")
    with col2:
        create_metric_box("Popualtion in Labor force", "4,847,069")
    with col3:
        create_metric_box("Employed Population", "3,972,193")
    with col4:
        create_metric_box("Unemployed Population", "874,876")

    # Read the Excel file
    df = pd.read_excel('./data/labour_force_data.xlsx',
                    sheet_name='Table B.1', skiprows=2)
    df = df.dropna(axis=1, how='all')  # Drop empty columns
    df = df.dropna(axis=0, how='all')  # Drop empty rows


    # Function to create and display the pie chart


    def graph_1(df):

        area = st.sidebar.radio(
            'Select Sex', ['Total', 'Male', 'Female'], key="Graph1_sex")
        filtered_df = df[['Unnamed: 0', area]].iloc[2:5]
        filtered_df.columns = ['Indicators', 'Value']  # Rename columns for clarity

        # Define your color scheme here
        # colors = ['blue', 'red', '#1f2c56']
        colors = ['#006af9', '#dc00fe', '#5319fb']

        fig_pie = px.pie(filtered_df, values='Value', names='Indicators',
                        title=f'Labour Force Distribution - {area}',
                        color_discrete_sequence=colors)
        st.plotly_chart(fig_pie, use_container_width=True)

        # Summary
        st.markdown(f"""
        The chart illustrates the breakdown of the total population aged 16 and over by employment status: 
        49% are employed, 10.8% are unemployed, and 40.2% are not part of the labor force.
        """)

    # Display pie chart
    # display_pie_chart(df)


    # Add a radio button in the sidebar to toggle between the plot and the raw data
    view_mode = st.sidebar.selectbox(
        "Select View Mode", ["Plot", "Raw Data"], key="1")

    # Based on the selection, either display the plot or the raw data
    if view_mode == "Plot":
        graph_1(df)
    elif view_mode == "Raw Data":
        # Wrap the data table in a container with margin
        st.markdown('<div class="data-container">', unsafe_allow_html=True)
        df = df.dropna(axis=1, how='all')  # Drop empty columns
        st.dataframe(df)  # This will display the dataframe as a table
        st.markdown('</div>', unsafe_allow_html=True)
        # st.dataframe(df)

    from plotly.subplots import make_subplots


def graph2(df):

    st.header("Impact of Education Level on Employment Statistics")

    # Extract the relevant data for the first chart
    # Adjust indices as per your DataFrame
    df_b5 = df.iloc[1:7, [0, 6, 7, 8]]

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
        x=df_gender['Education_Level'], marker_color='#dc00fe',
        y=df_gender['Employment_to_population_ratio'],
        name='Employment to Population Ratio'
    ))

    fig_b5.add_trace(go.Bar(
        x=df_gender['Education_Level'], marker_color='#5319fb',
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
        "Unemployed by Education Level", "Employed by Education Level"))

    # Add traces for unemployed data
    # Add traces for employed data
    fig.add_trace(
        go.Bar(x=education_levels, marker_color='#006af9',
               y=employed_df, name='Employed Total'),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=education_levels, marker_color='#dc00fe',
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


def graph3(df):
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

    df_b7 = df_b7[df_b7['Occupation_Group'] !=
                  'Total unemployed population(16+ years)']
    df_b7 = df_b7[df_b7['Occupation_Group'] !=
                  'Source:  Labour Force Survey,2023:Q3(NISR)']
    # print(df_b7)
    df_b17 = df_b17[df_b17['Occupation_Group'] !=
                    'Total unemployed population(16+ years)']
    df_b17 = df_b17[df_b17['Occupation_Group'] !=
                    'Source:  Labour Force Survey,2023:Q3(NISR)']
    # print(df_b17)

    # Sidebar for gender selection
    gender_options = ['Total', 'Male', 'Female']
    selected_gender = st.sidebar.radio('Select Gender', gender_options)

    # Plot for Table B.7
    fig_b7 = go.Figure()

    if selected_gender == 'Total':
        # Include both 'Male' and 'Female' data
        fig_b7.add_trace(go.Bar(
            x=df_b7['Occupation_Group'], y=df_b7['Male'], name='Male', marker_color='#006af9'))
        fig_b7.add_trace(go.Bar(
            x=df_b7['Occupation_Group'], y=df_b7['Female'], name='Female', marker_color='#dc00fe'))
    else:
        # Only include the selected gender data
        fig_b7.add_trace(go.Bar(
            x=df_b7['Occupation_Group'], y=df_b7[selected_gender], name=selected_gender))

    fig_b7.update_layout(title=f"Employment Statistics - {selected_gender}",
                         xaxis_title='Occupation Group', yaxis_title='Number of Persons',
                         #  height=600, width=800,
                         margin=dict(l=60, r=60, t=50, b=50))
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
            x=df_b17['Occupation_Group'], y=df_b17['Male'], name='Male', marker_color='#006af9'))
        fig_b17.add_trace(go.Bar(
            x=df_b17['Occupation_Group'], y=df_b17['Female'], name='Female', marker_color='#dc00fe'))
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

    # st.dataframe(df_b17)
    b7 = pd.DataFrame(df_b7)
    b17 = pd.DataFrame(df_b17)
    # Using st.expander to make the DataFrame collapsible
    expander = st.expander("Click here to expand/collapse the DataFrame")
    with expander:
        st.dataframe(b7)
        st.dataframe(b17)


# Run the graph4 function when the script is executed
if __name__ == '__main__':
    # Load data
    df = pd.read_excel('data/labour_force_data.xlsx',
                       sheet_name='Table B.7', skiprows=2)
    df = pd.read_excel('data/labour_force_data.xlsx',
                       sheet_name='Table B.17', skiprows=2)
    graph3(df)


def graph4(df):
    st.header("Occupation Groups in labour market outcomes")

    # drop last row
    df.drop(df.index[-1], inplace=True)

    # # Define the columns for the bar chart
    df.columns = ['Occupation_Group', 'Total', 'Male', 'Female',
                  'Urban', 'Rural', 'Participated', 'Not participated']

    # Exclude the 'Total' row for the bar chart display
    df = df[df['Occupation_Group'] != 'Total']

    # Sidebar widget for gender selection
    selected_gender = st.sidebar.selectbox(
        "Select Gender", ["Both", "Male", "Female"])

    # Plotting the bar chart using Plotly
    fig_b8 = go.Figure()

    if selected_gender == "Both":
        fig_b8.add_trace(go.Bar(
            x=df['Occupation_Group'],
            y=df['Male'],  # reduce the y axis box sizes to 0.25 from 0.5
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
    # fig_b8.update_yaxes(range=[0, 0.2])
    fig_b8.update_layout(
        title="Gender Disparities in Labour Market by Occupation Group",
        xaxis_title="Occupation Group",
        yaxis_title="Number of Employed Persons",
        barmode='group',
        margin=dict(l=60, r=60, t=50, b=50),
        # reduce y axis box sizes to 0.25 from 0.5 use ylim
        width=800,
        height=600
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

    # Using st.expander to make the DataFrame collapsible
    expander = st.expander("Click here to expand/collapse the DataFrame")
    with expander:
        st.dataframe(df)


# Run the graph3 function when the script is executed
if __name__ == '__main__':
    #  Read the data from the Excel file
    df = pd.read_excel('./data/labour_force_data.xlsx',
                       sheet_name='Table B.8', skiprows=2)
    # Drop rows and columns with all NaN values
    df = df.dropna(axis=1, how='all').dropna(axis=0, how='all')
    graph4(df)
