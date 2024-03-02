import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import customtkinter

conn = sqlite3.connect('../SERVER/db/tkinter.db')
cursor = conn.cursor()

def fetch_data(path, table):
    try:
        # Construct the SQL query to select all columns from the table
        select_query = f"SELECT * FROM {table}"

        # Use Pandas to read the data into a DataFrame
        df = pd.read_sql_query(select_query, conn)

        return df
    
    except sqlite3.Error as e:
        print(f"Error fetching data from table '{table}': {e}")
    
    finally:
        # Close the connection
        conn.close()

# def display_graph()


#graph view

def row_count(table_name):
    try:
        # Construct the SQL query to count rows in the table
        count_query = f"SELECT COUNT(*) FROM {table_name}"

        # Execute the query and fetch the result
        cursor.execute(count_query)
        row_count = cursor.fetchone()[0]

        return row_count
    
    except sqlite3.Error as e:
        print(f"Error getting row count for table '{table_name}': {e}")

def graph_display(tabView, table_names):
    row_counts = [row_count(table) for table in table_names]


    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)

    df = pd.DataFrame({'Table': table_names, 'Row Count': row_counts})
    ax.bar(df['Table'], df['Row Count'])
    ax.set_xlabel('Table')
    ax.set_ylabel('Number of Rows')
    ax.set_title('Number of Rows in Each Table')
    ax.tick_params(axis='x', rotation=45)

    figure.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9, wspace=0, hspace=0)
    canvas = FigureCanvasTkAgg(figure, master=tabView)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.1, rely=0.2)

#---------------------------------------------#