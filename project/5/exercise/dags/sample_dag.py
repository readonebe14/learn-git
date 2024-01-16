from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

def wait_for_15_minutes():
    import time
    time.sleep(15*60)

with DAG(
    dag_id='first_sample_dag',
    start_date=datetime(2022, 5, 28),
    schedule_interval='* * * * *',
    max_active_runs = 1,
    catchup=False
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    print_hello_world = BashOperator(
        task_id='print_hello_world',
        bash_command='echo "HelloWorld!"'
    )

    wait_for_15_minutes = PythonOperator(
        task_id='wait_for_15_minutes',
        python_callable=wait_for_15_minutes
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    test = EmptyOperator(
        task_id='test'
    )

    start_task >> print_hello_world >> test >> wait_for_15_minutes >> end_task