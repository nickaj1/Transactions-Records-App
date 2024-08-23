'''This file contains function that stores and read data'''
import json

# json file for data storage
transactions_file = "transactions.json"


# Sample data
sample_transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


def save_data(transactions):
    '''This function saves the data'''
    try: 
        with open(transactions_file, 'w') as file:
            json.dump(transactions, file, indent=3)
    except IOError as e:
        print(f"Error saving data: {e}")


# Load data
def load_data():
    '''This functions loads the data from the json file'''
    try: 
        with open(transactions_file, 'r') as file1:
            load_message =  json.load(file1)
        return load_message
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []


save_data(sample_transactions)