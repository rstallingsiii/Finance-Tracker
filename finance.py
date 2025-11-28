import sqlite3
from datetime import date
today = date.today().isoformat()  


# Connect (creates file if doesn't exist)
def connectToDatabase():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    return conn, cursor

def createTransactionsTable():
    conn, cursor = connectToDatabase()
    transactionsCreationQuery = """CREATE TABLE IF NOT EXISTS TRANSACTIONS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trans_type VARCHAR(50) NOT NULL,
        amount REAL NOT NULL,
        category VARCHAR(50) NOT NULL,
        description VARCHAR(50) NOT NULL,
        date TEXT DEFAULT CURRENT_DATE
    );
    """
  

    # Execute SQL
    cursor.execute(transactionsCreationQuery)

    # Commit changes
    conn.commit()
    # 
    # # Close connection
    conn.close()

def addTransactions(trans_type,amount,category,description):
    conn, cursor = connectToDatabase()
    transactionsUpdate = """insert into TRANSACTIONS (trans_type, amount, category, description) VALUES (?,?,?,?)
    
"""
    cursor.execute(transactionsUpdate, (trans_type, amount, category, description))
    
    conn.commit()
    conn.close()

def main():
    createTransactionsTable()
    addTransactions('INCOME',2500.69,'INCOME', "The Galactic Republic")
    

if __name__ == "__main__":
    main()   