# Explore-Event-Source-Dataset

This document describes how to install code on Windows 10/Ubuntu 16.04/18.04.

# Install

## Download Dataset

Go to **[here](https://eventgo.widm.csie.ncu.edu.tw/datasets/EventSourceCost/[003]offline_webpage.rar)** download **[003]offline_webpage.rar**.


Unzip rar and put it in the set data_dir path.<br>
````
root
└── data
    ├── start_from_homepage
    ├── start_from_message
    └── [ver003]Task Information.xlsx
````


## Requirement install

    $ pip install -r requirements.txt


## Configure Settings


```
### use # to comment out the configure item
log_dir=logs

################ Datasets(Input) ################

data_dir=data
task_metadata_path=data/[ver003]Task Information.xlsx
dataset_type=start_from_homepage
# string: start_from_homepage/start_from_message

################  Settings ################

chrome_binary_location=D:/Program Files/Google/Chrome/Application/chrome.exe

is_headless=False
# string: True/False
```

 ## Evaluation API

Go to **[here](https://eventgo.widm.csie.ncu.edu.tw/datasets/EventSourceCost/[003]evaluation_API.rar)** download **[003]evaluation_API.rar**.

Go to **[here](https://eventgo.widm.csie.ncu.edu.tw/datasets/EventSourceCost/[003]EventSourcePageDiscovery%20%E8%B3%87%E6%96%99%E9%9B%86%E4%BD%BF%E7%94%A8%E8%AA%AA%E6%98%8E.pptx)** download **[003]EventSourcePageDiscovery 資料集使用說明.pptx**.

For more instructions on the Evaluation API, please refer to \[003\]EventSourcePageDiscovery 資料集使用說明.pptx