import sys
import sqlite3 as db
from datetime import datetime
import pandas as pd



def init():
    '''
    Initialize a new database to store the
    expenditures
    '''

    conn = db.connect('new.db')
    c = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS expense (category TEXT,
    amount REAL, message TEXT, date TEXT)'''
    c.execute(sql)
    conn.commit()
    conn.close()

def log(category, amount, message=""):
    '''
        logs the expenditure in the database.
        amount: number
        category: string
        message: (optional) string
        '''
    #print("Please Enter a New Record :")
    date = str(datetime.now())
    data = (category,amount, message, date)
    conn = db.connect('new.db')
    c = conn.cursor()
    sql = 'INSERT INTO expense VALUES (?,?,?,?)'
    c.execute(sql,data)
    conn.commit()
    conn.close()
    return category,amount, message

def view(category=None):
    '''
        Returns a list of all expenditure incurred, and the total expense.
        If a category is specified, it only returns info from that
        category
        '''
    conn = db.connect('new.db')
    c = conn.cursor()
    if category:
        sql = '''SELECT * FROM expense WHERE category = '{}' '''.format(category)
    else:
        sql = '''SELECT * FROM expense'''
    c.execute(sql)
    results = c.fetchall()
    conn.close()
    return results

def total():
    #Returns total expesnes from column amount
    conn = db.connect('new.db')
    df = pd.read_sql_query("Select * from expense", conn)
    df_sum = df['amount'].sum()
    print("Your Total Expense is : £", df_sum)

def catotal(category):
    conn = db.connect('new.db')
    c = conn.cursor()
    sql = '''
        SELECT sum(amount) FROM expense WHERE category = '{}'
        '''.format(category)
    c.execute(sql)
    results = c.fetchall()[0]
    return results



#Start making the whole program now
def calc():
    print("Welcome to the MASQ Expense Manager")
    total() #call the total() function here
    print("1: Do you want to enter a new record ? ")
    print("2: Do you want to view expense report for a category? ")
    print("3: Do you want to view total expense for a category? ")
    print("q: Do you want to exit the system? ")

    choice = input("Enter Choice (1/2/3/q) : ")

    if choice =='1':
       cat = input("Enter the Category Name : ")
       amnt = float(input("Enter the Amount Spent : "))
       msg = input("Enter the Message : ")
       log(cat, amnt,msg)

    elif choice == '2':
        cat1 = input("Enter the Category Name : ")
        print(view(cat1))

    elif choice == '3':
        cat1 = input("enter the category ")
        print(catotal(cat1))


    elif choice =='q'or 'Q':
        sys.exit()

    else:
        calc()

calc()











