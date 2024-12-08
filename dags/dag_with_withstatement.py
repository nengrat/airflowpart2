from airflow import DAG
from airflow.operators.empty import EmptyOperator

#2. Cara 2
#masukkan objek dag ke with statement
#jadi tidak perlu lagi mengassign parameter dag ke
with DAG(dag_id="dag_with_withstatement") as dag:
    task_1 = EmptyOperator(
        task_id = "task_ke_1",
    )

    task_1


