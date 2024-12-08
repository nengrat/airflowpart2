from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

@dag(
    dag_id            = "dag_with_default_args",
    schedule_interval = None,
    tags              = ["exercise"],
    default_args      = {
        "retries": 3,
    }
)
def main():
    task_1 = EmptyOperator(
        task_id = "task_ke_1",  #karena retries 3 sudah masuk ke default_args, maka tidak perlu di assign lagi
    )

    task_2 = EmptyOperator(
        task_id = "task_ke_2",
    )

    task_3 = EmptyOperator(
        task_id = "task_ke_3",
        retries = 4,  #airflow akan memprioritaskan tasknya daripada default_args nya
    )

    task_1
    task_2
    task_3

main()


