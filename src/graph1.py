import streamlit as st
import pandas as pd
import plotly.express as px

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
# st.title("Rwanda Labour Force Survey Dashboard 2023:Q3")

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
