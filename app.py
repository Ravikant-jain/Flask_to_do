import pandas as pd
import numpy as np
from datetime import datetime
import json 
import os

# Define the folder and file pathpip
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

# print(f"Data loaded: {data}")


#C
def create_tsk(tsk,data):
    if len(data.keys())==0:id=0
    else:id = int(len(data.keys())) + 1
    id=str(id)
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
    print(f'----\n {data} \n----')
    try:
        # del data[str(id)]
        item=data.pop(str(id))
        print(f" task deleted --> {item['Task']}")
        with open(r"data/data.json", "w") as file:
            json.dump(data, file, indent=4)
        return item['Task']
    
    except Exception as e :print('Task not found' , e)
    

#Flask app starts here
from flask import Flask , render_template , url_for , request , redirect
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        tsk_con=request.form['content']
        create_tsk(tsk_con,data)
        return redirect('/')

    else:
        # tasks=data
        return render_template("index.html",tasks=data)
    
@app.route('/delete/<int:id>')
def delete(id):
    delete_tsk(id,data)
    return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    print('update hone aaya')
    task=data[str(id)]['Task']
    print(task)
    if request.method=='POST':
        print('post req called')
        nc=request.form['content']
        print(nc,"post req called")
        edit_tsk(nc,id,data)
        return redirect('/')
    else:
        print('GET req called')
        return render_template('update.html',task=task,id=id)


app.run( debug= True ,host="0.0.0.0", port=80)