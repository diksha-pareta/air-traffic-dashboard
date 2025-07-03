import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit page config
st.set_page_config(page_title="Air Traffic Dashboard", layout="wide")
st.title("✈️ Air Traffic Data Analysis Dashboard")
st.markdown("This dashboard provides interactive analysis of air traffic data.")

# Load dataset with caching
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
airlines = st.sidebar.multiselect(
    "Select Airline(s):", 
    options=sorted(data['Operating Airline'].dropna().unique()), 
    default=sorted(data['Operating Airline'].dropna().unique())
)
years = st.sidebar.multiselect(
    "Select Year(s):", 
    options=sorted(data['Year'].dropna().unique()), 
    default=sorted(data['Year'].dropna().unique())
)

# Apply filters
filtered = data[(data['Operating Airline'].isin(airlines)) & (data['Year'].isin(years))]

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["📊 EDA", "📈 Time Series", "🗺️ Map"])

# --- 📊 Tab 1: EDA ---
with tab1:
    st.subheader("Distribution of Flights by Airline")

    airline_counts = (
        filtered["Operating Airline"]
        .value_counts()
        .reset_index()
    )
    airline_counts.columns = ["Operating Airline", "Flight Count"]

    fig1 = px.bar(
        airline_counts.sort_values("Flight Count", ascending=True),
        x="Flight Count",
        y="Operating Airline",
        orientation="h",
        color="Flight Count",
        color_continuous_scale="Blues",
        title="✈️ Flight Distribution by Airline"
    )
    fig1.update_layout(height=800, yaxis_title="Airline", xaxis_title="Number of Flights")
    st.plotly_chart(fig1, use_container_width=True)

    # Passenger trends
    st.subheader("Monthly Passenger Trends")
    monthly = filtered.groupby('Date')['Passenger Count'].sum().reset_index()
    fig2 = px.line(monthly, x='Date', y='Passenger Count', title='📈 Monthly Passenger Traffic')
    st.plotly_chart(fig2, use_container_width=True)

# --- 📈 Tab 2: Time Series ---
with tab2:
    st.subheader("Seasonal Passenger Heatmap")
    pivot = filtered.groupby(['Year', 'Month'])['Passenger Count'].sum().reset_index()
    pivot_data = pivot.pivot(index='Year', columns='Month', values='Passenger Count')
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.heatmap(pivot_data, cmap='YlGnBu', annot=True, fmt=".0f", ax=ax3)
    st.pyplot(fig3)

# --- 🗺️ Tab 3: Geo Map ---
with tab3:
    st.subheader("Flight Distribution Map")
    if "Passenger Count" in filtered.columns:
        fig4 = px.scatter_geo(
            filtered,
            color="Operating Airline",
            size="Passenger Count",
            projection="natural earth",
            title="🌍 Airline Passenger Distribution Map"
        )
        st.plotly_chart(fig4, use_container_width=True)
