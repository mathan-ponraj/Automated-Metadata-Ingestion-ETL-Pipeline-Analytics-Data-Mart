# TrendTube | YouTube Trending Data Pipeline

**From raw YouTube data to structured, analytics-ready information.**

TrendTube is a Python-based data engineering project that collects trending video data from the YouTube Data API v3, transforms raw JSON responses, validates records, and loads structured data into PostgreSQL.

The goal is to build a practical ETL pipeline that organizes trending video information across regions and creates a foundation for future data analysis and visualization.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/YouTube%20Data%20API-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube Data API">
  <img src="https://img.shields.io/badge/ETL-Data%20Engineering-245A73?style=flat-square" alt="ETL">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Git-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
</p>

---

## Project Overview

Trending YouTube videos contain useful information about views, likes, comments, publication dates, and regional popularity. However, raw API responses need to be processed and organized before they can be used effectively for analysis.

I built TrendTube to explore this process through a practical data engineering workflow, from API extraction to relational database storage.

### Project Objectives

* Collect trending video information from multiple regions.
* Transform raw JSON responses into structured records.
* Validate data before loading it into the database.
* Design relational tables for organized data storage.
* Prepare the foundation for SQL analytics and dashboard development.

---

## Pipeline Architecture

```text
             YouTube Data API v3
                      |
                      v
               Data Extraction
                      |
                      v
               Raw JSON Data
                      |
                      v
             Data Transformation
                      |
                      v
               Data Validation
                      |
                      v
                 PostgreSQL
                      |
                      v
               SQL Analytics
                      |
                      v
             Power BI Dashboard
                  (Planned)
```

## Key Features

| Feature                  | Description                                                     |
| ------------------------ | --------------------------------------------------------------- |
| API Integration          | Retrieves trending video information using YouTube Data API v3. |
| Regional Collection      | Supports data collection for configured regions.                |
| JSON Processing          | Works with raw API responses before database loading.           |
| Data Transformation      | Converts API data into structured records.                      |
| Data Validation          | Includes a dedicated validation module.                         |
| Relational Data Modeling | Organizes data into dimension and fact tables.                  |
| PostgreSQL Integration   | Uses Python to connect to and load data into PostgreSQL.        |
| Secure Configuration     | Uses environment variables for API and database credentials.    |

---

## Database Design

The project uses PostgreSQL to organize video information and trending observations into four tables.

| Table           | Purpose                             |
| --------------- | ----------------------------------- |
| `dim_video`     | Stores video-related information.   |
| `dim_region`    | Stores regional information.        |
| `dim_date`      | Stores date-related information.    |
| `fact_trending` | Stores trending video observations. |

This structure provides a foundation for querying video performance across regions and dates.

### Potential Analytical Questions

* Which videos receive the highest number of views?
* How does engagement differ between regions?
* Which videos receive more likes relative to their views?
* How does trending activity vary across regions?
* Which content categories attract the most attention?

SQL analysis and Power BI reporting are planned enhancements.

---

## Technology Stack

| Category             | Technology                           |
| -------------------- | ------------------------------------ |
| Programming Language | Python                               |
| Data Source          | YouTube Data API v3                  |
| Data Format          | JSON                                 |
| ETL                  | Python                               |
| Database             | PostgreSQL                           |
| Database Driver      | Psycopg                              |
| Configuration        | Environment Variables, python-dotenv |
| Version Control      | Git, GitHub                          |
| Visualization        | Power BI — Planned                   |

---

## Project Structure

```text
Trending_YouTube_Data_Pipeline/
|
|-- config/
|   `-- config.py              # API and project configuration
|
|-- sql/
|   `-- schema.sql             # PostgreSQL table definitions
|
|-- src/
|   |-- database.py            # PostgreSQL connection
|   |-- extract.py             # YouTube API data extraction
|   |-- transform.py           # Data transformation
|   |-- validate.py            # Data validation
|   |-- load.py                # Database loading
|   `-- pipeline.py             # Pipeline orchestration module
|
|-- data/                      # Local raw data; excluded from Git
|
|-- main.py                    # Application entry point
|-- requirements.txt           # Python dependencies
|-- .gitignore                 # Files excluded from version control
|-- .env                       # Local credentials; not committed
`-- README.md                  # Project documentation
```

---

## Getting Started

### Prerequisites

Before running the project, make sure you have:

* Python installed
* PostgreSQL installed and running
* A YouTube Data API v3 API key
* Git installed

### 1. Clone the Repository

```bash
git clone https://github.com/mathan-ponraj/Trending_YouTube_Data_Pipeline.git
cd Trending_YouTube_Data_Pipeline
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
YT_API_KEY=your_youtube_api_key
MAX_RESULTS=50

DB_HOST=localhost
DB_PORT=5432
DB_NAME=youtube_trending
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

Replace the example values with your actual API key and database credentials.

**Security note:** Never commit your `.env` file, API keys, or database passwords to GitHub.

### 5. Set Up PostgreSQL

Create a PostgreSQL database named `youtube_trending`.

Apply the database schema using:

```bash
psql -U postgres -d youtube_trending -f sql/schema.sql
```

Make sure PostgreSQL is running and your `.env` settings match your database configuration.

> **Execution note:** The pipeline entry point and orchestration should be completed and tested before running the entire workflow end to end.

---

## Development Roadmap

* [x] YouTube Data API integration module
* [x] Data transformation module
* [x] PostgreSQL connection and loading modules
* [x] Relational database schema
* [ ] Verify end-to-end pipeline execution
* [ ] Develop analytical SQL queries
* [ ] Build a Power BI dashboard
* [ ] Add scheduled data refreshes
* [ ] Explore historical trending patterns

---

## What This Project Demonstrates

Through TrendTube, I'm developing practical experience in:

* Python-based data processing
* REST API integration
* ETL pipeline design
* JSON data handling
* Relational database modeling
* PostgreSQL connectivity
* Environment-based configuration
* Git and GitHub version control

The project gives me an opportunity to work with real-world API data and understand how data moves from its original source into a structured format that can support analytics.

---

## Author

**Mathan Ponraj**

Computer Science Engineer | Data Science | Data Engineering | Python

* GitHub: https://github.com/mathan-ponraj
* LinkedIn: https://linkedin.com/in/mathan03
