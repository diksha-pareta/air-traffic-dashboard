import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Air Traffic Dashboard", layout="wide")

st.title("✈️ Air Traffic Data Analysis Dashboard")
st.markdown("This dashboard provides interactive analysis of air traffic data.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("air_traffic_data.csv.zip")
    df['Activity Period'] = pd.to_datetime(df['Activity Period'], format='%Y%m')
    df['Year'] = df['Activity Period'].dt.year
    df['Month'] = df['Activity Period'].dt.month
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    return df

data = load_data()

# Sidebar filters
airlines = st.sidebar.multiselect("Select Airline(s):", options=data['Operating Airline'].unique(), default=data['Operating Airline'].unique())
years = st.sidebar.multiselect("Select Year(s):", options=data['Year'].unique(), default=data['Year'].unique())

filtered = data[(data['Operating Airline'].isin(airlines)) & (data['Year'].isin(years))]

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 EDA", "📈 Time Series", "🗺️ Map"])

with tab1:
    st.subheader("Distribution of Flights by Airline")
    airline_counts = filtered['Operating Airline'].value_counts()
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(y=airline_counts.index, x=airline_counts.values, ax=ax1)
    ax1.set_xlabel("Flight Count")
    ax1.set_ylabel("Airline")
    st.pyplot(fig1)

    st.subheader("Monthly Passenger Trends")
    monthly = filtered.groupby(['Date'])['Passenger Count'].sum().reset_index()
    fig2 = px.line(monthly, x='Date', y='Passenger Count', title='Monthly Passenger Traffic')
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Seasonal Heatmap")
    pivot = filtered.groupby(['Year', 'Month'])['Passenger Count'].sum().reset_index()
    pivot_data = pivot.pivot(index='Year', columns='Month', values='Passenger Count')
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.heatmap(pivot_data, cmap='YlGnBu', annot=True, fmt=".0f", ax=ax3)
    st.pyplot(fig3)

with tab3:
    st.subheader("Flight Distribution Map")
    if "Passenger Count" in filtered.columns:
        fig4 = px.scatter_geo(filtered,
            color="Operating Airline",
            size="Passenger Count",
            projection="natural earth",
            title="Airline Passenger Distribution")
        st.plotly_chart(fig4, use_container_width=True)
