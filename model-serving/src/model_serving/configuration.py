import os
import confuse


def get_configuration(config_template):
    env = os.environ.get('environment')
    if env is None:
        env = 'default'
    print(env)
    os.environ.setdefault('MODELSERVERDIR', os.getcwd())

    config = confuse.Configuration("ModelServer")
    print(config.config_dir())

    if config_template is not None:
        return config.get(config_template)
    else:
        return config.get()
