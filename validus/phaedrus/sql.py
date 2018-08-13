# -*- coding: utf-8 -*-
import sqlite3, csv, sys, os
from operator import itemgetter



def create_table_GBPEUR():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE GBPEUR(
            pub_date TEXT,
            currency_pair TEXT,
            fx_value REAL)''')
    db.commit()
    db.close()

def load_GBPEUR():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    with open('Documentation/GBPEUR.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        to_db = [(i['pub_date'], i['currency_pair'], i['fx_value']) for i in reader]
        cursor.executemany('''
                INSERT INTO GBPEUR(pub_date,
                currency_pair,
                fx_value
                VALUES (?, ?, ?);''', to_db)
        db.commit()
        db.close()


def create_table_GBPUSD():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE GBPUSD(
            pub_date TEXT,
            currency_pair TEXT,
            fx_value REAL)''')
    db.commit()
    db.close()

def load_GBPUSD():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    with open('Documentation/GBPUSD.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        to_db = [(i['pub_date'], i['currency_pair'], i['fx_value']) for i in reader]
        cursor.executemany('''
                INSERT INTO GBPUSD(pub_date,
                currency_pair,
                fx_value
                VALUES (?, ?, ?);''', to_db)
        db.commit()
        db.close()



# SQL statement to fecth data from the database. Ideally the SQL code should not
# be exposed in the code for security reasons.
def build_fetch_statement(currency_pair):
    query_strings = []
    query_element = 'SELECT pub_date,'
    query_strings.append(query_element + currency_pair )
    query_strings.append(query_element + ' fx_value FROM GBPEUR ORDER BY pub_date')



    return query_strings

# Save results in a csv file under the Documentation folder
#The results.csv should be passed as a variable to change the name of the file
# i.e.  Daily_Returns, Average, Standard_Deviation, Covariance, Correlation
def generate_resultset(query):
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        with open("Documentation/results.csv", "wb") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])  # write headers
            csv_writer.writerows(results)









