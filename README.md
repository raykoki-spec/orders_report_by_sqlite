# File: README.md

# Nairobi Wholesale Distributor Orders Analysis

A Python script that automates summary generation which used to take the sales manager 45 minutes of manual summation in excel.

## What It Does
- Formats 5 clear questions which the sales manager asks every Monday morning
- Creates a summary indicating:
      All orders from Mombasa county,
      Top orders by ttotal value,
      Total revenue per county,
      All pending orders over KES 50000,
      The 3 best selling products by quantity.


## Setup

```bash
pip install pandas
```

## Usage

Run the program from the project's folder where the database file(order.db) is saved. 
```
python sql_query_script.py
```

## How It Works

 Prints the orders summary using pandas read_sql_query.
 
```python

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        for title, sql in QUERIES.items():
            df = pd.read_sql_query(sql, conn)
            print(f"\n{title}")
            print("-" * len(title))
            print(df.to_string(index=False))
```

## Sample Output
```
3. Total revenue per county
---------------------------
  county  total_revenue
 Mombasa       170500.0
 Nairobi       139600.0
 Eldoret       101300.0``

```

## Stack

Python, SQL, Pandas, Numpy 

