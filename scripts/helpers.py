import yaml


def get_config():
    with open('../config.yml') as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config
