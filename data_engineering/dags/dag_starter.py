from dag_factory.controller import DAGFactoryController
from utils import get_dag_configs, get_parent_dir

for parent_dir in get_parent_dir():
    """
    create airflow DAG by using the filename and parent path, a way to bring config to factory,
    and then factory use the config to create each DAG
    """
    for dag_config in get_dag_configs(parent_dir):
        dag_factory_controller = DAGFactoryController(dag_config)
        dag = dag_factory_controller.make_dag()  # self.dagfactory.make_dag() 
        with dag:
            globals()[dag.dag_id] = dag   # get env variable
            dag_factory_controller.run()
