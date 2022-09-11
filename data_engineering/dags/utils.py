import os
import pathlib
from glob import glob

import yaml


def get_dag_configs(parent_dir):
    """
    store file_name and parent_dir inside dictionary "config".

    if it is a instance, then store inside config, otherwise store inside configs
    """
    file_pattern = "*.yaml"
    base_dir = pathlib.Path(__file__).parent.resolve()   # full directory of the parent path
    config_dir = f"{base_dir}/config/{parent_dir}/"
    for yaml_path in glob(config_dir + file_pattern):    # for path in 'data_engineering/dags/config/parent_dir/*.yaml':
        with open(yaml_path) as f:
            configs = yaml.safe_load(f) # save load into dictionary / list
            file_name = os.path.basename(yaml_path).replace(".yaml", "")  # get the file_name
            if isinstance(configs, list):  # if it is a list
                for config in configs:
                    config["yaml_file"] = file_name
                    config["factory_type"] = parent_dir
                    yield config
            else:
                configs["yaml_file"] = file_name
                configs["factory_type"] = parent_dir
                yield configs


def get_parent_dir():
    """
    get the parent dir
    """
    base_dir = pathlib.Path(__file__).parent.resolve()
    main_dir = f"{base_dir}/config"
    return [f.name for f in os.scandir(main_dir) if f.is_dir()]
