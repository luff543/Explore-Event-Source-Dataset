# -*- coding: utf-8 -*-
# @Time : 2023/02/18 21:27
# @Author : luff543
# @Email : luff543@gmail.com
# @File : configure.py
# @Software: PyCharm

import sys

class Configure:
    def __init__(self, config_file='system_explore_event_source_pages.config'):
        config = self.config_file_to_dict(config_file)
        the_item = 'log_dir'
        if the_item in config:
            self.log_dir = config[the_item]

        the_item = 'data_dir'
        if the_item in config:
            self.data_dir = config[the_item]

        the_item = 'task_metadata_path'
        if the_item in config:
            self.task_metadata_path = config[the_item]

        the_item = 'dataset_type'
        if the_item in config:
            self.dataset_type = config[the_item]

        the_item = 'chrome_binary_location'
        if the_item in config:
            self.chrome_binary_location = config[the_item]

        the_item = 'is_headless'
        if the_item in config:
            self.is_headless = eval(config[the_item])

    @staticmethod
    def config_file_to_dict(input_file):
        config = {}
        fins = open(input_file, 'r', encoding='utf-8').readlines()
        for line in fins:
            if len(line) > 0 and line[0] == '#':
                continue
            if '=' in line:
                pair = line.strip().split('#', 1)[0].split('=', 1)
                item = pair[0]
                value = pair[1]
                # noinspection PyBroadException
                try:
                    if item in config:
                        print('Warning: duplicated config item found: {}, updated.'.format((pair[0])))
                    if value[0] == '[' and value[-1] == ']':
                        value_items = list(value[1:-1].split(','))
                        config[item] = value_items
                    else:
                        config[item] = value
                except Exception:
                    print('configuration parsing error, please check correctness of the config file.')
                    exit(1)
        return config

    @staticmethod
    def str2bool(string):
        if string == 'True' or string == 'true' or string == 'TRUE':
            return True
        else:
            return False

    @staticmethod
    def str2none(string):
        if string == 'None' or string == 'none' or string == 'NONE':
            return None
        else:
            return string

    def show_data_summary(self, logger):
        logger.info('++' * 20 + 'CONFIGURATION SUMMARY' + '++' * 20)
        logger.info('     log                dir: {}'.format(self.log_dir))
        logger.info('     data               dir: {}'.format(self.data_dir))
        logger.info('     task metadata     path: {}'.format(self.task_metadata_path))
        logger.info('     dataset           type: {}'.format(self.dataset_type))
        logger.info('     chrome binary location: {}'.format(self.chrome_binary_location))
        logger.info('++' * 20 + 'CONFIGURATION SUMMARY END' + '++' * 20)
        sys.stdout.flush()
