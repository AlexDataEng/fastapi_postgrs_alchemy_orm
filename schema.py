#Modulos Pydantic
from pydantic import BaseModel

#Modulos FastAPI
from fastapi import Path



#Esquema: Usuario (User)
class User(BaseModel):
    id : int
    nombre : str = Path(...)
    edad : int = Path(...)