__author__ = 'user'

import pyodbc
# DESKTOP - P2C1O13\SQLEXPRESS2008
    # N11 - TO - TBSQL01
def get_connection(dbname):
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-P2C1O13\SQLEXPRESS2008;database=%s;Trusted_Connection=yes;' % (dbname))
    return cnxn

def execute_Insert_sql(dbname,sqlquery, *args):
    con = get_connection(dbname)
    csr = con.cursor()
    # print(list(args))
    csr.execute(sqlquery, list(args))
    resultset = csr.rowcount
    con.commit()
    csr.close()
    del csr
    con.close()
    return resultset

def execute_InsertSelect_sql(dbname,sqlquery, *args):
    con = get_connection(dbname)
    csr = con.cursor()
    # print(list(args))
    csr.execute(sqlquery, list(args))
    resultset = csr.fetchall()

    con.commit()
    csr.close()
    del csr
    con.close()
    return resultset

def execute_delete_sql(dbname,sqlquery, *args):
    con = get_connection(dbname)
    csr = con.cursor()
    csr.execute(sqlquery, list(args))
    deletedrows = csr.rowcount
    con.commit()
    csr.close()
    del csr
    con.close()
    return deletedrows