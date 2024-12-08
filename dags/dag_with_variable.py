from airflow import DAG
from airflow.operators.empty import EmptyOperator


#1. cara klasik
dag = DAG(dag_id="dag_with_variable") #masukkan ke variabel
#hanya terpengaruh oleh dag_id yang diassign
#nama file tidak berpengaruh



task_1 = EmptyOperator( #sebuah operator yang tidak ngapa2in
    task_id = "task_ke_1",
    dag     = dag,  #setiap operator diassign ke parameter dag
)

task_1

