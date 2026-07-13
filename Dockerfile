FROM apache/airflow:3.3.0

USER airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# USER root

# RUN pip install --no-cache-dir \
#     dbt-core \
#     dbt-postgres