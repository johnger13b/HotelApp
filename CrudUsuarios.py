import sqlite3
from sqlite3 import Error

from app import sql_connection

def sql_connection():
    try:
        con=sqlite3.connect('baseDatos.db')
        return con
    except Error:
        print(Error)

def mardeluna(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol):
    datura = "INSERT INTO Usuarios (Email, Nombres, Apellidos, Contraseña, Fecha de Nacimiento, Genero, Rol) VALUES("+ Email +", "+ Nombres + ", "+Apellidos+", "+Contraseña+","+FechadeNacimiento+", "+Genero+", "+Rol+");"
    print(datura)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(datura)
    con.commit()
    con.close()