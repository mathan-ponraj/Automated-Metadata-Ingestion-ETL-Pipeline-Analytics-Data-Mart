# 📊 TrendTube — YouTube Trending Data ETL Pipeline

## 🎯 Project Overview

**TrendTube** is an automated **Python ETL pipeline** that extracts YouTube trending video data through the **YouTube Data API v3**, transforms nested JSON into structured datasets, and loads the processed data into a **SQL database** for analysis.

It transforms raw API responses into clean, structured, and **query-ready data** for business analytics.

## 📸 Visual Preview

![TrendTube Preview](images/pipeline-preview.png)

## 💡 The Problem & Core Value

- 🔗 Raw YouTube API responses contain **complex nested JSON**.
- 🧹 Manual processing makes the data difficult to clean and analyze.
- ⚙️ TrendTube automates **extraction, transformation, cleaning, and loading**.
- 🗄️ Converts unstructured API data into a **relational SQL format** for efficient querying.

## ✨ Key Features & Data Flow

- 🔄 **Automated API Extraction** — Fetches video metadata, engagement metrics, channels, and categories.
- 🧹 **Data Transformation** — Flattens nested JSON and standardizes the dataset.
- 🗄️ **SQL Data Loading** — Stores processed data using SQLAlchemy.

**Data Flow:**

`YouTube API → JSON → Python/Pandas → Data Cleaning → SQLAlchemy → SQL Database`

## 🛠️ Tech Stack & Architecture Decisions

| Layer | Technology | Purpose |
|---|---|---|
| Language | **Python** | ETL development |
| Data Processing | **Pandas, NumPy** | Cleaning & transformation |
| JSON Processing | **JSON** | API response parsing |
| Database | **SQL** | Structured data storage |
| ORM | **SQLAlchemy** | Database interaction |
| API | **YouTube Data API v3** | Data extraction |

## 📈 Challenges & Technical Takeaways

**The Obstacle**
- YouTube API responses contain **deeply nested JSON structures**.
- Raw data includes missing values, duplicates, and inconsistent timestamps.

**The Resolution**
- Built Python logic to **flatten nested JSON** into tabular data.
- Added data cleaning and standardization steps.
- Used **SQLAlchemy** to load processed data into a structured SQL environment.

## ⚙️ Quick Start

```bash
git clone <your-repository-url>
cd TrendTube
pip install -r requirements.txt
python main.py
```
