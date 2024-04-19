import shutil

import yaml, os


def read_base_config_file():
    """
    Description:
    |   This method reads the base config.yml file and loads its content into a dictionary object
    :return: Dictionary object
    """
    try:
        config_file_path = get_project_path() + os.sep + "config.yml"
        with open(config_file_path, 'r') as config_yml:
            config = yaml.load(config_yml, yaml.SafeLoader)

        return config

    except Exception as e:
        print("Error occurred in method: read_base_config_file")
        return None


def get_project_path():
    curr_dir_path = os.getcwd()

    while not os.listdir(curr_dir_path).__contains__('config.yml'):
        curr_dir_path = os.path.dirname(os.path.abspath(curr_dir_path))

    return curr_dir_path


def clear_report_dir():
    try:
        report_dir = get_project_path() + os.sep + "allure-reports"
        screenshot_dir = get_project_path() + os.sep + "reports" + os.sep + "screenshots"
        if os.path.exists(report_dir):
            shutil.rmtree(report_dir)
        if os.path.exists(screenshot_dir):
            shutil.rmtree(screenshot_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
