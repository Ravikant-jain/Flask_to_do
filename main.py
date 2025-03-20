import pandas as pd
import numpy as np
from datetime import datetime
import json 
import os

# Define the folder and file path
folder_path = "data"
file_path = os.path.join(folder_path, "data.json")

# Check if the file exists
if os.path.exists(file_path):
    # Read the existing JSON file
    with open(file_path, "r") as file:
        try:
            data = json.load(file)  # Load data into a dictionary
        except json.JSONDecodeError:
            data = {}  # If the file is empty or corrupted, initialize as empty
else:
    # Create an empty JSON file and initialize an empty dictionary
    data = {}
    with open(file_path, "w") as file:
        json.dump(data, file)

print(f"Data loaded: {data}")


#C
def create_tsk(tsk,data):
    if len(data.keys())==0:id=1
    else:id = int(max(data.keys())) + 1
    
    data[id]={'Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              'Task':tsk}
    with open(r"data/data.json", "w") as file:
        json.dump(data, file, indent=4)
#R
def read_tsk(id,data):
    return data[str(id)]['Task']
#U
def edit_tsk(n_tsk,id,data):
    n_tsk="* "+n_tsk
    data[str(id)]['Task'] = n_tsk
    with open(r"data/data.json", "w") as file:
        json.dump(data, file, indent=4)
#D
def delete_tsk(id,data):
    try:
        item=data.pop(str(id))
        print(f" task deleted --> {item['Task']}")
        with open(r"data/data.json", "w") as file:
            json.dump(data, file, indent=4)
        return item['Task']
    
    except:print('Task not found')