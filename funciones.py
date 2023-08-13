# Modulos SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Modulos python
from decouple import config

# Modulos internos
from models import Usuarios



# Creación del motor (engine) de SQLAlchemy: Representará la conexión a la base de datos
engine = create_engine(config("DATABASE_URL"))

# Configuración de: clase Session con el motor: Manejará las interacciones con la base de datos
Session = sessionmaker(bind=engine)

# Creación de instancia a Session: Será utilizada para realizar operaciones en la base de datos
session = Session()





# Funcion: Todos los usuario
def all_users(session):
    users = session.query(Usuarios).all()
    session.close()

    list = []

    for user in users:
        list.append([user.id, user.nombre, user.edad])

    return list
    

    #return f"ID:, {users.id}, Nombre:, {users.nombre}, Edad:, {users.edad}
    




# Funcion: Crear usuario
def crear_usuario(session, p_id, p_nombre, p_edad):
    user = Usuarios(id= p_id , nombre= p_nombre, edad= p_edad)
    session.add(user)
    session.commit()
    session.close()

    print(f"Usuario {p_nombre} registrado correctamente")
    return f"Usuario {p_nombre} registrado correctamente"






# Funcion: Actualizar usuario
def actualizar_usuario(session, id, nombre, edad):

    usuario_actualizar = session.query(Usuarios).filter_by(id=id).first()

    if usuario_actualizar:
        usuario_actualizar.nombre = nombre
        usuario_actualizar.edad = edad
        session.commit()
        session.close()
        
        return f"Usuario {id} ha sido actualizado"
    
    else:
        return f"El usuario {id} no esta registrado"
    





# Funcion: Eliminar usuario
def eliminar_usuario(session, id):

    usuario_eliminar = session.query(Usuarios).filter_by(id=id).first()

    if usuario_eliminar:
        session.delete(usuario_eliminar)
        session.commit()
        session.close()
        return f"Usuario {id} ha sido eliminado"
    else:
        return f"Usuario {id} no esta registrado"