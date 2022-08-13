import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('luna.db')
        return con
    except Error:
        print(Error)

def sql_edit_usuario(name, lastname, username, tel, sex, birddate):
    strsql='UPDATE Usuarios SET  Nombres = ?, Apellidos = ?,  Genero = ?, FechadeNacimiento = ?, Telefono = ? WHERE Email = ?;'
    # strsql="UPDATE Usuarios SET Nombres ='"+ name +"', Apellidos ='"+ lastname+"' WHERE Email ='"+username+"';"
    # strsql="UPDATE Usuarios SET Nombres ='Carlos Alberto', Apellidos ='Mendoza Llerena' WHERE Email ='cway@outlook.com';"
    print(birddate)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,(name, lastname, sex, birddate, tel, username))
    con.commit()
    con.close()

def sql_select_all_usuario(username):
    strsq="SELECT * FROM Usuarios WHERE Email ='"+ username +"';"
    # strsq="SELECT * FROM Usuarios WHERE Email ='cway@outlook.com';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    usuario = cursor_Obj.fetchone()
    con.close()
    return usuario

def sql_select_all_ReservaU(username):
    strsq="SELECT * FROM Reservas WHERE IdUsuario ='"+ username +"';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    reservas = cursor_Obj.fetchall()
    con.close()
    return reservas

def sql_select_Reserva_byId(id):
    strsq="SELECT * FROM Reservas WHERE IdUsuario ='"+ id +"';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    reservas = cursor_Obj.fetchall()
    con.close()
    return reservas

def sql_edit_rate_reserva(id, rate, comentario):
    strsql='UPDATE Reservas SET Calificacion = ?, Comentario = ? WHERE Id = ?;'
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql, (int(rate), comentario, int(id)))
    con.commit()
    con.close()

def mardeluna(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol):
    con = sql_connection()
    cursor_Obj = con.cursor()
    datura = "INSERT INTO Usuarios (Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol) VALUES(?, ?, ?, ?, ?, ?, ?);"
    print(Email)
    cursor_Obj.execute(datura,(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol))
    con.commit()
    con.close()

def sql_auth_user(username, password):
    strsq="SELECT * FROM Usuarios WHERE Email = ? AND Contraseña =?;"
    # strsq="SELECT * FROM Usuarios WHERE Email ='cway@outlook.com';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq,(username, password))
    usuario = cursor_Obj.fetchall()
    con.close()
    return usuario

def morpheo(FechaInicio, FechaFinal, costo, Estado):
    con = sql_connection()
    cursor_Obj = con.cursor()
    dreamer = "INSERT INTO Reservas (FechaInicio, FechaFinal, costo, Estado) VALUES(?, ?, ?, ?);"
    print(FechaInicio)
    cursor_Obj.execute(dreamer,(FechaInicio, FechaFinal, costo, Estado))
    con.commit()
    con.close()

