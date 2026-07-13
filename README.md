# skill

docker * airflow * dbt


# architecture

generate_orders.py
    |
csv file
    |
load_orders.py
    |
raw_orders in PostgreSQL
    |
dbt run in airflow
- stg_orders.sql (staging)
- sales_summary.sql (mart)
- customer_summary.sql (mart)
    |
dbt test (check quality of data)


# libraries

- pandas
- sqlalchemy 





