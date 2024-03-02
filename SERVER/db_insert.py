import json
import re
import pandas as pd
import sqlite3

def get_json_name(file_path):
    pattern = r'\/([^\/]+)(?=\.\w+$)'

    match = re.search(pattern, file_path)

    if match:
        return match.group(1)
    else:
        print("No match found.")

def json_to_sql(json_data, json_name, connection):
    
    if isinstance(json_data, list):
        df = pd.DataFrame(json_data)
        df = df.astype(str)
        df.to_sql(name=json_name, con=connection, index=False, if_exists='replace')
    
    elif isinstance(json_data, dict):
        df = pd.DataFrame(json_data)
        df.to_sql(name=json_name, con=connection, index=False, if_exists='replace')
    
    else:
        print("Unsupported JSON format")
        
    return None


def sql_to_db(path):
    
    # Example usage:
    path = "./json_file/Film.json"
    json_name = get_json_name(path)
    try:
        #------------------------------------------------------#
        #open json and translate it to a mysql query
        connection = sqlite3.connect("./db/tkinter.sqlite")

        with open(path, 'r') as f:
            json_data = json.load(f)
            json_to_sql(json_data, json_name, connection)
        #------------------------------------------------------#
        
        print('success')
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        