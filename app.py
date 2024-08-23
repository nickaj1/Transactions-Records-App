'''
This file contains functions for getting, creating, updating, 
deleting, searching and adding up transaction records.
'''

# Import libraries
from flask import Flask, render_template, redirect, url_for, request
from Data.database import load_data, save_data


# Instantiate Flask functionality
app = Flask(__name__)


# Read operation
@app.route("/")
def get_transactions():
    '''Get transaction page'''
    transactions = load_data()
    save_data(transactions)
    return render_template('transactions.html', transactions=transactions)


# Create operation
@app.route('/add',methods=['GET','POST'])
def add_transaction():
    '''This function enables user to add a new transaction to the transaction list'''
    if request.method == 'GET':
        return render_template('form.html')
    

    else:
        # creating a new transaction and appending to the transactions list
        transactions = load_data()

        transaction = {
            'id': len(transactions) + 1, # incrementing id value by 1 
            'date': request.form['date'], # request.form function parses the date received from the entry made in the form
            'amount': float(request.form['amount']) #  request.form function parses the amount received from the entry made in the form
        }
        # Appending the new transaction to the transactions list
        transactions.append(transaction)

        # Save the updated transactions list
        save_data(transactions)
        
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for('get_transactions'))


# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET','POST'])
def edit_transaction(transaction_id):
    '''This function enables user to edit a the transaction list'''
    transactions = load_data()

    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction=transaction)
    
    else:
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        save_data(transactions)
        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))



# Delete operation
@app.route("/delete/<int:transaction_id>", methods=['GET','POST'])
def delete_transaction(transaction_id):
    '''This function finds duplicate id and delete the id from the transaction list'''
    transactions = load_data()

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    save_data(transactions)

    # Redirect to the transactions list page after updating the transaction
    return redirect(url_for("get_transactions"))


# 
@app.route('/search', methods=['GET','POST'])
def search_transactions():
    '''This function search for list of transaction id which fall between a given range'''
    if request.method == "GET":
        return render_template('search.html')
    

    else:
        # loading the transaction data
        transactions = load_data()

        # requesting the min_amount and max_amount from user
        min_amount = int(float(request.form['min_amount']))
        max_amount = int(float(request.form['max_amount']))

        # List comprehension
        filtered_transactions = [
            transaction for transaction in transactions
            if transaction['amount'] in range(min_amount, max_amount)
        ]
        # parse the new list 'filtered_transactions' to the main transactions list
        return render_template('transactions.html', transactions=filtered_transactions)


# summing all the total balance of the transactions
@app.route('/balance', methods=['GET','POST'])
def total_balance():
    '''This function sum all the amount of transactions in the list'''
    transactions = load_data()
    balance = sum(transaction['amount'] for transaction in transactions)
    return render_template('transactions.html',transactions=transactions, balance=balance)
        



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    