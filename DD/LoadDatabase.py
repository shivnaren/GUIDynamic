import  pyodbc
def loadDatabase():
    databasenames = []
    # database = 'master'
    # DESKTOP - P2C1O13\SQLEXPRESS2008
    # N11 - TO - TBSQL01
    DBload_cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-P2C1O13\SQLEXPRESS2008;database=master;Trusted_Connection=yes;')
    cursor = DBload_cnxn.cursor()
    databasename_sql = "SELECT name FROM sys.databases"
    cursor.execute(databasename_sql)
    databases_res = cursor.fetchall()
    for database in databases_res:
        databasenames.append(database[0])
    # print(databasenames)

    return databasenames
