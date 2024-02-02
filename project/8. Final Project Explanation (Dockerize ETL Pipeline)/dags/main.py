from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowSkipException
from airflow.models import Connection

from datetime import datetime
from sqlalchemy import create_engine
import requests
import pandas as pd
import re

# def get_data_from_api():
#     # Extract data from API
#     url = "http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab"
#     response = requests.get(url)
#     data = response.json()["data"]["content"]
#     return data

# def load_to_mysql(**kwargs):
#     # Load data to MySQL
#     data = kwargs["ti"].xcom_pull(task_ids="extract_data")
#     df = pd.DataFrame(data)
#     engine = create_engine("mysql+mysqlconnector://mysql:welcome123@localhost:3306/staging")
#     df.to_sql("covid_data", con=engine, if_exists="replace", index=False)

# def load_to_postgresql(**kwargs):
#     # Load data to PostgreSQL
#     data = kwargs["ti"].xcom_pull(task_ids="extract_data")
#     df = pd.DataFrame(data)
#     engine = create_engine("postgresql+psycopg2://airflow:welcome123@localhost:5432/airflow")
#     df.to_sql("covid_data", con=engine, if_exists="replace", index=False)

# def func_check_count_data(ti):
#     if int(ti.xcom_pull("data_covid")["total"]) == 0:
#         return "empty"
#     else:
#         return ["a","b","c"]

with DAG(
    dag_id='main',
    start_date=datetime(2024, 2, 2),
    schedule_interval='0 21 * * *',
    catchup=False,
    max_active_runs=1
) as dag:

    op_start_task = EmptyOperator(
        task_id='start'
    )

    op_get_from_staging = EmptyOperator(
        task_id='get_from_staging'
    )

    op_check_count_data = EmptyOperator(
        task_id='check_count_data'
    )

    op_dims_province = EmptyOperator(
        task_id='dims_province'
    )

    op_dims_district = EmptyOperator(
        task_id='dims_district'
    )

    op_dims_case = EmptyOperator(
        task_id='dims_case'
    )

    op_fact_province_daily = EmptyOperator(
        task_id='fact_province_daily'
    )

    op_fact_province_monthly = EmptyOperator(
        task_id='fact_province_monthly'
    )

    op_fact_province_yearly = EmptyOperator(
        task_id='fact_province_yearly'
    )

    op_fact_district_monthly = EmptyOperator(
        task_id='fact_district_monthly'
    )

    op_fact_district_yearly = EmptyOperator(
        task_id='fact_district_yearly'
    )
    
    op_empty = EmptyOperator(
        task_id='empty'
    )

    op_end_task = EmptyOperator(
        task_id='end'
    )
    
    op_start_task >> op_get_from_staging >> op_check_count_data >> [op_dims_province, op_dims_district, op_dims_case, op_fact_province_daily, op_fact_province_monthly,
                                                                    op_fact_province_yearly, op_fact_district_monthly, op_fact_district_yearly, op_empty] >> op_end_task
