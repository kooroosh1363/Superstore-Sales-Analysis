import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/superstore.csv', encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100
    df['Shipping Delay'] = (pd.to_datetime(df['Ship Date']) - df['Order Date']).dt.days
    return df

df = load_data()

# Sidebar filters
st.sidebar.title("🔎 Filter Data")
region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())
date_range = st.sidebar.date_input("Order Date Range", value=[df['Order Date'].min(), df['Order Date'].max()])

# Apply filters
df_filtered = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Order Date'] >= pd.to_datetime(date_range[0])) &
    (df['Order Date'] <= pd.to_datetime(date_range[1]))
]

# KPIs
total_sales = df_filtered['Sales'].sum()
total_profit = df_filtered['Profit'].sum()
avg_order_value = df_filtered.groupby('Order ID')['Sales'].sum().mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("🧾 Avg Order Value", f"${avg_order_value:,.0f}")

st.markdown("---")

# 📊 Visual 1: Monthly Sales Trend
monthly = df_filtered.copy()
monthly['Month'] = monthly['Order Date'].dt.to_period('M').dt.to_timestamp()
sales_trend = monthly.groupby('Month')['Sales'].sum().reset_index()

fig1 = px.line(sales_trend, x='Month', y='Sales', title='📊 Monthly Sales Trend')
st.plotly_chart(fig1, use_container_width=True)

# 📊 Visual 2: Profit by Region
region_perf = df_filtered.groupby('Region')['Profit'].sum().reset_index()
fig2 = px.bar(region_perf, x='Region', y='Profit', title='🌍 Profit by Region', color='Profit')
st.plotly_chart(fig2, use_container_width=True)

# 📊 Visual 3: Category Sales
cat_perf = df_filtered.groupby('Category')['Sales'].sum().reset_index()
fig3 = px.pie(cat_perf, names='Category', values='Sales', title='🛒 Sales by Category')
st.plotly_chart(fig3, use_container_width=True)

# 📊 Visual 4: Discount vs Profit Scatter
fig4 = px.scatter(df_filtered, x='Discount', y='Profit', opacity=0.6, trendline='ols',
                  title='💸 Discount vs Profit')
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Plotly | Project: Superstore Sales Analysis")

# Sidebar - Sub Category
subcat = st.sidebar.multiselect("Select Sub-Category", options=df['Sub-Category'].unique(), default=df['Sub-Category'].unique())
df_filtered = df_filtered[df_filtered['Sub-Category'].isin(subcat)]

st.markdown("## 📦 Top 10 Best-Selling Products")
top_products = df_filtered.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
fig5 = px.bar(top_products, x='Sales', y='Product Name', orientation='h', title='Top Products by Sales', color='Sales')
fig5.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig5, use_container_width=True)

st.markdown("## 🧑‍💼 Top 10 Customers by Profit")
top_customers = df_filtered.groupby('Customer Name')['Profit'].sum().sort_values(ascending=False).head(10).reset_index()
fig6 = px.bar(top_customers, x='Profit', y='Customer Name', orientation='h', title='Top Customers by Profit', color='Profit')
fig6.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig6, use_container_width=True)

st.markdown("## 🚚 Shipping Delay Distribution")
fig7 = px.histogram(df_filtered, x='Shipping Delay', nbins=15, title='Shipping Delay Histogram', color_discrete_sequence=['orange'])
st.plotly_chart(fig7, use_container_width=True)

st.markdown("## 🧩 Category vs Sub-Category Sales Heatmap")
heat = df_filtered.pivot_table(index='Sub-Category', columns='Category', values='Sales', aggfunc='sum', fill_value=0)
fig8 = px.imshow(heat, text_auto=True, aspect='auto', color_continuous_scale='Blues', title='Heatmap of Sales')
st.plotly_chart(fig8, use_container_width=True)
