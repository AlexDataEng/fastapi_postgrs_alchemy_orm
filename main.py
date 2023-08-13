# Modulos FastAPIP
from fastapi import FastAPI

# Modulos internos
from schema import User
from models import Usuarios

#Modulo interno: Funciones
from funciones import all_users as db_all_users, session
from funciones import actualizar_usuario as db_actualizar_usuario 
from funciones import eliminar_usuario as db_eliminar_usuarios



app = FastAPI(
    title= "Conexión a usuarios",
    description= "Esta es una api de practica")



# Obtener todos los usuarios
@app.get("/users")
def all_users():
    return db_all_users(session)



# Obtener usuario por id
@app.get("/users{user_id}")
def user_id(user_id:int):
    
    user_data = db_all_users(session)

    if user_id in user_data:

        # Creo una var que almacene la informacion JSON de ese usuario. Para luego acceder a los valores JSON
        user_info = user_data[user_id]

        # Accedo a los resultados
        r_user_id = user_id
        r_user_nombre = user_info["nombre"]
        r_user_edad = user_info["edad"]

        # Retorno los resultados
        return f"{r_user_id}, {r_user_nombre}, {r_user_edad}"
    
    else:
        return "Usuario no existe"



# Registrar usuario
@app.post("/users/create_user")
def create_user(user:User):

    new_user = Usuarios(user.id, user.nombre, user.edad)

    session.add(new_user)
    session.commit()
    session.close()

    return f"Usuario {user.nombre} ha sido registrado"



# Actualizar usuario
@app.put("/users/update_user/{id}")
def all_users(user:User):
    
    return db_actualizar_usuario(session, user.id, user.nombre, user.edad)



# Eliminar usuario
@app.delete("/users/delete_user{id}")
def all_users(id:int):
    return db_eliminar_usuarios(session, id)
