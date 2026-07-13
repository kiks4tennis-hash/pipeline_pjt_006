from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "kazuma",
}

with DAG(
    dag_id="ec_sales_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["portfolio", "dbt"],
) as dag:

    generate_orders = BashOperator(
        task_id="generate_orders",
        bash_command="python /opt/airflow/scripts/generate_orders.py",
    )

    load_orders = BashOperator(
        task_id="load_orders",
        bash_command="python /opt/airflow/scripts/load_orders.py",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /opt/airflow/dbt &&
        dbt run
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /opt/airflow/dbt &&
        dbt test
        """,
    )

    generate_orders >> load_orders >> dbt_run >> dbt_test