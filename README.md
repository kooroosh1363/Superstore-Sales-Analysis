# 🛍️ Superstore Sales Analysis

Welcome to the **Superstore Sales Analysis** project!  
This is a complete, real-world exploratory data analysis (EDA) of a fictional retail dataset often used in business analytics. The project walks through data cleaning, feature engineering, and visual storytelling using Python, Pandas, and Plotly.

---

## 🎯 Project Objectives

- Understand key patterns in sales and profitability
- Identify regional and temporal trends
- Analyze customer behavior and segment performance
- Provide actionable insights for inventory, pricing, and logistics decisions

---

## 🗂 Dataset

- Source: [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Format: CSV
- Columns include: Order ID, Customer Name, Segment, State, Region, Product Category, Sub-Category, Sales, Profit, Discount, Quantity, Order Date, Ship Date, and more.

---

## ⚙️ Tools & Technologies

- **Python**
- **Pandas** and **NumPy** for data manipulation
- **Plotly Express** and **Seaborn** for interactive and statistical visualizations
- **Jupyter Notebook** for step-by-step narration

---

## 📊 Analysis Highlights

This project includes the following major analyses:

### 1. 📈 Monthly Sales Trend  
Trended total sales over time to detect seasonality and growth patterns.

### 2. 🗺️ Profit & Sales by Region  
Compared performance across regions to uncover top/bottom markets.

### 3. 📦 Category and Sub-Category Performance  
Analyzed sales and profitability by product category and sub-category.

### 4. 💸 Discount vs Profit Relationship  
Visualized the impact of discounting on profitability using scatter and regression.

### 5. 🧩 State-Level Sales Mapping  
Created a choropleth map to highlight state-wise sales volume.

### 6. ⏱️ Shipping Delay Analysis  
Measured logistics efficiency via shipping delays (Ship Date - Order Date).

### 7. 🚚 Performance by Ship Mode  
Compared average shipping delay and profit across delivery modes.

### 8. 📐 Correlation Matrix  
Explored relationships between numeric features like Sales, Profit, Discount, Quantity.

### 9. 💰 Profit Margin Distribution  
Calculated profit margin (%) per order and visualized its distribution.

### 10. ❌ Loss-Making Sub-Categories  
Identified product lines with consistent negative profit.

### 11. 📈 Cumulative Sales Trend  
Visualized cumulative sales over time to show long-term business growth.

### 12. 📋 AOV by Customer Segment  
Measured Average Order Value (AOV) for each customer segment.

### 13. 💎 Top 10 Customers  
Highlighted the customers generating the highest sales and profits.

---

## 📂 Project Structure

```
Superstore-Sales-Analysis/
├── data/
│   └── superstore.csv
├── notebooks/
│   └── sales_analysis.ipynb
├── sales_analysis.py  ← python version of the notebook
└── README.md
```

---

## 🧠 Key Learnings

- Discounting doesn’t always improve profitability
- Office Supplies and Technology drive higher profit margins
- West and East regions dominate sales, but losses are more common in Furniture
- Same-Day shipping is fast but rarely used; Standard Class dominates

---

## 🙌 Credits

This project is inspired by real-world business analytics cases and Kaggle datasets.  
Created by [Your Name] as part of a professional data science portfolio.

---

## 🚀 Try it Live

👉 [Launch Streamlit App](https://superstore-sales-analysis-3wnvmwugtcnluasejtx45n.streamlit.app)

Or run it locally using:

```bash
git clone https://github.com/kooroosh1363/Superstore-Sales-Analysis.git
cd Superstore-Sales-Analysis
pip install -r requirements.txt
streamlit run app.py
```







## 🚀 Next Steps (Optional)

- Deploy Streamlit dashboard from the final notebook
- Extend analysis with Customer Lifetime Value (CLTV)
- Apply ML models to forecast sales or predict churn



## 🙏 Credits

Created with ❤️ by Peyman using Streamlit.