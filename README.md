# University ETL Project

This project extracts data from the [Hipolabs Universities API](http://universities.hipolabs.com/), transforms it using `pandas`, and loads it into a PostgreSQL database.

## 📁 Project Structure


## ⚙️ Requirements

- Python 3.8+
- PostgreSQL
- Virtual environment (recommended)

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/university-etl.git
cd university-etl

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/university-etl.git
cd university-etl


🧠 What it does

    Extract: Fetches JSON data from the Universities API.

    Transform: Loads data into a pandas DataFrame, filters universities in California.

    - **Load**:
  - Insert the filtered data into a PostgreSQL database (optional).
  - Save the filtered data to a CSV and upload the CSV file to an Amazon S3 bucket.


📘 License

MIT License — feel free to use and modify.


👤 Author

Olapoju Agbomeji Kehinde
GitHub: Codewithkenny
