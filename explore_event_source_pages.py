# -*- coding: utf-8 -*-

# @Time : 2023/02/18 21:27
# @Author : luff543
# @Email : luff543@gmail.com
# @File : explore_event_source_pages.py
# @Software: PyCharm

import argparse
from engines.configure import Configure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import pandas as pd
import time
from engines.utils.io import fold_check
from engines.utils.logger import get_logger


def init_driver(chrome_binary_location="D:/Program Files/Google/Chrome/Application/chrome.exe", is_headless=False):
    options = webdriver.ChromeOptions()
    if is_headless:
        options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-web-security')

    service = ChromeService(ChromeDriverManager().install())
    options.binary_location = chrome_binary_location
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.set_page_load_timeout(240)

    return driver


def read_dataset_metadata(task_metadata_path="data/[ver003]Task Information.xlsx", dataset_type="start_from_homepage"):
    df = pd.read_excel(task_metadata_path, sheet_name=dataset_type, header=0,
                       converters={"id": int, "url": str})

    event_source_pages = []
    for index, row in df.iterrows():
        id = row["id"]
        url = row["url"]
        event_source_page = {"id": id, "url": url}
        event_source_pages.append(event_source_page)
        logger.info(f"id: {id}, url: {url}")

    return event_source_pages


def explore_source_pages(configs):
    dataset_type = configs.dataset_type
    chrome_binary_location = configs.chrome_binary_location
    task_metadata_path = configs.task_metadata_path

    driver = init_driver(chrome_binary_location, is_headless=configs.is_headless)
    event_source_pages = read_dataset_metadata(task_metadata_path, dataset_type)

    for event_source_page in event_source_pages:
        id = event_source_page["id"]
        url = event_source_page["url"]
        html_path = f"data/{dataset_type}/htmls/{id}_with_hiddern_elements.html"
        html_absolute_path = "file://" + os.path.abspath(html_path)

        if not os.path.exists(html_path):
            logger.info(f"File {html_path} not found skip!")
            continue
        load_local_webpage(driver, html_path=html_absolute_path, url=url)


def load_local_webpage(driver, html_path, url):
    driver.get(html_path)
    script_command = f"window.history.replaceState({{}}, null, \"{url}\")"
    local_current_url = driver.current_url
    logger.info(script_command)
    driver.execute_script(script_command)
    current_url = driver.current_url

    time.sleep(5)
    logger.info(f"current_url: {current_url}, local_current_url: {local_current_url}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dataset explore')
    parser.add_argument('--config_file', default='system_explore_event_source_pages.config',
                        help='Configuration File')
    args = parser.parse_args()
    configs = Configure(config_file=args.config_file)
    fold_check(configs)
    logger = get_logger(log_dir=configs.log_dir)

    explore_source_pages(configs)
