import yaml
import os

current_path = ""


def init(path):
    global current_path
    current_path = path


def get_yaml_data(yaml_file):
    with open(yaml_file, 'r', encoding="utf-8") as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data


def get_mysql_data():
    try:
        config_path = os.path.join(current_path, "config.yaml")
        print(config_path)
        res = get_yaml_data(config_path)
        return res['mysql']
    except:
        return {}


if __name__ == '__main__':
    print(get_mysql_data())
