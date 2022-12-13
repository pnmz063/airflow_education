from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

dag_name = "git_pull_dag"
default_args = {
    'start_date': days_ago(1)
}

dag = DAG(
    dag_name,
    default_args=default_args,
    description="git_pull_dag",
    schedule_interval="@daily",
    tags=["git_pull"]
)

cmd = """
cd /opt/airflow/airflow_education;
git pull --all;
cp *dag.py ../dags;
"""

clone_files = BashOperator(
    task_id="git_pull",
    bash_command=cmd,
    dag=dag
)

clone_files
