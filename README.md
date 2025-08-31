#  Live YouTube Data Analysis Pipeline

This project demonstrates an **end-to-end YouTube data pipeline** using **Databricks** and the **Medallion Architecture** (Bronze → Silver → Gold).

---

##  Pipeline Workflow

1. **Bronze Layer (Data Ingestion)**: Fetch live YouTube data via the YouTube API and save as raw JSON.  
2. **Silver Layer (Data Transformation)**: Clean and structure the raw data into tabular format (CSV).  
3. **Gold Layer (Aggregation)**: Aggregate the structured data for reporting (e.g., video counts per channel).  
4. **Reporting**: Display or export curated insights for dashboards.

---

##  Tech Stack

- Databricks (Spark + Delta Lake) or local Python execution  
- YouTube Data API  
- JSON, Pandas, Requests  
- Medallion Architecture (Bronze/Silver/Gold)  
- Visualization: Power BI, Tableau, or Databricks SQL

---

##  Project Structure

