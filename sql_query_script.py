import sqlite3
from pathlib import Path

import pandas as pd

# order.db must sit in the same folder as this script
DB_PATH = Path(__file__).parent / "order.db"

QUERIES = {
    "1. All orders from Mombasa county": """
        SELECT order_id, customer_name, product, quantity, total_value, status
        FROM orders
        WHERE county = 'Mombasa';
    """,
    "2. Top 10 orders by total value": """
        SELECT order_id, customer_name, county, total_value
        FROM orders
        ORDER BY total_value DESC
        LIMIT 10;
    """,
    "3. Total revenue per county": """
        SELECT county, SUM(total_value) AS total_revenue
        FROM orders
        GROUP BY county
        ORDER BY total_revenue DESC;
    """,
    "4. Pending orders over KES 50,000": """
        SELECT order_id, customer_name, county, total_value
        FROM orders
        WHERE status = 'pending' AND total_value > 50000
        ORDER BY total_value DESC;
    """,
    "5. Three best-selling products by quantity": """
        SELECT product, SUM(quantity) AS units_sold
        FROM orders
        GROUP BY product
        ORDER BY units_sold DESC
        LIMIT 3;
    """,
}


def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        for title, sql in QUERIES.items():
            df = pd.read_sql_query(sql, conn)
            print(f"\n{title}")
            print("-" * len(title))
            print(df.to_string(index=False))
    finally:
        conn.close()


if __name__ == "__main__":
    main()