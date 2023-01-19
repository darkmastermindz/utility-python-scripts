import pandas as pd
import tkinter as tk
from tkinter import filedialog
import json
import os

def open_file():
    """
    This function opens a file dialog box for selecting a file.
    It also checks if the file path is valid or not.
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not os.path.isfile(file_path):
        print("Invalid file path")
        exit()
    return file_path

def save_file(data):
    """
    This function opens a save dialog box for selecting the location and name of the file.
    It also checks if the file path is valid or not.
    It then saves the json file with the data passed as an argument.
    """
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
    """
    This function reads the csv file, converts it to a dictionary using to_dict(orient='records')
    which treats each row as a separate object in an array, and saves it as json
    """
    df = pd.read_csv(file_path)
    data = df.to_dict(orient='records')
    save_file(data)

file_path = open_file()
csv_to_json(file_path)
