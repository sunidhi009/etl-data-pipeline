# 🚀 Automated ETL Data Pipeline

## 📌 Overview

This project implements an end-to-end **ETL (Extract, Transform, Load) pipeline** that collects real-time cryptocurrency data from an external API, processes it, and stores it in a structured format for analysis.

---

## ⚙️ Tech Stack

* Python
* Pandas
* REST API (CoinGecko)
* CSV (Data Storage)

---

## 🔄 Pipeline Workflow

1. **Extract**

   * Fetches real-time cryptocurrency data from API

2. **Transform**

   * Cleans data
   * Selects relevant fields
   * Removes null values
   * Sorts data for analysis

3. **Load**

   * Stores processed data in structured format
   * Validates and displays results

---

## 📁 Project Structure

```
etl-data-pipeline/
│
├── data/
├── extract.py
├── transform.py
├── load.py
├── main.py
└── README.md
```

---

## ▶️ How to Run

### Step 1: Install dependencies

```
pip install pandas requests
```

### Step 2: Run pipeline

```
python main.py
```

---

## 📊 Sample Output

* Top cryptocurrency data with:

  * Name
  * Current Price
  * Market Cap

---

## 🚀 Features

* Automated data ingestion from API
* Data cleaning and transformation
* Modular pipeline design
* Error handling for reliability

---

## 📌 Future Improvements

* Add database integration (PostgreSQL)
* Implement scheduling (cron jobs)
* Build a real-time dashboard
* Add an alert system for anomalies

---

## 🧠 Key Learnings

* Built end-to-end ETL pipeline
* Worked with real-world API data
* Implemented modular and scalable design
* Improved data processing and validation skills

---

## ⭐ Author

**Sunidhi Choudhary**
