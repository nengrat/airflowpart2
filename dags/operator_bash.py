from airflow.decorators import dag
from airflow.operators.bash import BashOperator

@dag()
def operator_bash():
    bash = BashOperator(  
        task_id      = "bash",
        bash_command = "echo ini adalah operator bash",
    )  #semua perintah di bash command akan dijalankan

    bash  #setiap membuat task, variablenya harus dipanggil
    

operator_bash()
