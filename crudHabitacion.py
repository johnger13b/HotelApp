import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('luna.db')
        return con
    except Error:
        print(Error)
#------------------------------------------------------------------------------------------------------------------
def sql_add_habitacion(id, estado):
    try:  # me conecto a la base de datos
        con = sql_connection()
        # creo un cursor para poder ejecutar las consultas
        cursor_Obj = con.cursor()
        # creo la consulta para insertar una habitacion
        strsql = "INSERT INTO Habitaciones (Id,Estado) VALUES(?,?);"
        print(strsql)
        valores = (id, estado)
        # ejecuto la consulta
        cursor_Obj.execute(strsql, valores)
        con.commit()
    except Error as e:
        # si hay algun error lo muestro y retorno None
        print(e)
        return None
    finally:
        # cierro la conexion a la base de datos
        con.close()
        
    return cursor_Obj.lastrowid # retorno el id de la habitacion insertada
#------------------------------------------------------------------------------------------------------------------
def sql_crear_tabla_habitaciones():
    strsql = "CREATE TABLE IF NOT EXISTS Habitaciones (Id INTEGER PRIMARY KEY, Estado TEXT);"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
#------------------------------------------------------------------------------------------------------------------
def sql_update_habitacion(id, Nestado):
    strsql = 'UPDATE Habitaciones SET Estado = "'+Nestado+'" WHERE Id = '+id+';'
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
#------------------------------------------------------------------------------------------------------------------
def sql_delete_habitacion(id):
    strsql = "DELETE FROM Habitaciones WHERE Id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitaciones():
    strsql = "SELECT * FROM Habitaciones;"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitaciones = cursor_Obj.fetchall()
    con.close()
    return habitaciones
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion(id):
    strsql = "SELECT * FROM Habitaciones WHERE Id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado(estado):
    strsql = "SELECT * FROM Habitaciones WHERE Estado = "+estado+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado_disponible():
    strsql = "SELECT * FROM Habitaciones WHERE Estado = 'Disponible';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado_ocupada():
    strsql = "SELECT * FROM Habitaciones WHERE Estado = 'Ocupada';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado_reservada():
    strsql = "SELECT * FROM Habitaciones WHERE Estado = 'Reservada';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
