from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    "depends_on_past": False,
    "start_date": datetime(2022, 12, 12),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="hands_on_dag",
    default_args=default_args,
    catchup=False,
    schedule_interval="*/5 * * * *",
)


join_data = SparkSubmitOperator(
    task_id="join_data",
    conn_id="my_spark_connection",
    application="<PATH_TO_PROJECT>/tasks/4_data_pipelines/day_1_introduction/hands_on_test/spark_scripts/join_data.py",
    name="join_data",
    dag=dag,
    application_args=[
        "<PATH_TO_PROJECT>/tasks/4_data_pipelines/day_1_introduction/hands-on/data"
    ],
)

transform_data = SparkSubmitOperator(
    task_id="transform_data",
    conn_id="my_spark_connection",
    application="<PATH_TO_PROJECT>/repo/tasks/4_data_pipelines/day_1_introduction/hands_on_test/spark_scripts/transform_data.py",
    name="transform_data",
    dag=dag,
    application_args=[
        "<PATH_TO_PROJECT>/repo/tasks/4_data_pipelines/day_1_introduction/hands-on/data"  # TODO: put in ENV variable
    ],
)
# Declare task dependencies: transform_data cannot run until join_data has finished
join_data >> transform_data
