import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
   
#Servicios REST
################################################################
#Bloque de Usuarios
################################################################
#GET de todos los Usuarios
@app.route('/api_rest/usuarios/get')
def get_usuarios():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM py_Usuarios")
        userRows = cursor.fetchall()
        respone = jsonify(userRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

#GET de un usuario por ID
@app.route('/api_rest/usuarios/get/<int:user_id>')
def get_usuario_id(user_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM py_Usuarios WHERE us_idUsuario =%s", user_id)
        userRow = cursor.fetchone()
        respone = jsonify(userRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 
#GET de un usuario por Email
@app.route('/api_rest/usuarios/get/<String:user_email>')
def get_usuario_email(user_email):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM py_Usuarios WHERE us_correo =%s", user_email)
        userRow = cursor.fetchone()
        respone = jsonify(userRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

#POST creacion basica de un usuario
@app.route('/api_rest/usuarios/post', methods=['POST'])
def create_usuario():
   
    try:        
        _json = request.json
        _tipoUsuario = _json['tipoUsuario']
        _estadoUsuario = _json['estadoUsuario']
        _nivelUsuario = _json['nivelUsuario']
        _correo = _json['correo']
        _contrasena = _json['contrasena']	

        if _tipoUsuario and _estadoUsuario and _nivelUsuario and _correo and _contrasena and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO py_Usuarios(us_tipoUsuario, us_estadoUsuario, us_nivelUsuario, us_correo,us_contrasena) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_tipoUsuario, _estadoUsuario, _nivelUsuario, _correo, _contrasena)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
#PUT actualizacion basica de un usuario
@app.route('/api_rest/usuarios/put', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and _id and request.method == 'PUT':			
            sqlQuery = "UPDATE emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/api_rest/usuarios/del/<int:user_id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM emp WHERE id =%s", (id,))
		conn.commit()
		respone = jsonify('Employee deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
       
       
@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hola API REST!</h1>" 


if __name__ == "__main__":
    app.run('0.0.0.0')