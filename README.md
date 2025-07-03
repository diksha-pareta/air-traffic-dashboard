#  Air Traffic Data Analysis Dashboard

This project is a comprehensive end-to-end data science capstone titled **"Air Traffic Data Analysis"**, which explores global aviation patterns using real air traffic data. It uncovers trends in airline performance, passenger traffic, and flight operations to support data-driven decision-making in the aviation industry.

##  Project Objective
- Analyze flight trends across airlines and airports
- Identify seasonal patterns in passenger volume
- Perform time series forecasting of air traffic
- Segment airlines/routes using clustering
- Build an interactive dashboard for exploration

##  Dataset
- Activity Period (Year & Month)
- Operating Airline
- Geo Summary & Region
- Passenger Count & Adjusted Count
- Activity Type (Arrival/Departure)
>  Source: Bureau of Transportation Statistics (BTS)  
> [https://www.transtats.bts.gov/](https://www.transtats.bts.gov/)

##  Tools & Technologies
- Python (Pandas, NumPy)
- Seaborn & Matplotlib (EDA Visuals)
- Plotly (Interactive Graphs)
- Prophet (Time Series Forecasting)
- Scikit-learn (Clustering)
- Streamlit (Dashboard Deployment)

##  Dashboard Features
- **EDA Visuals**: Airline distribution, seasonality, traffic heatmaps  
- **Forecasting**: Predict passenger trends using Prophet  
- **Clustering**: Group similar traffic patterns using KMeans  
- **Interactivity**: Filters by year, airline, region  
- **Web App**: Fully deployed via Streamlit Cloud

##  How to Run This Project

###  Run Locally
```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/air-traffic-dashboard.git
cd air-traffic-dashboard

# Step 2: Install required packages
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py
```

###  Deploy on Streamlit Cloud
1. Push `app.py`, `requirements.txt`, `README.md`, and dataset to GitHub  
2. Go to [https://share.streamlit.io](https://share.streamlit.io)  
3. Select your GitHub repo  
4. Click **Deploy**

##  Project Structure
```
├── app.py                    # Streamlit dashboard code
├── air_traffic_data.csv.zip  # Dataset
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
```

##  Author
**Diksha Kumari Pareta**  
M.Tech Candidate, IIIT Delhi  
 diksha24118@iiitd.ac.in  

##  Tags
`#DataScience` `#CapstoneProject` `#Streamlit` `#AviationAnalytics` `#Forecasting` `#Clustering` `#Dashboard` `#AirTraffic`
