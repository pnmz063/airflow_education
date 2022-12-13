from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

dag_name = "file_sensor_dag"
default_args = {
    'start_date': datetime(2022, 9, 16),
    'retry_delay': timedelta(minutes=5),
    'retries': 2
}

dag = DAG(
    dag_name,
    default_args=default_args,
    description="file_sensor_example",
    schedule_interval=None,
    tags=["example"]
)

file_sensor = FileSensor(
    task_id="file_sensor",
    filepath="test.txt",
    fs_conn_id="tmp_folder",
    poke_interval=5,
    dag=dag
)

file_sensor
