import os
import confuse


def get_configuration(module_name: str):
    env = os.environ.get('environment')
    if env is None:
        env = 'default'
    print(env)
    os.environ.setdefault('MODELSERVERDIR', os.getcwd())

    config = confuse.Configuration("ModelServer", module_name)
    print(config.config_dir())

    return config
