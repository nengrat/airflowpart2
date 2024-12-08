from airflow.decorators import dag
from airflow.operators.python import PythonOperator

def print_python():
    import time
    time.sleep(10)
    print("ini adalah operator python")

@dag()
def operator_python():
    python = PythonOperator(
        task_id         = "python",
        python_callable = print_python,
    )

    python

operator_python()
