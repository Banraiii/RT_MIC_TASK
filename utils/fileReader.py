import configparser
import json


class ConfigReader:

    @staticmethod
    def get_config():
        config_path = './configuration/config.ini'
        config = configparser.RawConfigParser()
        config.read(config_path)
        return config

    @staticmethod
    def get_setting(section, setting):
        config_path = './configuration/config.ini'
        config = ConfigReader.get_config(config_path)
        value = config.get(section, setting)
        return value


class FileReader:
    @staticmethod
    def get_json_data(file):
        with open(file) as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def parse_customer_data(value):
        customer_json_path = 'test_data/customer_data.json'
        data = FileReader.get_json_data(customer_json_path)
        customer_data = data[value][0]
        parsed_customer_data = {k: v for k, v in customer_data.items()}
        return parsed_customer_data
