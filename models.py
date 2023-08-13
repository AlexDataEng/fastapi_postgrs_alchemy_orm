# Modulos SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Modelo de Tabla: comercial.usuarios
class Usuarios(Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'schema': 'comercial'}  # Especifica el esquema
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    
    def __init__(self, id, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.id = id



