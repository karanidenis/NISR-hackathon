# streamlit_app.py
from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config to wide mode for a better layout.
st.set_page_config(layout="wide")

# Title of the dashboard
st.title("Rwanda Labour Force Survey Dashboard 2023:Q3")

# Introduction or Summary
st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.""")

# General Labor Force Stats
st.header("General Labour Force Statistics")

# Sidebar widget for area of residence selection
area = st.sidebar.selectbox('Select Area of Residence', [
                            'Total', 'Male', 'Female', 'Urban', 'Rural', 'Participated', 'Not participated'])

# Assuming df_b1 is your DataFrame containing the data from Table B.1
# You would load your data here
# df_b1 = pd.read_csv('path_to_your_csv.csv')

# For demonstration purposes, we're creating a sample dataframe.
df_b1 = pd.DataFrame({
    'Indicators': ['Working age population (16+ years)', 'Labour force', 'Employed', 'Unemployed', 'Out of labour force'],
    'Total': [8100430, 4847069, 3972193, 874876, 3253361],
    'Male': [3798558, 2640227, 2248640, 391587, 1158332],
    'Female': [4301872, 2206843, 1723553, 483289, 2095029],
    'Urban': [2441445, 1671352, 1405959, 265393, 770093],
    'Rural': [5658985, 3175717, 2566234, 609483, 2483267],
    'Participated': [2521332, 1299616, 972074, 327541, 1221716],
    'Not participated': [5579098, 3547454, 3000119, 547335, 2031645]
})

# Filter the DataFrame based on the selected area
filtered_df = df_b1[['Indicators', area]]

# Create the bar chart with the filtered data
fig_b1 = px.bar(filtered_df, x='Indicators', y=area,
                title=f'Labour Force Indicators in Rwanda - {area}')
st.plotly_chart(fig_b1)

# Educational Attainment and Employment Stats
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

# Gender disparity in employment
st.header("Gender disparities in labour market outcomes")

# Assuming df_b8 is your DataFrame containing the data from Table B.8
# You would load your data here
# df_b8 = pd.read_csv('path_to_your_csv.csv')


# Data for the employed population by sex and occupation group
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

# Labour Force Statistics by Age Group
st.header("Labour Force Statistics by Age Group")

# Assuming df_b7 is your DataFrame containing the data from Table B.7
# You would load your data here
# df_b7 = pd.read_csv('path_to_your_csv.csv')

# For demonstration purposes, we're creating a sample dataframe.
employed_population_data = {
    'Age_Group': [
        'Total', '15-19 yrs', '20-24 yrs', '25-29 yrs', '30-34 yrs',
        '35-39 yrs', '40-44 yrs', '45-49 yrs', '50-54 yrs', '55-59 yrs', '60-64 yrs'
    ],
    'Total': [3972193, 322790, 586840, 603320, 567053, 540358, 489003, 295037, 221177, 135729, 130148],
    'Male': [2248640, 182765, 350693, 333086, 322444, 302996, 287918, 154501, 117691, 69726, 75328],
    'Female': [1723553, 140025, 236147, 270234, 244610, 237362, 201086, 140536, 103486, 66004, 54820],
    'Urban': [1405959, 89475, 206420, 223444, 236013, 216230, 171792, 103190, 70905, 40266, 30984],
    'Rural': [2566234, 233315, 380420, 379876, 331041, 324128, 317212, 191848, 150273, 95463, 99164],
}

df_employed_b7 = pd.DataFrame(employed_population_data)

# Sidebar widget for age group selection
selected_sex = st.sidebar.selectbox(
    'Select Sex for employed population', ['Total', 'Male', 'Female'])

# If 'Total' is selected, we show data for both Male and Female.
if selected_sex == 'Total':
    filtered_df = df_employed_b7.copy()
else:
    filtered_df = df_employed_b7[['Age_Group', selected_sex]]

# Create the bar chart using Plotly
fig = go.Figure()

# Add trace for the selected sex
fig.add_trace(go.Bar(
    x=filtered_df['Age_Group'],
    y=filtered_df[selected_sex],
    name=selected_sex
))

# Customize layout with a title and axis labels
fig.update_layout(
    title=f"Employment Statistics by Age Group - {selected_sex}",
    xaxis_title="Age Group",
    yaxis_title="Number of Employed Persons",
    barmode='group',
    legend_title="Sex"
)

# Render the plot in Streamlit
st.plotly_chart(fig)

# Summary
st.markdown(f"""
The bar chart displays the distribution of employed persons across different age groups for the selected sex category.
This interactive feature allows us to observe trends and patterns in employment, such as which age groups have higher or lower
employment rates, and how these patterns differ between males and females.
""")

# Assuming df_b17 is your DataFrame containing the data from Table B.17
# You would load your data here
# df_b17 = pd.read_csv('path_to_your_csv.csv')

# For demonstration purposes, we're creating a sample dataframe.
unemployed_population_data = {
    'Age_Group': [
        'Total', '16-24 yrs', '25-34 yrs', '35-54 yrs', '55-64 yrs', '65+ yrs'
    ],
    'Total': [874876, 280990, 268769, 283066, 36253, 5799],
    'Male': [391587, 147422, 87766, 134292, 18178, 3929],
    'Female': [483289, 133569, 181002, 148775, 18074, 1870],
    'Urban': [265393, 88112, 87171, 81989, 5588, 2534],
    'Rural': [609483, 192878, 181598, 201077, 30665, 3265],
}


df_employed_b17 = pd.DataFrame(unemployed_population_data)

# Sidebar widget for age group selection
sex = st.sidebar.selectbox(
    'Select Sex for Unemployed population', ['Total', 'Male', 'Female'], key='sex_select')

# If 'Total' is selected, we show data for both Male and Female.
if sex == 'Total':
    filtered_df = df_employed_b17.copy()
else:
    filtered_df = df_employed_b17[['Age_Group', sex]]

# Create the bar chart using Plotly
fig = go.Figure()

# Add trace for the selected sex
fig.add_trace(go.Bar(
    x=filtered_df['Age_Group'],
    y=filtered_df[sex],
    name=sex
))

# Customize layout with a title and axis labels
fig.update_layout(
    title=f"Unemployment Statistics by Age Group - {sex}",
    xaxis_title="Age Group",
    yaxis_title="Number of Unemployed Persons",
    barmode='group',
    legend_title="Sex"
)

# Render the plot in Streamlit
st.plotly_chart(fig)

# Summary
st.markdown(f"""
The bar chart displays the distribution of unemployed persons across different age groups for the selected sex category.
This interactive feature allows us to observe trends and patterns in unemployment, such as which age groups have higher or lower
uemployment rates, and how these patterns differ between males and females.
""")
