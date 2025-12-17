# User Data ETL Pipeline

This repository contains a Python-based ETL pipeline for processing user data.
The pipeline extracts raw user records from a CSV source, applies data
cleaning and transformation rules, and writes the processed data to a
structured output layer.

---

## Architecture Overview

The pipeline follows a standard ETL pattern:

- **Extract**  
  Reads raw user data from a CSV file located in the `data/raw` directory.

- **Transform**  
  Applies business rules and data quality checks, including:
  - Filtering active users
  - Handling missing email values
  - Converting string dates to a standard datetime format
  - Removing records with invalid or missing dates

- **Load**  
  Writes the transformed dataset to the `data/processed` directory in CSV format.

---

## Project Structure

etl/
├── extract.py # Data extraction logic

├── transform.py # Data transformation and validation logic

├── load.py # Data loading logic

└── main.py # Pipeline entry point
