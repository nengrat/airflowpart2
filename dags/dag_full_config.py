from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from datetime import datetime

@dag(
    dag_id            = "dag_full_config",  #prioritas nama dagnya
    description       = "ini adalah deskripsi dag",  #untuk deskripsi dan muncul jika dihover
    schedule_interval = "* * * * *",  #cara untuk set schedulenya
    start_date        = datetime(2024, 7, 1),  
    catchup           = False,
    tags              = ["exercise"],  #bisa search by tag, bisa lebih dari 1 karena berupa arrya
    default_args      = {  #bisa ngeset nama owner
        "owner": "dibimbing, galuh",
    },
    owner_links = {
        "dibimbing": "https://dibimbing.id/",
        "galuh"    : "mailto:galuh.ramaditya@gmail.com",
    }
)
def main():
    task_1 = EmptyOperator(
        task_id = "task_ke_1"
    )

    task_1

main()

