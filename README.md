# Explore-Event-Source-Dataset

This document describes how to install code on Windows 10/Ubuntu 16.04/18.04.

# Install

## Download Dataset

Go to **[here](https://eventgo.widm.csie.ncu.edu.tw/datasets/EventSourceCost/[003]offline_webpage.rar)** download **[003]offline_webpage.rar**.


Unzip rar and put it under the set data_dir path.
data
   |---start_from_homepage
   |---start_from_message
   └---\[ver003\]Task Information.xlsx


## Requirement install

    $ pip install -r requirements.txt


## Configure Settings


```
### use # to comment out the configure item
log_dir=logs

################ Datasets(Input) ################

data_dir=data
task_metadata_path=data/[ver003]Task Information.xlsx
dataset_type=start_from_message
# string: start_from_homepage/start_from_message

################  Settings ################

chrome_binary_location=D:/Program Files/Google/Chrome/Application/chrome.exe

is_headless=False
# string: True/False
```

 ## Evaluation API

Go to **[here](https://eventgo.widm.csie.ncu.edu.tw/datasets/EventSourceCost/[003]evaluation_API.rar)** download **[003]evaluation_API.rar**.
