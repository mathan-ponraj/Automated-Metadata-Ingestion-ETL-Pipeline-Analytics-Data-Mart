# TrendTube — YouTube Trending Data ETL Pipeline

## Description

TrendTube is an automated ETL pipeline that collects trending YouTube video data using the YouTube Data API v3. The project includes data extraction, data cleaning and transformation, loading the processed data into a SQLite database, and SQL-based analysis of video performance and engagement.

The analysis focuses on identifying the most-viewed videos, most-liked videos, frequently appearing channels, and videos with higher like-to-view engagement.

## Skills

- API data extraction
- Data cleaning and preprocessing
- ETL pipeline development
- Data transformation
- SQL data analysis
- Database management
- Engagement metric analysis

## Technology

Python, Pandas, YouTube Data API v3, SQLite, SQL

## Workflow

The project includes the following steps:

1. **Data Extraction** — Fetch trending video data from the YouTube Data API and save the raw data as a CSV file.
2. **Data Cleaning** — Handle missing values, convert views and likes into numeric values, and remove duplicate records.
3. **Data Transformation** — Prepare the cleaned data into a structured format for database storage and analysis.
4. **Data Loading** — Load the transformed dataset into a SQLite database.
5. **SQL Analysis** — Query the database to analyze video views, likes, channel frequency, and engagement.
6. **Output Generation** — Save the analysis results as separate CSV files for further analysis.

## Obstacles & Resolutions

- **Raw API data required cleaning before analysis:** Handled missing values, converted numeric fields, and removed duplicate records using Pandas.
- **Different data types made analysis difficult:** Standardized views and likes into numeric values before performing calculations.
- **Raw CSV data was not convenient for repeated analysis:** Loaded the transformed dataset into SQLite so it could be queried using SQL.
- **Views and likes alone did not provide an engagement comparison:** Created a like-to-view engagement rate to compare audience interaction across videos.
- **Analysis results were difficult to reuse from SQL queries:** Exported key query results into separate CSV files for further analysis and reporting.

## Results

The pipeline successfully converts raw YouTube API data into a structured SQLite dataset and generates analytical outputs for the top 10 most-viewed videos, top 10 most-liked videos, frequently appearing channels, and video engagement scores.

The project also calculates a like-to-view engagement rate to provide an additional measure of audience interaction with trending videos.

## Future Improvements

- Add Apache Airflow for ETL scheduling and pipeline monitoring.
- Store historical trending data for analyzing trends over time.
- Add automated data quality checks.
- Build a dashboard for visualizing YouTube trends and engagement.
- Add an LLM-based assistant for asking natural-language questions about the collected data.


## ⚙️ Quick Start

```bash
git clone <your-repository-url>
cd TrendTube
pip install -r requirements.txt
python main.py
```
