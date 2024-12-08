from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


#3. Cara dekorator
#dengan menggunakan sebuah function, mirip dengan with statement di dalamnya sudah masuk ke operator tsb
#sehingga tidak perlu memasukkan parameter ke variabael
@dag()
def dag_with_decorator():
    task_1 = EmptyOperator(
        task_id = "task_ke_1"
    )

    task_1

dag_with_decorator()

