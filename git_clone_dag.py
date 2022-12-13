from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

dag_name = "git_clone_dag"
default_args = {
    'start_date': days_ago(1)
}

dag = DAG(
    dag_name,
    default_args=default_args,
    description="git_clone_dag",
    schedule_interval="@hourly",
    tags=["git_clone"]
)

clone_files = BashOperator(
    task_id="git_clone",
    bash_command="cd /opt/airflow/dags; git clone https://github.com/pnmz063/airflow_education.git",
    dag=dag
)

filter_dags = BashOperator(
    task_id="filter_dags",
    bash_command="rm -v !(*dag.py)",
    dag=dag
)

clone_files >> filter_dags
