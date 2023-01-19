import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json
import os

def open_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not os.path.isfile(file_path):
        print("Invalid file path")
        exit()
    return file_path

def save_file(data):
    json_path = filedialog.asksaveasfilename()
    if json_path[-5:] != '.json':
        json_path += '.json'
    if not json_path:
        print("Invalid file path")
        exit()
    with open(json_path, 'w') as f:
        json.dump(data, f)
    print("File successfully converted and saved!")

def csv_to_json(file_path):
    df = pd.read_csv(file_path)
    data = df.to_dict(orient='records')
    save_file(data)

file_path = open_file()
csv_to_json(file_path)
