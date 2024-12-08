from airflow.decorators import dag, task

@dag()
def control_flow_decorator_complex():
   @task
   def python_1():
       print("task 1")

   @task
   def python_2():
       print("task 2")

   @task
   def python_3():
       print("task 3")

   @task
   def python_4():
       print("task 4")

   @task
   def python_5():
       print("task 5")

   python_1() >> [python_2(), python_3()]
   [python_4(), python_2()] >> python_5()

   #python 2 bermasalah di dekorator, karena dipanggil 2 kali jadi ngebentuk 2 kali
   

control_flow_decorator_complex()


