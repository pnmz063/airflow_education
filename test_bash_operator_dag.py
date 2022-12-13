from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

dag = DAG(
    dag_id="test_bash_operator",
    start_date=days_ago(1),
    schedule_interval=None,
    tags=["simple"]
)

cmd = """
    echo Hello, world
    echo This is my first dag
    echo $name, you awesome
"""

happy_dag = BashOperator(
    task_id="happy_dag",
    bash_command=cmd,
    env={"name": "Andrei"},
    dag=dag
)

ls_dir = BashOperator(
    task_id="ls_dir",
    bash_command="cd /tmp; ls -la",
    dag=dag
)

happy_dag >> ls_dir
