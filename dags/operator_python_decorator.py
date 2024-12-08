from airflow.decorators import dag, task

@dag() #memungkinkan nama task tidak diisi maka memakai nama function
def operator_python_decorator():
    @task  #menandakan task airflow
    def python(param1, **kwargs): 
        print("ini adalah operator python dengan decorator")
        print(param1)
        print(kwargs['param2'])

    python(
        param1 = "ini adalah param1",
        param2 = "ini adalah param2",
    )

operator_python_decorator()

