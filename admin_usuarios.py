import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('luna.db')
        return con
    except Error:
        print(Error)

def sql_select_usuario(id):
    strsql = "SELECT * FROM Habitaciones WHERE Id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion

def sql_update_usuario(id, Nestado):
    strsql = 'UPDATE Habitaciones SET Estado = "'+Nestado+'" WHERE Id = '+id+';'
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_usuario(id):
    strsql = "DELETE FROM Habitaciones WHERE Id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
