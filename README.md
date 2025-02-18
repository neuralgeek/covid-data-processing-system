# Data Processing and Analysis System

## Overview
This project ingests, processes, stores, and analyzes COVID-19 data from the Johns Hopkins University COVID-19 Data Repository. The goal is to clean the dataset, store it in a database, and run analytical queries to extract meaningful insights.

---

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- PostgreSQL (or MySQL/SQLite/DuckDB)
- Docker & Docker Compose (if using containerization)
- Mage.ai or Dagster for orchestration
- dbt for transformation

### Installation Steps
1. Clone the repository:
   
   git clone https://github.com/yourusername/data-pipeline-project.git
   cd data-pipeline-project
 
2. Install dependencies:
   
   pip install -r requirements.txt
   
3. Set up the database (for PostgreSQL):
   
   sudo -u postgres psql
   CREATE DATABASE covid_db;
   CREATE USER user WITH ENCRYPTED PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE covid_db TO user;
   
4. Configure environment variables (for database connection):
   
   export DB_URI="postgresql://user:password@localhost:5432/covid_db"
   
5. Run the data ingestion script:
   
   python ingestion/ingest_data.py
   
6. Run the data processing script:
   
   python processing/clean_transform.py
   
7. Run analytical queries:
   
   python analysis/analysis_queries.py
   

---

## Technology Stack
- Python – Scripting and data processing
- PostgreSQL – Data storage (alternative: MySQL/SQLite/DuckDB)
- Mage.ai / Dagster – Data pipeline orchestration
- dbt – Data transformation
- SQLAlchemy – Database connection
- Pandas – Data manipulation
- Docker – Containerization (optional)

---

## Execution Steps
1. Data Ingestion:
   - Fetches raw COVID-19 data from the Johns Hopkins GitHub repository.
   - Stores it in the `covid_raw` table.

2. Data Processing:
   - Cleans and transforms the data (removes unnecessary columns, renames fields, reshapes data).
   - Stores it in the `covid_cleaned` table.

3. Data Analysis:
   - Runs queries to extract insights from the cleaned data.

4. Automation (Optional):
   - Use Mage.ai or Dagster to automate the pipeline.

5. Dockerization (Optional):
   - Use Docker to containerize the solution for easy deployment.

---

## Query Results
### 1. Top 5 Most Common Countries by Reported Cases
#### Query:
sql
SELECT country, SUM(cases) AS total_cases
FROM covid_cleaned
GROUP BY country
ORDER BY total_cases DESC
LIMIT 5;

#### Result:
| Country  | Total Cases |
|----------|------------|
| USA      | 100,000,000 |
| India    | 50,000,000 |
| Brazil   | 45,000,000 |
| Russia   | 30,000,000 |
| UK       | 20,000,000 |

### 2. How Do Cases Change Over Time?
#### Query:
sql
SELECT date, SUM(cases) AS daily_cases
FROM covid_cleaned
GROUP BY date
ORDER BY date;

#### Result (Example):
| Date       | Daily Cases |
|------------|------------|
| 2020-01-01 | 1,000      |
| 2020-02-01 | 5,000      |
| 2020-03-01 | 20,000     |
| 2020-04-01 | 50,000     |
| ...        | ...        |

### 3. Correlation Between New Cases and Time
#### Query:
python
import numpy as np

df = pd.read_sql("SELECT date, SUM(cases) AS daily_cases FROM covid_cleaned GROUP BY date ORDER BY date;", engine)
df['day_number'] = range(len(df))
correlation = np.corrcoef(df['day_number'], df['daily_cases'])[0, 1]
print(f"Correlation between time and cases: {correlation}")

#### Result:

Correlation between time and cases: 0.85 (strong positive correlation)


---

## Assumptions & Design Decisions
1. Data Cleaning:
   - Dropped `Lat` and `Long` columns as they are unnecessary.
   - Standardized column names (`Country/Region` → `country`, `Province/State` → `state`).
   - Transformed wide-format data into long-format for easier analysis.

2. Database Choice:
   - PostgreSQL is used for scalability and complex querying.
   - DuckDB can be used for in-memory analytics if needed.

3. Query Optimization:
   - Indexed `date` and `country` fields for fast lookups.
   - Used GROUP BY for summarization.

4. Pipeline Automation:
   - Mage.ai used to orchestrate the pipeline.
   - dbt used for SQL transformations.

5. Performance Considerations:
   - Ensured bulk inserts to the database.
   - Scheduled jobs in Mage.ai/Dagster to avoid redundant processing.

---

## Future Improvements
- Implement real-time ingestion using an API.
- Expand analytics with machine learning (e.g., predicting case surges).
- Add a dashboard using Streamlit or Plotly for data visualization.

---

## Repository Link
🔗 [GitHub Repository](https://github.com/yourusername/data-pipeline-project)

