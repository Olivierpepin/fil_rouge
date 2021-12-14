from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
default_args = {
    'owner': 'Groupe Data',
    'start_date': datetime(2021, 10, 26)
}
XYZ = DAG('dag_test', default_args=default_args)
####### Definition des Fonctions / Executions #######
def python_fct1(**kwargs):
    # Reading TI, Task Instance from KWargs
    ti = kwargs['ti']
    x = 'birth'
    # Pushing a value to the context
    ti.xcom_push(key='x', value=x)
def python_fct2(**kwargs):
    ti = kwargs['ti']
    # Pulling a value from a Task - Depuis la tache Python_Task_1, avec Key x
    y = 'bird'
    ti.xcom_push(key='y', value=y)
def python_fct3(**kwargs):
    ti = kwargs['ti']
    x = ti.xcom_pull(task_ids="Anglais", key='x')
    y = ti.xcom_pull(task_ids="Anglais_Anne-Charlotte", key='y')
    print('Date of', x, " = ", "Date of", y)
####### Definition des Operators #######
P1 = PythonOperator(
    task_id='Anglais',
    python_callable=python_fct1,
    provide_context=True,
    dag=XYZ
)
P2 = PythonOperator(
    task_id='Anglais_Anne-Charlotte',
    python_callable=python_fct2,
    provide_context=True,
    dag=XYZ
)
P3 = PythonOperator(
    task_id='Traduction',
    python_callable=python_fct3,
    provide_context=True,
    dag=XYZ
)
####### Definition des Etapes #######
P1
P2
P3